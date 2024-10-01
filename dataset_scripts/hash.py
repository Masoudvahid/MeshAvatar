import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        hash_object = hashlib.sha256(file_content)
        return hash_object.hexdigest()

file1_path = 'smpl_params.npz'
file1_path = 'SMPLX_NEUTRAL2.npz'
file2_path = '../sibur_db/smpl_params.npz'

hash1 = calculate_hash(file1_path)
hash2 = calculate_hash(file2_path)
print(f'Hash of file1: {hash1}')
print(f'Hash of file2: {hash2}')