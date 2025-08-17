# RDR2Cleaner

A simple utility to temporarily disable or restore mods in your Red Dead Redemption 2 game folder by moving mod files to and from a `mods_disabled` folder.

## Features

- **Disable mods:** Moves all files/folders (except those you specify) into a `mods_disabled` folder.
- **Enable mods:** Restores all files/folders from `mods_disabled` back to the main folder.
- Supports a config file (`list_of_file_to_keep.txt`) to specify files/folders to keep.
- Works as a Windows executable or as a Python script.

---

## How to Use

### As a Windows Executable

1. **Download or build the executable** (see below).
2. **Place the EXE** in your RDR2 game folder.
3. **(Optional)**: Create a `list_of_file_to_keep.txt` in the same folder, listing files/folders (one per line) you want to keep. (This repo also have a vanilla list available with all files from first installation)
4. **Run the EXE** by double-clicking it.
5. **Choose an option:**
    - Enter `1` to disable mods (move mods to `mods_disabled`)
    - Enter `2` to enable mods (restore mods from `mods_disabled`)

### As a Python Script

1. Make sure you have Python 3 installed.
2. Place `rdr2cleaner.py` in your RDR2 game folder.
3. Open a terminal/command prompt in that folder.
4. Run:
    ```
    python rdr2cleaner.py
    ```
5. Follow the on-screen prompts.

---

## How to Compile to Windows Executable

1. Install [Python](https://www.python.org/downloads/) (if not already installed).
2. Install PyInstaller:
    ```
    pip install pyinstaller
    ```
3. Open a terminal in the folder containing `rdr2cleaner.py`.
4. Run:
    ```
    pyinstaller --onefile rdr2cleaner.py
    ```
5. The executable will be created in the `dist` folder. Move it to your RDR2 game folder.

---

## Notes

- The program will always keep the `mods_disabled` folder itself.
- If no config file is found, you can enter files/folders to keep when prompted.
- The program is designed for use in the RDR2 game folder, but can be used in any folder with similar needs.

---

## License

The software is licensed under MIT.
