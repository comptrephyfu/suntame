# Checking if a specific hash is valid
hash_to_check = 'hash1'
if hash_to_check in old_hashes_valid:
    is_valid = old_hashes_valid[hash_to_check]
    print(f"Hash {hash_to_check} is valid: {is_valid}")
else:
    print(f"Hash {hash_to_check} not found in the dictionary.")
