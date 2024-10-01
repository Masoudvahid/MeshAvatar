import os
from PIL import Image

def check_image_dimensions(folder_path):
    """Checks if all images in the folder and its subdirectories have the same dimensions."""
    
    # Walk through all directories and files in the given folder
    for dirpath, _, filenames in os.walk(folder_path):
        dimensions = set()  # To store unique dimensions
        
        for filename in filenames:
            # Check for common image file extensions
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                file_path = os.path.join(dirpath, filename)
                
                try:
                    with Image.open(file_path) as img:
                        # Get image dimensions
                        dim = img.size  # (width, height)
                        dimensions.add(dim)
                except Exception as e:
                    print(f"Could not open {file_path}: {e}")
        
        # Check if all dimensions are the same
        if len(dimensions) == 1:
            # All images have the same dimensions
            common_dim = dimensions.pop()
            print(f"All images in '{dirpath}' have the same dimensions: {common_dim}")
        elif dimensions:
            # Images have different dimensions
            print(f"Images in '{dirpath}' have different dimensions: {dimensions}")
        else:
            print(f"No images found in '{dirpath}'.")

if __name__ == "__main__":
    # Specify the folder path where the image directories are located
    folder_path = '/home/mvahid/Avatar/sergey/cams'  # Replace this with your actual folder path
    
    # Call the function to check image dimensions
    check_image_dimensions(folder_path)
