import os
import shutil
import sys


def get_to_keep(root_dir):
    # 1. Config file
    config_path = os.path.join(root_dir, 'list_of_file_to_keep.txt')
    if os.path.isfile(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            keep = [line.strip() for line in f if line.strip()]
            if keep:
                print(f"Using config file list_of_file_to_keep.txt: {keep}")
                return keep

    # 2. Command-line argument
    if len(sys.argv) > 1:
        keep = sys.argv[1:]
        print(f"Using files/folders from command line: {keep}")
        return keep

    # 3. Interactive input
    print("Enter comma-separated names of files/folders to keep:")
    user_input = input("To keep: ")
    keep = [x.strip() for x in user_input.split(',') if x.strip()]
    print(f"Using user input: {keep}")
    return keep

def disable_mods(root_dir):
    items_in_root = set(os.listdir(root_dir))
    mods_disabled_dir = os.path.join(root_dir, "mods_disabled")
    os.makedirs(mods_disabled_dir, exist_ok=True)

    to_keep = get_to_keep(root_dir)
    to_keep.append("mods_disabled")

    for item in items_in_root:
        if item in to_keep:
            continue
        src_path = os.path.join(root_dir, item)
        dest_path = os.path.join(mods_disabled_dir, item)
        try:
            shutil.move(src_path, dest_path)
            print(f"Moved {item} to mods_disabled")
        except Exception as e:
            print(f"Could not move {item}: {e}")

def enable_mods(root_dir):
    mods_disabled_dir = os.path.join(root_dir, "mods_disabled")
    if not os.path.isdir(mods_disabled_dir):
        print("No mods_disabled folder found. Nothing to restore.")
        return

    for item in os.listdir(mods_disabled_dir):
        src_path = os.path.join(mods_disabled_dir, item)
        dest_path = os.path.join(root_dir, item)
        try:
            shutil.move(src_path, dest_path)
            print(f"Restored {item} from mods_disabled")
        except Exception as e:
            print(f"Could not restore {item}: {e}")

def main():
    # Use the folder where the EXE is located
    if getattr(sys, 'frozen', False):
        root_dir = os.path.dirname(sys.executable)
    else:
        root_dir = os.path.dirname(os.path.abspath(__file__))

    print("Choose an option:")
    print("1. Disable mods (move mods to mods_disabled)")
    print("2. Enable mods (restore mods from mods_disabled)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        disable_mods(root_dir)
    elif choice == "2":
        enable_mods(root_dir)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
