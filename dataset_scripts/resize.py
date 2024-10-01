import os
from PIL import Image

def resize_images(folder_path, new_size):
    """Resizes images in the folder and its subdirectories to the specified size."""
    
    # Walk through all directories and files in the given folder
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            # Check for common image file extensions
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                file_path = os.path.join(dirpath, filename)
                
                try:
                    with Image.open(file_path) as img:
                        # Resize the image
                        current_size = img.size  # (width, height)
                        # Check if the current size matches the desired size
                        if current_size != new_size:
                            resized_img = img.resize(new_size)
                            # Save the resized image, overwriting the original
                            resized_img.save(file_path)
                            print(f"Resized: {file_path} to {new_size}")
                except Exception as e:
                    print(f"Could not open or resize {file_path}: {e}")

if __name__ == "__main__":
    # Specify the folder path where the images are located
    folder_path = '/home/mvahid/Avatar/sergey/cams/'  # Replace this with your actual folder path
    # Specify the new size (width, height) for resizing
    new_size = (1409, 1920)  # Example size, adjust as needed
    
    # Call the function to resize images
    resize_images(folder_path, new_size)
