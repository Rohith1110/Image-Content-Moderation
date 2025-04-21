# Enhancing Image Captioning: 
# Content Moderation & ALT Text Generation

## 📌 Overview

This project is focused on enhancing automatic image captioning using a hybrid deep learning approach that combines **CNN (Xception)** for image feature extraction and **RNN (LSTM)** for natural language caption generation. In addition to captioning, the system performs **content moderation** by flagging potentially harmful text and supports **ALT text generation** for web accessibility.

This tool serves two core purposes:
- **Moderation**: Helps platforms detect unsafe or inappropriate content before it gets posted.
- **Accessibility**: Automatically generates meaningful ALT text for visually impaired users.

## 🚀 Key Features

- Upload any image and generate ALT Text
- Detect and flag harmful/inappropriate content
- Support for multilingual caption output (via Googletrans)
- Retrieve and display similar images using Google Image Search
- User-friendly GUI built with Tkinter (based on version)
- Uses pre-trained **Xception** model for robust feature extraction

## 🧠 Tech Stack

- **Python 3.8+**
- **TensorFlow / Keras**
- **Xception (Pre-trained CNN)**
- **LSTM (RNN) for language modeling**
- **Googletrans** for translation
- **OpenCV, PIL** for image handling
- **Tkinter** or **Streamlit** for GUI
- **Flickr8K Dataset**

## ✅ Example Usage

- Upload an image: 🖼️
- Get the caption: `"A child playing with a soccer ball"`
- If harmful: `"⚠️ Inappropriate content detected!"`
- ALT text: `"Child playing outdoor soccer"`

## 📌 Future Enhancements

- Integrate attention mechanism for better context
- Add video/audio captioning
- Enable real-time browser extension support

## 🙌 Acknowledgements

- Flickr8k Dataset
- Show and Tell: A Neural Image Caption Generator
- Camera2Caption (2018)
- WCAG Guidelines for Web Accessibility

## 👥 Contributors

- Rohith Kumar Chennareddy  
- Rithwik Vamshi  
(Team Project for CS521 - Spring 2025, University of Illinois Chicago)
