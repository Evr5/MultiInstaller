# MultiInstaller

A lightweight cross-platform Python script to **batch launch multiple installers** from a list of relative paths.  
Supports **Windows (.exe / .msi)**, **Linux**, and **macOS**.

---

## ✨ Features

- Reads a list of installers from a text file (`installers.txt` by default)  
- Asks confirmation before launching each installer  
- Supports **relative paths** (keeps installers organized in subfolders)  
- Cross-platform support:
  - ✅ Windows → `.exe` / `.msi`  
  - ✅ Linux → opens with `xdg-open`  
  - ✅ macOS → opens with `open`  

---

## 📦 Installation

Clone the repository:

```bash
git clone git@github.com:Evr5/MultiInstaller.git
cd MultiInstaller
python main.py
```

## 📝 Usage

1. Place your installers in subfolders (for example: ChromeSetup/ChromeSetup.exe, VLC/vlc_installer.exe, etc.)

2. Create a file installers.txt (or another name) in the same directory as the script.
Example:

    ```txt
    ChromeSetup/ChromeSetup.exe
    VLC/vlc_installer.exe
    7zip/7z1900-x64.exe
    ```

3. Run the launcher:

    ```bash
    python launcher.
    ```

    Or specify a custom list:

    ```bash
    python launcher.py mylist.txt   
    ```

## 🖥️ Example Folder Structure

```
📂 MultiInstaller
 ┣ 📄 main.py
 ┣ 📄 installers.txt
 ┣ 📂 ChromeSetup
 ┃   ┗ 📄 ChromeSetup.exe
 ┣ 📂 VLC
 ┃   ┗ 📄 vlc_installer.exe
 ┗ 📂 7zip
     ┗ 📄 7z1900-x64.exe
```

## ⚠️ Notes

- On Windows, you may need to run as Administrator for some installers.
- The script will ask confirmation (y/n) before launching each installer.
- Non-existent paths in the list will be skipped with a warning.
