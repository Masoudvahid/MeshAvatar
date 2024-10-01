import os
from PIL import Image

def check_image(image_path):
    """
    Attempts to open an image file to check if it's corrupted.
    If the image is corrupted, an IOError will be raised.
    """
    try:
        img = Image.open(image_path)
        img.verify()  # Verify that it's an image
        return True
    except (IOError, SyntaxError) as e:
        print(f"Corrupted image found: {image_path} - Error: {e}")
        return False

def check_images_in_directory(directory):
    """
    Recursively checks all images in the given directory for corruption.
    """
    corrupted_images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_path = os.path.join(root, file)
                if not check_image(image_path):
                    corrupted_images.append(image_path)
    
    if corrupted_images:
        print("\nList of corrupted images:")
        for image in corrupted_images:
            print(image)
    else:
        print("No corrupted images found.")

if __name__ == "__main__":
    directory = input("Enter the directory path to check for corrupted images: ")
    check_images_in_directory(directory)
