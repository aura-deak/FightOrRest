import platform
import subprocess


def clear_console():
    """
    Cross-platform console clear (Windows/Linux/macOS).
    """
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


# Test
if __name__ == "__main__":
    print("This is content before clearing")
    input("Press Enter to clear the console...")
    clear_console()
    print("Console cleared, this is new content")
