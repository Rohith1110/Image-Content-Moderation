import tkinter as T
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog 
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse
import pyttsx3
import warnings
import webbrowser

window = Tk()
window.title("CS521 Project")
window.geometry("1000x600")
window.configure(bg="ivory2")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=4)
window.rowconfigure(2, weight=4)
window.rowconfigure(3, weight=1)
window.columnconfigure(1, weight=1)
warnings.filterwarnings('ignore')
from googletrans import Translator
translator = Translator()

banned_keywords = ['gun', 'knife', 'blood', 'nude', 'weapon', 'violence', 'fight', 'dead', 'kill']

def is_harmful_caption(text):
    for word in banned_keywords:
        if word in text.lower():
            return True
    return False

def extract_features(filename, model):
	try:
		image = Image.open(filename)
	except:
		print("ERROR: Couldn't open image! Make sure the image path and extension is correct")
	image = image.resize((299,299))
	image = np.array(image)
	if image.shape[2] == 4: 
		image = image[..., :3]
	image = np.expand_dims(image, axis=0)
	image = image/127.5
	image = image - 1.0
	feature = model.predict(image)
	return feature

def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None


def generate_desc(model, tokenizer, photo, max_length):
	in_text = 'start'
	for i in range(max_length):
		sequence = tokenizer.texts_to_sequences([in_text])[0]
		sequence = pad_sequences([sequence], maxlen=max_length)
		pred = model.predict([photo,sequence], verbose=0)
		pred = np.argmax(pred)
		word = word_for_id(pred, tokenizer)
		if word is None:
			break
		in_text += ' ' + word
		if word == 'end':
			break
	in_text = in_text.replace("start","")
	in_text = in_text.replace("end","")
	return in_text


def openfilename(): 
    root = T.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(initialdir="/Users/rithwikvamshi/Desktop/CS521\ code/Test\ inputs",
                           title = "Choose a file.")
    root.destroy() 
    return filename 

def open_img():
    x = openfilename()
    if x:
        img_path = x
        img = Image.open(x)
        img = img.resize((200, 200), Image.BILINEAR) 
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.grid(row=1, column=1, sticky="ns")
        max_length = 32
        tokenizer = load(open("tokenizer.p", "rb"))
        model = load_model('model_1.h5')
        xception_model = Xception(include_top=False, pooling="avg")
        photo = extract_features(img_path, xception_model)
        img = Image.open(img_path)
        global description
        description = generate_desc(model, tokenizer, photo, max_length)
        print(description)
		# to read the description out loud 
        # engine = pyttsx3.init(driverName='nsss')
        # engine.say(description)
        # engine.runAndWait()

def handle_caption_filtering(caption):
    for word in banned_keywords:
        if word in caption.lower():
            lbl3.config(fg="red")
            return "⚠️ Content flagged as inappropriate."
    lbl3.config(fg="green")
    return f"{caption}\n\n✔️ Caption is clean — no harmful content found."
	
def telugu_translate():
	trans = translator.translate(description, dest='te')
	text.set("")
	text.set(trans.text)

def tamil_translate():
	trans = translator.translate(description, dest='ta')
	text.set("")
	text.set(trans.text)
	
def english_print():
	fr_desc = T.Frame(window, bd=2,bg="mint cream")
	text.set("")
	filtered_text = handle_caption_filtering(description)
	text.set(filtered_text)

def open_images():
	
	url = "https://www.google.com/search?q="+description+"&tbm=isch"
	#webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    #webbrowser.get('chrome').open_new(url)
	webbrowser.open_new(url)


text = StringVar()
fr_desc = T.Frame(window, bd=2,bg="ivory2")
lbl3 = Label(fr_desc, textvariable=text,bg="ivory2", fg="gray25", font="oxygen 10 bold")
lbl3.grid(row=0, column=1,sticky="ew")
fr_desc.grid(row=2,column=1,sticky="ns")
	

#Buttons
fr_buttons = T.Frame(window,bd=2,bg="ivory2")
btn_choose = T.Button(fr_buttons, text="Choose Image", bg="salmon", command = open_img)
btn_english = T.Button(fr_buttons, text="English", bg="peach puff",command = english_print)
btn_telugu = T.Button(fr_buttons, text="Telugu", bg="peach puff",command = telugu_translate)
btn_tamil = T.Button(fr_buttons, text="Tamil", bg="peach puff",command = tamil_translate)
btn_open = T.Button(fr_buttons, text="Find Similar", bg="peach puff", command = open_images)


btn_choose.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_english.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_telugu.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_tamil.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_open.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=1, column=0, sticky="ns")

#Main Content
fr_main = T.Frame(window, bd=2,bg="peach puff")
lbl1 = Label(fr_main, text="Content Moderation & ALT Text Generator\nCS521 - Project", bg="peach puff", fg="black", font="none 16 italic")
lbl1.grid(row=0, column=1,sticky="ew")
fr_main.grid(row=0,column=1,sticky="ns")


#Footer
fr_foot = T.Frame(window, bd=2,bg="peach puff")
lbl2 = Label(fr_foot, text="Developed by\nRithwik Vamshi\nRohith Kumar",bg="peach puff", fg="gray25", font="oxygen 10 bold")
lbl2.grid(row=0, column=1,sticky="ew")

fr_foot.grid(row=3,column=1,sticky="ns")


window.mainloop()
