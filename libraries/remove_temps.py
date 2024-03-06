import os, shutil
from datetime import datetime

# Directories to search for temporary files

temp_dirs = [
    '~/Downloads',
    '~/Desktop'
    'C:/Users/Appdata/Local/Temp'
]

# Extensions of the temporary files

temp_ext = [
    '.log',
    '.tmp',
    '.cache'
]

def remove_temps():
    for dir in temp_dirs:
        for dir_path, dir_name, file_names in os.walk(os.path.expanduser(dir)):
            for file_name in file_names:
                # check to see if the file extension is in the list of temporary files extension
                if os.path.splitext(file_name)[1].lower() in temp_ext:
                    file_path = os.path.join(dir_path, file_name)
                    try:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)

                        f = open("../logs/remove_temps.log", "w")
                        f.write(f"{datetime.now()}: Removed {file_path}\n")
                        f.close()
                    except Exception as e:
                        f = open("../logs/remove_temps_error.log", "w")
                        f.write(f"{datetime.now()}: Error deleting {file_path}: {e}\n")

                    # Remove screenshots from the Desktop
                    if dir == '~/Desktop':
                        desktop_path = os.path.expanduser(dir) # expand ~ to /home directory
                        screenshot_files = [f for f in os.listdir(desktop_path) if f.startswith('Screenshot')]
                        for file in screenshot_files:
                            file_path = os.path.join(desktop_path, file)
                            try:
                                os.remove(file_path)
                                f = open("../logs/remove_temps.log", "w+")
                                f.write(f"{datetime.now()}: Removed {file_path}\n")
                                f.close()
                            except Exception as e:
                                f = open("../logs/remove_temps_error.log", "w")
                                f.write(f"{datetime.now()}: Error deleting {file_path}: {e}\n")
                                f.close()