import json

# Load the JSON data
with open('/home/masoud1/Documents/Avatar/avatarex/calibration_full.json', 'r') as file:
    data = json.load(file)

# Iterate over each camera's calibration data
for camera_id, calibration in data.items():
    K = calibration['K']
    imgsz = calibration['imgSize']
    
    # Scale the first two elements of K
    # K[0] /= 2  # f_x
    # K[4] /= 2  # f_y
    # K[2] /= 2  # c_x
    # K[5] /= 2  # c_y

    imgsz[0] *= 2
    imgsz[1] *= 2
    imgsz[0] = int(imgsz[0])
    imgsz[1] = int(imgsz[1])
    
    # Update the K matrix
    calibration['K'] = K
    calibration['imgSize'] = imgsz

# Save the modified JSON data back to the file
with open('/home/masoud1/Documents/Avatar/avatarex/calibration_full_modified.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Intrinsic matrices modified and saved to 'calibration_full_modified.json'.")
