import os
import shutil

# Specify the source directory
source_directory = r'D:\Emogen\coco2017\Train'

# Specify the target directory for sorted images
target_directory = r'D:\Emogen\coco2017\Train_Sorted'

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Iterate through the range of image numbers
for i in range(1, 118828):  # Start from 1 and go up to 118827
    # Generate the source and target filenames
    source_filename = f'image_{i}.jpg'  # Assuming the images have PNG extension
    target_filename = f'image_{i:06d}.jpg'  # Padded with leading zeros

    source_path = os.path.join(source_directory, source_filename)
    target_path = os.path.join(target_directory, target_filename)

    # Check if the source file exists and move it to the target directory
    if os.path.exists(source_path):
        shutil.move(source_path, target_path)
        print(f'Moved {source_filename} to {target_filename}')
    else:
        print(f'Skipped {source_filename} (not found)')

print('Sorting completed.')