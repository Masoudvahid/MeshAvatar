import os

def organize_images_by_camera_symlink(input_folder, output_folder, masks_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through each frame folder
    for frame_folder in sorted(os.listdir(input_folder)):
        frame_path = os.path.join(input_folder, frame_folder)
        
        if os.path.isdir(frame_path):  # Check if it's a directory
            # Loop through each image in the frame folder
            for image_file in os.listdir(frame_path):
                if image_file.endswith('.jpg'):
                    # Extract the camera name from the image file (e.g., 'cam_005.jpg')
                    cam_name = image_file.split('.')[0]
                    cam_folder = os.path.join(output_folder, cam_name)
                    
                    # Create the camera folder if it doesn't exist
                    if not os.path.exists(cam_folder):
                        os.makedirs(cam_folder)
                    
                    # Define the new symlink path in the camera folder
                    new_image_name = f"{frame_folder}.jpg"
                    new_image_path = os.path.join(cam_folder, new_image_name)
                    
                    # Define the new symlink path in the masks
                    mask_name = f"{frame_folder}.png"
                    original_mask_path = os.path.join(masks_folder, cam_name, mask_name)
                    if not os.path.exists(os.path.join(output_folder, 'mask')):
                        os.makedirs(os.path.join(output_folder, cam_folder, 'mask'), exist_ok=True)
                        os.makedirs(os.path.join(output_folder, cam_folder, 'mask', 'pha'), exist_ok=True)

                    new_mask_path = os.path.join(cam_folder,'mask', 'pha', mask_name)

                    # Create a symbolic link instead of copying the file
                    original_image_path = os.path.join(frame_path, image_file)
                    if not os.path.exists(new_image_path):  # Check if symlink doesn't already exist
                        os.symlink(original_image_path, new_image_path)
                        os.symlink(original_mask_path, new_mask_path)

if __name__ == "__main__":
    input_folder = "/home/mvahid/Avatar/sergey/jpg_resized"
    output_folder = "/home/mvahid/Avatar/sergey/cams"
    masks_folder = "/home/mvahid/Avatar/sergey/masks/track"
    organize_images_by_camera_symlink(input_folder, output_folder, masks_folder)
