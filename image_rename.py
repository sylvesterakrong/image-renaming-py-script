import os

# path to image folder...replace folder name to path to your folder
folder_path = r"c:\Users\USER\OneDrive\Desktop\GalleryApp\gallery_app\lib\assets\images"

# this should get all files in the folder
files = os.listdir(folder_path)

# This would go through the files and rename them to the format you want
for i, file_name in enumerate(files):
    new_name = f"image{i+1}.jpg"  
    
    # this should replace the file name with the new format
    os.rename(
        os.path.join(
            folder_path, file_name
        ), os.path.join(
            folder_path, new_name
            )
        )
