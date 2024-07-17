import os
import shutil
import time
import sys

def move_fcbak_files(source_dir, backup_folder):
    """
    Move all .FCBak files from the source directory to the backup folder every second.
    Each .FCBak file is placed in a folder named after the original file, with enumeration
    to avoid overwriting, starting at 000 and continuing with 001, 002, etc.

    Args:
        source_dir (str): The directory to search for .FCBak files.
        backup_folder (str): The folder to move .FCBak files to.
    """
    try:
        # Ensure the backup folder exists
        os.makedirs(backup_folder, exist_ok=True)

        while True:
            for filename in os.listdir(source_dir):
                if filename.endswith(".FCBak"):
                    source_path = os.path.join(source_dir, filename)
                    file_base_name = os.path.splitext(filename)[0]
                    destination_dir = os.path.join(backup_folder, file_base_name)

                    # Ensure the individual backup folder exists
                    os.makedirs(destination_dir, exist_ok=True)

                    # Enumerate to avoid overwriting starting at 000
                    file_counter = 0
                    destination_path = os.path.join(destination_dir, f"{file_base_name}{file_counter:03}.FCBak")
                    while os.path.exists(destination_path):
                        file_counter += 1
                        destination_path = os.path.join(destination_dir, f"{file_base_name}{file_counter:03}.FCBak")

                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} -> {destination_path}")

            # Wait for 1 second before the next iteration
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Press Enter to exit...")
        input()
        sys.exit(1)

if __name__ == "__main__":
    source_directory = r"C:\Home\CAD\001 Projects"
    backup_directory = r"C:\Home\CAD\001 Projects\.Backups"

    move_fcbak_files(source_directory, backup_directory)
