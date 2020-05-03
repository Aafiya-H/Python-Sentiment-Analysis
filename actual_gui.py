from tkinter import *
from tkinter import filedialog
import pickle
import tensorflow as tf
# from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing.text import Tokenizer
import tkinter.font as font
from PIL import ImageTk, Image

print(tf.__version__)
model = tf.keras.models.load_model("model.h5")
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
# model.summary()
root = Tk()
root.configure(background="#85eaed")
root.title('Sentiment Analysis')
root.iconbitmap("LOGO.ico")

txt = "Welcome to the Sentiment Analysis application"
img = ImageTk.PhotoImage(Image.open("LOGO_cropped.png"))
s = """We provide you with two options here. 

Option 1 : You can either enter a statement and we will guess if the statement is positive or negative.

Option 2 : You can provide the path of a file and we will analyze the number of positive and negative statements.
"""
intro_font = font.Font(family='Helvetica', size=25, weight='bold', slant='italic', underline='1')
intro = Label(root, text=txt, fg="#FFFFFF", height="3", bg="#072d2e")
intro['font'] = intro_font
intro.pack(fill=X)

img_label = Label(root, image=img, bg='#420de0')  # '#420de0'
img_label.pack(fill=X)

info_font = font.Font(size=18, family='Helvetica')
info = Label(root, text=s, bg='#85eaed', fg='#0a0a0a')
info['font'] = info_font
info.pack(fill=X)
s1 = Label(root, text='\n', bg='#85eaed')
s1.pack(fill=X)
e1 = Entry(root, border=2)
e1.pack()
e1.insert(0, "Enter your choice")


def single(statement, top1):
    s = "\"" + statement + " \""
    ls = Label(top1, text=s, bg="#85eaed")
    ls['font'] = info_font
    ls.pack()
    return


def get_path():
    top2.filename = filedialog.askopenfile(initialdir='C:\\Users\\Aafiya Hussain\\Desktop\\GUI\\New GUI\\Python-Sentiment-Analysis', title='Select file',filetypes=[("image files",'*.png')])
    print(top2.filename)


# def single(path,top2):
# 	s="The statement entered is \" "+path+" \" "
# 	ls=Label(top2,text=s)
# 	ls.pack()
# 	return

def predict_result(ee1):
    li = []
    li.append(ee1.get())
    val = tokenizer.texts_to_sequences(li)
    predicted_val = model.predict(val)
    print(predicted_val)
    if predicted_val > 0.3:
        output_text = "Positivity always wins…Always"
    else:
        output_text = "Negativity will tear you down. Be more positive"
    return output_text


def submit():
    c = e1.get()
    c = int(c)
    if (c == 1):
        top1 = Toplevel()
        top1.configure(background="#85eaed")
        top1.iconbitmap("LOGO.ico")
        s2 = Label(top1, text='\n', bg="#85eaed")
        s2.pack(fill=X)
        l1 = Label(top1, text="You selected option " + str(c), bg="#85eaed", fg="#072d2e")
        l1['font'] = font.Font(family='Helvetica', size=20, weight='bold')
        l1.pack()

        lspace1 = Label(top1, text='\n', bg="#85eaed")
        lspace1.pack(fill=X)

        ee1 = Entry(top1, border=2)
        ee1.insert(0, 'Enter your statement')
        ee1.pack(fill=X)
        lspace2 = Label(top1, text='\n', bg="#85eaed")
        lspace2.pack(fill=X)
        bb1 = Button(top1, text="Submit for testing", command=lambda: single(predict_result(ee1), top1))
        bb1.pack()

        lspace3 = Label(top1, text='\n', bg="#85eaed")
        lspace3.pack(fill=X)
        exit = Button(top1, text="Exit", command=top1.quit)
        exit.pack()

    elif (c == 2):
        
        global top2
        top2 = Toplevel()
        top2.iconbitmap("LOGO.ico")
        top2.configure(background="#85eaed")
        s2 = Label(top2, text='\n', bg="#85eaed")
        s2.pack(fill=X)
        l1 = Label(top2, text="You selected option " + str(c), bg="#85eaed", fg="#072d2e")
        l1['font'] = font.Font(family='Helvetica', size=20, weight='bold')
        l1.pack()

        lspace1 = Label(top2, text='\n', bg="#85eaed")
        lspace1.pack(fill=X)

        upload = Label(top2, text="Upload file", bg="#85eaed")
        upload['font'] = info_font
        upload.pack()
        l_space = Label(top2, text='\n', bg="#85eaed")
        l_space.pack()
        # code for uploading
        open_file = Button(top2, text='Open file', command=get_path).pack()

        l_space1 = Label(top2, text='\n', bg="#85eaed")
        l_space1.pack()

        bb2 = Button(top2, text="Submit for testing", command=lambda: dataset(output_text, top2))
        bb2.pack()
        l_space2 = Label(top2, text='\n', bg="#85eaed")
        l_space2.pack()
        exit = Button(top2, text="Exit", command=top1.quit)
        exit.pack()

    else:
        e1.delete(0, END)
        e1.insert(0, "Enter your choice")


s2 = Label(root, text="\n", bg='#85eaed')
s2.pack(fill=X)

b1 = Button(root, text="Submit Choice", command=submit)
b1.pack()

l = Label(root, text='\n', bg='#85eaed')
l.pack(fill=X)

exit = Button(root, text="Exit", command=root.quit)
exit.pack()

root.mainloop()
#######################################
'''

val = tokenizer.texts_to_sequences(val)
predicted_val = model.predict(val)
print(np.squeeze(predicted_val))
if predicted_val > 0.5 :
    print("Positive :))")
else:
    print("Negative :(")

'''
