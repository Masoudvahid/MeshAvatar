import json
import os
import yaml

def read_yaml(yaml_file):
    """Reads a YAML file and returns the data as a dictionary."""
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def construct_calibration(intrinsics, extrinsics):
    """Constructs calibration data for all cameras present in the intrinsic and extrinsic files."""
    calibration = {}
    
    # Extract camera names by finding keys that match 'K_cam_*'
    camera_names = [key.split('_')[1] for key in intrinsics if key.startswith('K_cam')]
    
    # Loop over all camera names and construct calibration dictionaries
    for camera_name in camera_names:
        # Intrinsic Parameters (K matrix and distortion coefficients)
        K = intrinsics[f'K_cam_{camera_name}']['data']
        distCoeff = intrinsics[f'dist_cam_{camera_name}']['data']
        
        # Extrinsic Parameters (Rotation matrix R and translation vector T)
        R = extrinsics[f'Rot_cam_{camera_name}']['data']
        T = extrinsics[f'T_cam_{camera_name}']['data']
        
        # Construct the calibration dictionary for each camera
        calibration[f'cam_{camera_name}'] = {
            "K": K,
            "R": R,
            "T": T,
            "distCoeff": distCoeff,
            "imgSize": [1920, 1080],  # Placeholder values, adjust as necessary
            "rectifyAlpha": 0.0
        }
    
    return calibration

def save_calibration_as_json(calibration, output_file):
    """Saves the calibration dictionary as a JSON file."""
    with open(output_file, 'w') as file:
        json.dump(calibration, file, indent=4)

if __name__ == "__main__":
    # Paths to your YAML files
    intrinsics_file = '/home/mvahid/Avatar/sergey/intri.yml'
    extrinsics_file = '/home/mvahid/Avatar/sergey/extri.yml'
    
    # Output calibration file path
    output_file = '/home/mvahid/Avatar/sergey/calibration_full.json'
    
    # Read the intrinsic and extrinsic parameters from YAML files
    intrinsics = read_yaml(intrinsics_file)
    extrinsics = read_yaml(extrinsics_file)
    
    # Construct the calibration dictionary for all cameras
    calibration = construct_calibration(intrinsics, extrinsics)
    
    # Save the calibration to a JSON file
    save_calibration_as_json(calibration, output_file)
    
    print(f"Calibration file saved to {output_file}")
