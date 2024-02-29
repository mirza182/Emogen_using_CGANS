# # Define the path to the original captions file and the new file
# original_file_path = 'D:/Emogen/coco2017/Train_Sorted/Captions.txt'
# new_file_path = 'D:/Emogen/coco2017/Train_Sorted/Captions_new.txt'

# # Open the original file and read the lines
# with open(original_file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# # Filter out any empty lines (including lines that only contain whitespace)
# filtered_lines = [line for line in lines if line.strip()]

# # Write the filtered lines to the new file
# with open(new_file_path, 'w', encoding='utf-8') as new_file:
#     new_file.writelines(filtered_lines)

# print("Empty lines removed and new file saved as 'Captions_new.txt'.")



import shutil

# Paths configuration
captions_file_path = 'D:/Emogen/coco2017/Train_Sorted/captions_new.txt'
images_source_dir = 'D:/Emogen/coco2017/Train_Sorted'
images_destination_dir = 'D:/Lab'
new_captions_file_path = 'D:/Lab/new_captions.txt'

# Extract and save the last 10 captions
with open(captions_file_path, 'r', encoding='utf-8') as captions_file:
    all_captions = captions_file.readlines()

last_10_captions = all_captions[-10:]

with open(new_captions_file_path, 'w', encoding='utf-8') as new_captions_file:
    for caption in last_10_captions:
        new_captions_file.write(caption)

# Copy the corresponding images to the new location
for caption in last_10_captions:
    # Extract the image filename directly from the caption
    image_id_with_colon = caption.split(':')[0]  # This gets us 'image_XXXXXX'
    image_filename = f'{image_id_with_colon}.jpg'  # Adjusted for the correct file extension

    src = f'{images_source_dir}/{image_filename}'
    dst = f'{images_destination_dir}/{image_filename}'

    try:
        shutil.copy(src, dst)
        print(f"Image '{image_filename}' copied successfully.")
    except FileNotFoundError:
        print(f"File not found: {src}")

print("The last 10 images and their captions have been successfully processed.")


#DOTLINE PROBLEM
# import traceback

# # Open the original file for reading
# with open("D:/Emogen/coco2017/Train_Sorted/captions.txt", "r") as f:
#     # Open a new file for writing
#     with open("D:/Lab/captions_new.txt", "w") as g:
#         # Loop through each line in the original file
#         for i, line in enumerate(f):
#             # Check if the line is not empty
#             if line.strip():
#                 # Check if the line has a colon
#                 if ":" in line:
#                     # Split the line by the colon
#                     parts = line.split(":")
#                     try:
#                         # Get the caption part
#                         caption = parts[1]
#                         # Format the new prefix with leading zeros
#                         prefix = f"image_{i+1:06d}"
#                         # Write the new line to the new file
#                         g.write(prefix + ":" + caption)
#                     except IndexError:
#                         # Print the line number and the traceback information
#                         print(f"Line {i+1}:")
#                         traceback.print_exc()
#                 else:
#                     # Skip the invalid line
#                     print("Invalid line: " + line)

# # Close the files
# f.close()
# g.close()
