import os
import sys
import json
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from data.db import init_db, get_config, set_config
from core.space import get_available_space, human_readable, check_space
from core.backup import run_backup
import json as json_module


def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    init_db()

    @app.route("/")
    def index():
        backup_root = get_config("backup_root")
        return render_template("index.html", backup_root=backup_root)

    @app.route("/api/status")
    def status():
        backup_root = get_config("backup_root")
        return jsonify({
            "configured": backup_root is not None,
            "backup_root": backup_root
        })

    @app.route("/api/setup", methods=["POST"])
    def setup():
        data = request.get_json()
        folder_name = data.get("folder_name", "").strip()
        parent_path = data.get("parent_path", "").strip()

        if not folder_name:
            return jsonify({"success": False, "error": "Ingresá un nombre para la carpeta."})
        if not parent_path:
            return jsonify({"success": False, "error": "Seleccioná dónde crear la carpeta."})

        full_path = os.path.join(parent_path, folder_name)
        try:
            os.makedirs(full_path, exist_ok=True)
            set_config("backup_root", full_path)
            return jsonify({"success": True, "path": full_path})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)})

    @app.route("/api/browse")
    def browse():
        path = request.args.get("path", "")

        if not path:
            return jsonify({"items": _get_roots(), "current": "", "parent": None})

        if not os.path.isdir(path):
            return jsonify({"error": "Ruta no válida", "items": []})

        items = []
        try:
            entries = sorted(os.scandir(path), key=lambda e: e.name.lower())
            for entry in entries:
                if entry.is_dir() and not entry.name.startswith("."):
                    items.append({
                        "name": entry.name,
                        "path": entry.path,
                    })
        except PermissionError:
            pass

        parent = str(os.path.dirname(path))
        if parent == path:
            parent = None

        return jsonify({"items": items, "current": path, "parent": parent})

    @app.route("/api/space")
    def space():
        folders_raw = request.args.get("folders", "[]")
        backup_root = get_config("backup_root", os.path.expanduser("~"))
        try:
            folders = json_module.loads(folders_raw)
        except Exception:
            folders = []

        if not folders:
            avail = get_available_space(backup_root)
            return jsonify({
                "has_space": True,
                "total_needed": 0,
                "available": avail,
                "total_needed_human": "0 B",
                "available_human": human_readable(avail),
                "margin_human": human_readable(avail),
            })

        result = check_space(folders, backup_root)
        return jsonify(result)

    @app.route("/api/backup", methods=["POST"])
    def backup():
        from data.db import save_backup
        data = request.get_json()
        folders = data.get("folders", [])
        backup_root = get_config("backup_root")

        if not backup_root:
            return jsonify({"success": False, "error": "Primero configurá la carpeta de backups."})
        if not folders:
            return jsonify({"success": False, "error": "Seleccioná al menos una carpeta."})

        result = run_backup(backup_root, folders)
        save_backup(result, folders)
        return jsonify(result)

    @app.route("/api/history")
    def history():
        from data.db import get_backups
        return jsonify(get_backups())

    @app.route("/api/delete/<int:backup_id>", methods=["DELETE"])
    def delete_backup(backup_id):
        from data.db import get_backups, delete_backup_record
        include_files = request.args.get("files", "false") == "true"
        backups = get_backups()
        record = next((b for b in backups if b["id"] == backup_id), None)

        if not record:
            return jsonify({"success": False, "error": "Backup no encontrado."})

        if include_files and record["backup_path"] and os.path.isdir(record["backup_path"]):
            try:
                shutil.rmtree(record["backup_path"])
            except Exception as e:
                return jsonify({"success": False, "error": str(e)})

        delete_backup_record(backup_id)
        return jsonify({"success": True})

    return app


def _get_roots():
    items = []
    if os.name == "nt":
        import string
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                items.append({"name": f"Disco {letter}:", "path": drive})
    else:
        home = os.path.expanduser("~")
        items.append({"name": "Carpeta personal", "path": home})
        items.append({"name": "Raíz del sistema (/)", "path": "/"})
    return items
