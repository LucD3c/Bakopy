import sys
import os
import subprocess
import importlib


def install_flask():
    print("=========================================")
    print("  Bakopy - Primer arranque")
    print("  Instalando dependencias necesarias...")
    print("=========================================")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "--quiet"])
    print("  Listo.\n")


def check_dependencies():
    try:
        importlib.import_module("flask")
    except ImportError:
        install_flask()


def main():
    check_dependencies()

    import threading
    import webbrowser
    import time

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ui.app import create_app

    app = create_app()

    def open_browser():
        time.sleep(1.2)
        webbrowser.open("http://localhost:5099")

    print("=========================================")
    print("  Bakopy está corriendo")
    print("  Abriendo en: http://localhost:5099")
    print("  Para cerrar: CTRL+C")
    print("=========================================")

    threading.Thread(target=open_browser, daemon=True).start()
    app.run(host="0.0.0.0", port=5099, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
