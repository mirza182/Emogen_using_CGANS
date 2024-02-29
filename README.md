# "Emogen": Text-to-Image Generation using CGANs
This repository contains my final year project, which focuses on generating images from textual descriptions using Conditional Generative Adversarial Networks (CGANs).

# Project Overview
The goal of this project is to build a model that can generate images based on textual descriptions. This is achieved by training a CGAN on a dataset of images and their corresponding textual descriptions.

# The project involves several key steps:

# Data Preparation: 
The first step in any machine learning project is preparing the data. This involves extracting the image and text data and ensuring it’s in a format that can be used to train the model.
# Text Preprocessing: 
The text data is preprocessed to ensure consistency and improve the model’s performance. This includes lowercasing all text, selectively cleaning punctuation, and tokenizing the text.
# Vectorization: 
The tokenized text is then converted into numerical vectors that can be used as input to the model. This project uses FastText pre-trained embeddings for vectorization.
# Model Training: 
The CGAN model is trained on the prepared data. The model learns to generate images that correspond to the provided textual descriptions.
# Image Generation: 
Once the model is trained, it can be used to generate images from textual descriptions.
Installation and Usage
To run the notebooks, you need to have Python and Jupyter installed on your machine. You can install them using Anaconda.

After cloning the repository, navigate to the repository’s directory and start Jupyter by running jupyter notebook in your terminal. This will open a new tab in your web browser where you can open and run the notebooks.

# Contributing
As this is a final year project, contributions will not be accepted. However, feel free to explore the code and use it for your own projects.

