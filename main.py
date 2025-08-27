import os
import sys
import subprocess

def load_installers(file):
    """
    Reads a text file containing the relative paths of the installers.
    """
    if not os.path.exists(file):
        input(f"❌ File not found: {file}. Press any key to exit the program.")
        return []

    with open(file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return lines

def launch_installers(paths):
    """
    Launches each executable/installer listed in `paths`.
    The paths are relative to the directory where this script is executed.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for rel_path in paths:
        full_path = os.path.join(base_dir, rel_path)
        if os.path.exists(full_path):
            inp = ""
            while inp not in ("y", "n"):
                inp = input("❓ Do you want to launch the installer of " + rel_path + " ? (y/n) : ").strip().lower()
                if inp == "y":
                    print(f"🔹 Launching: {full_path}")
                    try:
                        if sys.platform.startswith("win"):
                            subprocess.run([full_path], shell=True) # shell=True for .exe / .msi on Windows
                        elif sys.platform.startswith("linux"):
                            subprocess.Popen(["xdg-open", full_path]) # Linux
                        elif sys.platform == "darwin":
                            subprocess.Popen(["open", full_path]) # macOS
                    except Exception as e:
                        print(f"⚠️ Error launching {full_path}: {e}")
        else:
            input(f"❌ File not found: {full_path}. Please press Enter to continue.")

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "installers.txt"  # Path to the installers file or "installers.txt" if not provided
    paths = load_installers(file)
    launch_installers(paths)
