# from PIL import Image
# import os

# # Specify the source directory with the original images
# source_directory = r'D:\Emogen\coco2017\Train_Sorted'

# # Specify the target directory to save the resized images
# target_directory = r'D:\Emogen\coco2017\Train_Resized'

# # Create the target directory if it doesn't exist
# if not os.path.exists(target_directory):
#     os.makedirs(target_directory)

# # List all files in the source directory
# files = os.listdir(source_directory)

# # Filter only image files (e.g., PNG, JPG, JPEG, BMP)
# image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# # Sort the image files in ascending order
# image_files.sort()

# # Resize and save all the images
# for file in image_files:
#     source_path = os.path.join(source_directory, file)
#     target_path = os.path.join(target_directory, file)

#     try:
#         # Open the image file
#         with Image.open(source_path) as img:
#             # Resize the image to 256x256 pixels
#             img = img.resize((256, 256), Image.LANCZOS)
#             # Save the resized image in PNG format
#             img.save(target_path, 'PNG')
#             print(f'Resized and saved: {file}')
#     except Exception as e:
#         print(f'Error processing {file}: {e}')

# print('Resizing and saving completed for all images.')

from PIL import Image
import os

# Specify the source and target directories
source_directory = r'D:\Emogen\coco2017\Train_Sorted'
target_directory = r'D:\Emogen\coco2017\Train_Resizenew'

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# List all files in the source directory
files = os.listdir(source_directory)
# Filter only image files (e.g., PNG, JPG, JPEG, BMP)
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Resize and save all the images in JPG format
for file in image_files:
    source_path = os.path.join(source_directory, file)
    # Change extension to .jpg for the target path
    target_path = os.path.join(target_directory, os.path.splitext(file)[0] + '.jpg')

    try:
        with Image.open(source_path) as img:
            # Resize the image to 256x256 pixels
            img_resized = img.resize((256, 256), Image.LANCZOS)
            # Save the resized image in JPG format with the highest quality setting
            img_resized.save(target_path, 'JPEG', quality=100)
            print(f'Resized and saved: {file} as JPG')
    except Exception as e:
        print(f'Error processing {file}: {e}')

print('Resizing and saving of all images completed.')
