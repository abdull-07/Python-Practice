# Week 8: Virtual Environments, pip libraries, os/sys/datetime Exercises:
    # Create a project folder and activate a virtual environment
    # Install libraries (requests, pandas, etc.)
    # Build a File Organizer:
        # Auto-create folders: Images, Docs, Videos
        # Move files to correct folder based on extension

import os
import shutil
import sys
import time

# 1️⃣ Create project folder (if not exists)
project_dir = "File Organizer"
if not os.path.exists(project_dir):
    os.makedirs(project_dir)
print(f"Project folder '{project_dir}' created.")

# 2️⃣ Create subfolders
subfolders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Docs": [".txt", ".pdf", ".docx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"]
}
for folder in subfolders:
    folder_path = os.path.join(project_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print(f"Subfolder '{folder}' created.")
    


# 4️⃣ Move files to correct folder
for filename in os.listdir():
    if os.path.isfile(filename):
        file_ext = os.path.splitext(filename)[1]
        for folder, exts in subfolders.items():
            if file_ext in exts:
                src_file = os.path.join(os.getcwd(), filename)
                dst_file = os.path.join(project_dir, folder, filename)
                shutil.move(src_file, dst_file)
                print(f"Moved '{filename}' to '{folder}' folder.")
                break

print("✅ File Organizer executed successfully.")