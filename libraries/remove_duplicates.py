import os, re, datetime

def remove_duplicates(directory):
    timestamp = datetime.datetime.today()
    f = open("logs/remove_duplicates.log", "w")
    for root, _, files in os.walk(directory):
        files_dict = {}
        for file in files:
            file_path = os.path.join(root, file)

            # check if a file is a duplicate
            file_match = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', file)
            if file_match:
                file_name = file_match.group(1)
                file_number = int(file_match.group(2))
                file_extension = file_match.group(3)

                # Add file to the dictionary {file_name: [(file_number, file_path, file_extension)]}
                if file_name not in files_dict:
                    files_dict[file_name] = [(file_number, file_path, file_extension)]
                else:
                    files_dict[file_name].append((file_number, file_path, file_extension))

        # Rename files in each group
        for file in files_dict:
            file_detail = files_dict[file]
            file_detail.sort(key = lambda file_name: file_name[0])
            print(file_detail)
            latest_file_path = file_detail[-1][1]
            latest_file_extension = file_detail[-1][2]

            for file_number, file_path, _ in file_detail[:-1]:
                f.write(f"{timestamp}: Deleted duplicate file: {file_path}\n")
                os.remove(file_path)

            os.rename(latest_file_path, os.path.join(root, f"{file_name}{latest_file_extension}"))
            f.write(f"{timestamp}: Rename {latest_file_path} to {file_name}{latest_file_extension}\n")