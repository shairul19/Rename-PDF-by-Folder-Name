import os

# Write your main directory
root_directory = r"C:\path\to\your\main\folder" 

for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    if os.path.isdir(folder_path):  # Check if this is a folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".pdf"):  # Check if this is a pdf file
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, f"{folder_name}.pdf")
                
                # Check whether the file with the target name already exists
                if os.path.exists(new_file_path):
                    print(f"File already exists: {new_file_path}. Skipping...")
                else:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} -> {new_file_path}")
