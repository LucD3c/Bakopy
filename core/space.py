import os
import shutil
import ctypes
import platform


def get_folder_size(path):
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total += os.path.getsize(fp)
                except (OSError, PermissionError):
                    pass
    except (OSError, PermissionError):
        pass
    return total


def get_available_space(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        if platform.system() == "Windows":
            free_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                ctypes.c_wchar_p(path), None, None,
                ctypes.pointer(free_bytes)
            )
            return free_bytes.value
        else:
            st = os.statvfs(path)
            return st.f_bavail * st.f_frsize
    except Exception:
        return 0


def human_readable(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.1f} MB"
    else:
        return f"{size_bytes / (1024 ** 3):.2f} GB"


def check_space(folders, destination):
    total_needed = sum(get_folder_size(f) for f in folders)
    available = get_available_space(destination)
    margin = available - total_needed

    return {
        "has_space": available > total_needed,
        "total_needed": total_needed,
        "available": available,
        "margin": margin,
        "total_needed_human": human_readable(total_needed),
        "available_human": human_readable(available),
        "margin_human": human_readable(abs(margin)),
    }
