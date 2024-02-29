import json
import os
from PIL import Image
import random

# Define the paths
captions_file_path = "D:/Emogen/coco2017/annotations/captions_train2017.json"
image_dir_path = "D:/Emogen/coco2017/train2017"
output_dir_path = "D:/Emogen/coco2017/Train"
output_captions_file_path = os.path.join(output_dir_path, "captions.txt")

# Load the captions from the JSON file
with open(captions_file_path, "r") as captions_file:
    captions_data = json.load(captions_file)

# Create a dictionary to map image IDs to captions
image_id_to_caption = {}
for annotation in captions_data["annotations"]:
    image_id = annotation["image_id"]
    caption = annotation["caption"]
    
    if image_id not in image_id_to_caption:
        image_id_to_caption[image_id] = []
    image_id_to_caption[image_id].append(caption)

# Get the list of image paths
image_paths = os.listdir(image_dir_path)

# Create the output directory if it doesn't exist
os.makedirs(output_dir_path, exist_ok=True)

# Open the captions file for writing
with open(output_captions_file_path, "w") as captions_output_file:
    # Loop through all images
    for i, image_path in enumerate(image_paths):
        # Get the image ID
        image_id = int(image_path.split(".")[0])

        # Load the image
        image_file_path = os.path.join(image_dir_path, image_path)
        image = Image.open(image_file_path)

        # Save the image in the output directory
        output_image_path = os.path.join(output_dir_path, f"image_{i + 1}.jpg")
        image.save(output_image_path)

        # Get and write one random caption for the image
        random_caption = random.choice(image_id_to_caption[image_id])
        captions_output_file.write(f"Image {i + 1} Caption: {random_caption}\n")

print("Images and captions saved successfully.")



