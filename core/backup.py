import os
import shutil
from datetime import datetime
from core.scanner import get_category
from core.space import check_space, human_readable


def run_backup(backup_root, folders):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(backup_root, timestamp)

    space = check_space(folders, backup_root)
    if not space["has_space"]:
        return {
            "success": False,
            "error": (
                f"Espacio insuficiente. Necesitás {space['total_needed_human']} "
                f"pero solo tenés {space['available_human']} disponibles."
            ),
            "timestamp": timestamp,
        }

    os.makedirs(backup_folder, exist_ok=True)

    stats = {
        "copied": 0,
        "skipped": 0,
        "errors": [],
        "categories": {},
        "total_size": 0,
    }

    for folder in folders:
        if not os.path.isdir(folder):
            stats["errors"].append(f"Carpeta no encontrada: {folder}")
            continue

        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                src = os.path.join(dirpath, filename)
                category = get_category(filename)

                dest_dir = os.path.join(backup_folder, category)
                os.makedirs(dest_dir, exist_ok=True)

                dest = os.path.join(dest_dir, filename)

                if os.path.exists(dest):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest):
                        dest = os.path.join(dest_dir, f"{base}_{counter}{ext}")
                        counter += 1

                try:
                    shutil.copy2(src, dest)
                    size = os.path.getsize(src)
                    stats["copied"] += 1
                    stats["total_size"] += size
                    stats["categories"][category] = (
                        stats["categories"].get(category, 0) + 1
                    )
                except (OSError, PermissionError) as e:
                    stats["skipped"] += 1
                    stats["errors"].append(f"{filename}: {str(e)}")

    return {
        "success": True,
        "timestamp": timestamp,
        "backup_path": backup_folder,
        "copied": stats["copied"],
        "skipped": stats["skipped"],
        "errors": stats["errors"][:10],
        "categories": stats["categories"],
        "total_size": human_readable(stats["total_size"]),
        "space_info": space,
    }
