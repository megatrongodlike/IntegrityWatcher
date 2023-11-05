import hashlib
import os
import time

def calculate_file_hash(filepath):
    sha512 = hashlib.sha512()
    with open(filepath, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha512.update(data)
    return sha512.hexdigest()

def erase_baseline_if_already_exists():
    if os.path.exists('./baseline.txt'):
        os.remove('./baseline.txt')

print()
print("What would you like to do?")
print()
print("    A) Collect new Baseline?")
print("    B) Begin monitoring files with saved Baseline?")
print()
response = input("Please enter 'A' or 'B: ").upper()
print()

if response == "A":
    erase_baseline_if_already_exists()

    # Collect all files in the target folder
    files = [os.path.join('./Files', filename) for filename in os.listdir('./Files') if os.path.isfile(os.path.join('./Files', filename))]

    # For each file, calculate the hash, and write to baseline.txt
    with open('./baseline.txt', 'a') as baseline_file:
        for file_path in files:
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")

elif response == "B":
    file_hash_dictionary = {}

    # Load file|hash from baseline.txt and store them in a dictionary
    with open('./baseline.txt', 'r') as baseline_file:
        for line in baseline_file:
            file_path, file_hash = line.strip().split('|')
            file_hash_dictionary[file_path] = file_hash

    # Begin (continuously) monitoring files with the saved Baseline
    while True:
        time.sleep(1)

        files = [os.path.join('./Files', filename) for filename in os.listdir('./Files') if os.path.isfile(os.path.join('./Files', filename))]

        for file_path in files:
            file_hash = calculate_file_hash(file_path)

            # Notify if a new file has been created
            if file_path not in file_hash_dictionary:
                print(f"{file_path} has been created!")

            # Notify if a file has been changed
            elif file_hash_dictionary[file_path] != file_hash:
                print(f"{file_path} has changed!")

        # Check if any baseline files have been deleted
        for key in list(file_hash_dictionary.keys()):
            if not os.path.exists(key):
                print(f"{key} has been deleted!")
                del file_hash_dictionary[key]
                
for file_path in files:
    print(f"Processing file: {file_path}")
    file_hash = calculate_file_hash(file_path)
    print(f"Hash of {file_path}: {file_hash}")
               
