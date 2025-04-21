# Enhancing Image Captioning  
## Content Moderation & ALT Text Generation  

## Overview  

This project enhances automatic image captioning using a hybrid deep learning model that combines **CNN (Xception)** for image feature extraction and **RNN (LSTM)** for caption generation. It also integrates a lightweight **content moderation pipeline** to detect unsafe captions and supports **ALT text generation** to improve accessibility.

This system supports two real-world applications:  
- **Moderation**: Flagging unsafe or inappropriate content  
- **Accessibility**: Generating clean and descriptive ALT text automatically  


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

<div style="margin-left: 100px;">
  <img width="270" alt="image" src="https://github.com/user-attachments/assets/88b18127-8ecc-4531-93d7-00f5453a1564" />
</div>

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

## Dataset  

- This project uses the **Flickr8K** dataset for training.  
- Due to size constraints, the dataset is not included in the repository.  
- Precomputed features (`features.p`) and the model file (`model_1.h5`) are included separately.


## Installation Instructions (How to Run) 

To install the necessary dependencies, use the following commands:

**Step 1:**:
```
python = >=3.8

```
**Step 2:**:
```
tensorflow==2.12.0
keras==2.12.0
numpy
Pillow
```

**Step 3:**:
You can download the Flickr8K dataset from the following sources
```
  [Kaggle - Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)
  [GitHub - Flickr8k_Dataset.zip](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip)
```

**Step 4:**:
Train the model using `training_caption_generator.py`
```
python training_caption_generator.py
```

**Step 5:**:
Run the GUI using `gui.py`.
```
python gui.py
```

The GUI will automatically load the saved model and tokenizer, allowing you to generate captions, apply content filtering, and optionally translate or search the caption.
The input will be an image selected via the GUI, and the output will be either ALT text (caption) or a moderation alert if inappropriate content is detected.

## Future Work  

- Integrate BERT or transformer-based content moderation  
- Add attention mechanisms to improve caption quality  
- Extend support to video/audio captioning  
- Build a browser extension for real-time captioning and moderation  


## Contributors  

- **Rithwik Vamshi Athinarap**  
- **Rohith Kumar Chennareddy**  

CS521 – Spring 2025  
University of Illinois at Chicago  
