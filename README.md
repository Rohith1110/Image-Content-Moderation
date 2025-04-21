# Enhancing Image Captioning  
## Content Moderation & ALT Text Generation  

---

## Overview  

This project enhances automatic image captioning using a hybrid deep learning model that combines **CNN (Xception)** for image feature extraction and **RNN (LSTM)** for caption generation. It also integrates a lightweight **content moderation pipeline** to detect unsafe captions and supports **ALT text generation** to improve accessibility.

This system supports two real-world applications:  
- **Moderation**: Flagging unsafe or inappropriate content  
- **Accessibility**: Generating clean and descriptive ALT text automatically  

---

## Project Workflow  

### 1. Model Training  
- A cleaned version of the Flickr8K dataset is used.  
- Xception is used to extract image features.  
- An LSTM-based decoder is trained to generate captions.  
- The final model and tokenizer are saved for deployment.  

### 2. GUI Inference  
- A user-friendly GUI is developed using Tkinter.  
- Users can upload an image, generate captions, and run moderation checks.  
- Captions can also be translated to Tamil or Telugu, and similar images can be searched using Google.

---

## Key Features  

- Upload an image and get an automatic caption  
- Captions are moderated using a rule-based filter  
- Clean captions are shown in green and flagged ones in red  
- Captions can be translated to Tamil or Telugu  
- Option to search for similar images using the caption  

---

## Example Outputs  

### Clean Caption  
- **Generated**: `two boys are playing soccer`  
- ✅ Caption accepted and displayed as ALT text  

### Inappropriate Caption  
- **Generated**: `man holding knife`  
- ⚠️ Caption flagged as inappropriate  

---

## Dataset  

- This project uses the **Flickr8K** dataset for training.  
- Due to size constraints, the dataset is not included in the repository.  
- Precomputed features (`features.p`) and the model file (`model_1.h5`) are included separately.

---

## How to Run & Setup  

**Step 1:** Install Python 3.8 or later.  
**Step 2:** Download the Flickr8K dataset and precompute image features.  
**Step 3:** Train the model using `training_caption_generator.py`.  
**Step 4:** Run the GUI using `gui.py`.  
The GUI will load the saved model and tokenizer, and allow you to generate captions, apply content filtering, and translate or search the caption.

---

## Future Work  

- Integrate BERT or transformer-based content moderation  
- Add attention mechanisms to improve caption quality  
- Extend support to video/audio captioning  
- Build a browser extension for real-time captioning and moderation  

---

## Contributors  

- **Rithwik Vamshi Athinarap**  
- **Rohith Kumar Chennareddy**  

CS521 – Spring 2025  
University of Illinois at Chicago  
