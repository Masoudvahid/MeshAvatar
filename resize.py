import os
import torch
from torchvision import transforms
from PIL import Image

def resize_image_gpu(image_path, output_path, size):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load image
    img = Image.open(image_path).convert("RGB")

    # Define the resize transform
    resize_transform = transforms.Compose([
        transforms.Resize(size, interpolation=Image.LANCZOS),
        transforms.ToTensor()
    ])

    # Apply the transform and move to GPU
    img_tensor = resize_transform(img).to(device)

    # Move back to CPU and convert to PIL Image
    img_tensor = img_tensor.cpu()
    img_pil = transforms.ToPILImage()(img_tensor)

    # Save the resized image
    img_pil.save(output_path)

def resize_images_in_directory(directory, size):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                output_path = image_path  # Overwrite the original image
                resize_image_gpu(image_path, output_path, size)
                print(f"Resized {image_path} to {size}")

if __name__ == "__main__":
    base_directory = "/home/masoud1/Documents/Avatar/avatarex"
    target_size = (1024, 750)
    resize_images_in_directory(base_directory, target_size)
