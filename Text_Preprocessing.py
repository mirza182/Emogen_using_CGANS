# ##SEQUENCE LENGTH FOR PADDING
# import numpy as np

# # Read the file
# with open('D:\\Emogen\\coco2017\\Train_Resizenew\\captions_new.txt', 'r') as f:
#     lines = f.readlines()

# # Split each line into words, treating punctuation as separate tokens
# num_words = [len(line.split()) - 1 for line in lines]  # Subtract 1 to exclude the image identifier

# # Calculate the 90th percentile of the 'num_words' list
# sequence_length = np.percentile(num_words, 90)

# print(f"The 90% length of the number of words in your captions is {sequence_length}")

# #TOKENIZATION
import re

# Path to your captions file
captions_path = 'D:\\Emogen\\coco2017\\Train_Resizenew\\captions_new.txt'

captions = {}
with open(captions_path, 'r', encoding='utf-8') as file:
    for line in file:
        key, caption = line.strip().split(':', 1)
        captions[key.strip()] = caption.strip().lower()

# Selectively keeping important punctuation (.,!?)
captions_cleaned = {key: re.sub(r'(?<!\d)[,!?](?!\d)', r' \g<0> ', caption) for key, caption in captions.items()}


# Basic example of treating punctuation as separate tokens
tokenized_captions = {key: re.findall(r'\w+|[,!?]', caption) for key, caption in captions_cleaned.items()}

num_examples_to_display = 5  # You can adjust this number as needed
for i, (key, tokens) in enumerate(tokenized_captions.items()):
    print(f"{key}: {tokens}")
    if i >= num_examples_to_display - 1:
        break


#FASTTEXT

#Loading the FastText Embeddings
from gensim.models import KeyedVectors

# Updated path to the .vec file
model_path = 'D:\\Emogen\\coco2017\\crawl-300d-2M.vec'

# Load the FastText embeddings
ft_model = KeyedVectors.load_word2vec_format(model_path, binary=False)

print("FastText model loaded successfully.")

#Vectorizing Your Tokenized Captions
import numpy as np

embedding_dim = 300  # Dimensionality of the FastText embeddings
vectorized_captions = {}

for key, tokens in tokenized_captions.items():
    embeddings = []
    for token in tokens:
        # Retrieve embedding if token is in vocabulary; otherwise, use a zero vector
        if token in ft_model.key_to_index:
            embedding = ft_model[token]
        else:
            embedding = np.zeros(embedding_dim)
        embeddings.append(embedding)
    vectorized_captions[key] = np.array(embeddings)

# Get the first key in the dictionary
first_key = list(vectorized_captions.keys())[0]

# Print the key and its corresponding vectorized caption
print(f"Key: {first_key}")
print(f"Vectorized Caption: {vectorized_captions[first_key]}")

print("Done!")

#Padding the Sequences

# Assuming sequence_length is calculated from your captions
sequence_length=14
padded_captions = {}

for key, embeddings in vectorized_captions.items():
    padding_length = max(0, int(sequence_length) - len(embeddings))
    if padding_length > 0:
        # Pad with zero vectors if the sequence is shorter than the desired length
        padded_embedding = np.vstack((embeddings, np.zeros((padding_length, embedding_dim))))
    else:
        # Or truncate the sequence if it's longer than the desired length
        padded_embedding = embeddings[:int(sequence_length)]
    padded_captions[key] = padded_embedding


#Saving the Preprocessed and Padded Sequences

import pickle

# Assuming `padded_captions` is your final preprocessed data
data_to_save = {
    'padded_captions': padded_captions,
    'sequence_length': sequence_length  # It's useful to save this as well
}

# Specify the file path where you want to save the preprocessed data
save_path = 'D:\\Emogen\\coco2017\\preprocessed_captions.pkl'

# Writing the preprocessed data to file
with open(save_path, 'wb') as handle:
    pickle.dump(data_to_save, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Preprocessed data saved successfully to {save_path}")
