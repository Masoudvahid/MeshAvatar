import os

def remove_frame_prefix(folder_path):
    """Removes 'frame_' prefix from all files in the given folder and its subdirectories."""
    
    # Walk through all directories and files in the given folder
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            # Check if the file starts with 'frame_'
            new_filename = '000' + filename
            # Get the full file paths
            old_file_path = os.path.join(dirpath, filename)
            new_file_path = os.path.join(dirpath, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    # Specify the folder path where the files are located
    folder_path = '/home/mvahid/Avatar/sergey/cams'  # Replace this with your actual folder path
    
    # Call the function to remove the 'frame_' prefix
    remove_frame_prefix(folder_path)
