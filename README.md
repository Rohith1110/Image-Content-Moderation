# Enhancing Image Captioning  
# Content Moderation & ALT Text Generation  

## Overview  

This project enhances automatic image captioning using a hybrid deep learning model that combines **CNN (Xception)** for image feature extraction and **RNN (LSTM)** for caption generation. The system also supports **content moderation** by scanning generated captions for harmful or inappropriate text and **ALT text generation** to improve accessibility for visually impaired users.

This tool serves two core purposes:  
- **Moderation**: Detect and flag unsafe or sensitive image captions  
- **Accessibility**: Generate clean, descriptive ALT text automatically  

## Project Workflow  

### 1. Model Training (`training_caption_generator.py`)  
- Loads cleaned Flickr8K captions and image features  
- Uses a pre-trained **Xception** model to extract embeddings  
- Trains an LSTM model to generate captions based on extracted features  
- Saves:
  - `model_1.h5` – trained caption generator  
  - `tokenizer.p` – tokenizer used to preprocess text  

### 2. GUI Inference (`gui.py`)  
- Built with **Tkinter**  
- Allows users to:  
  - Upload an image  
  - Generate a caption using the trained model  
  - Filter harmful content using a rule-based filter  
  - Translate the caption to Tamil or Telugu  
  - Search similar images via Google Image Search  

## Key Features  

- Upload image and generate caption in real-time  
- Harmful content detection using a keyword-based filter  
- ALT text output suitable for accessibility use cases  
- Supports caption translation (English, Tamil, Telugu)  
- Search similar images using the generated caption  

## Example Outputs  

### Example 1 – Clean Caption  
- **Input**: An image of kids on a soccer field  
- **Generated**: `two boys are playing soccer`  
- **Result**: ✅ Caption accepted and used as ALT text  

### Example 2 – Inappropriate Caption  
- **Input**: Image simulating a violent scene  
- **Generated**: `man holding knife`  
- **Result**: ⚠️ Caption flagged as inappropriate  

> The filtering system uses a basic list of harmful terms for now. Future work may integrate smarter filters like **BERT** for better context handling.

## Dataset  

- **Flickr8K** was used for training  
- Due to size limitations, the dataset is **not included in this repository** but it contains the precomputed features (`features.p`)

## Tech Stack  

- Python 3.8+  
- TensorFlow / Keras  
- Xception (CNN encoder)  
- LSTM (caption decoder)  
- Googletrans (for translation)  
- Tkinter (GUI)  
- PIL, OpenCV (Image handling)  

## Future Work  

- Add attention mechanism for richer caption generation  
- Replace keyword filter with transformer-based content detection (e.g., BERT)  
- Extend support to video/audio captioning  
- Build a browser extension for real-time captioning and moderation  

## Contributors  

- **Rithwik Vamshi Athianrap**  
- **Rohith Kumar Chennareddy**  

CS521 – Spring 2025  
University of Illinois at Chicago  


