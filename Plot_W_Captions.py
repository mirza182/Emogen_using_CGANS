# Import the libraries
import os
from PIL import Image
import matplotlib.pyplot as plt

# Set the folder and file paths
folder_path = "D:/Emogen/coco2017/Train_Resizenew"
captions_file_path = "D:/Emogen/coco2017/Train_Resizenew/captions_new.txt"

# Create a dictionary that maps image ids to captions
image_id_to_caption = {}
with open(captions_file_path, "r") as f:
    for line in f:
        # Split the line by the colon
        parts = line.split(":")
        # Get the image id and the caption
        image_id = parts[0]
        caption = parts[1].strip()
        # Store the caption in the dictionary
        image_id_to_caption[image_id] = caption

# Get the list of image names
image_names = os.listdir(folder_path)

# Filter the list by the image file extension
image_names = [name for name in image_names if name.endswith((".jpg", ".png"))]

# Loop through the first 10 images
for i in range(10):
    # Get the image name and id
    image_name = image_names[i]
    image_id = image_name.split(".")[0]

    # Load and display the image
    image = Image.open(folder_path + "/" + image_name)
    plt.imshow(image)
    plt.axis("off")

    # Get and display the caption for the image
    caption = image_id_to_caption[image_id]
    plt.title(caption)
    plt.show()
