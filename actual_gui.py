from tkinter import *
import pickle
import tensorflow as tf
# from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing.text import Tokenizer

print(tf.__version__)
model = tf.keras.models.load_model("model.h5")
tokenizer = pickle.load(open('tokenizer.pkl','rb'))
# model.summary()

root=Tk()
root.title('Sentiment Analysis')
txt="""***********Welcome to the sentiment analysis application***********

We provide you with two options here. 

Option 1 : You can either enter a statement and we will guess if the statement is positive or negative.

Option 2 : You can provide the path of a file and we will analyze the number of positive and negative statements.
"""
info=Label(root,text=txt)
info.pack()

e1=Entry(root)
e1.pack()
e1.insert(0,"Enter your choice")

def single(statement,top1):
	s="The statment entered is \" "+statement+" \" "
	ls=Label(top1,text=s)
	ls.pack()
	return

def single(path,top2):
	s="The statement entered is \" "+path+" \" "
	ls=Label(top2,text=s)
	ls.pack()
	return

def predict_result(ee1):
	li = []
	li.append(ee1.get())
	val = tokenizer.texts_to_sequences(li)
	predicted_val = model.predict(val)
	print(predicted_val)
	if predicted_val > 0.3:
		output_text = "Positive :))"
	else:
		output_text = "Negative :("
	return output_text

def submit():
	c=e1.get()
	c=int(c)
	if(c==1):
		top1=Toplevel()
		l1=Label(top1,text="You selected option "+str(c))
		l1.pack()
		ee1=Entry(top1)
		ee1.pack()
		bb1=Button(top1,text="Submit Statement",command= lambda: single(predict_result(ee1),top1))
		bb1.pack()


	elif(c==2):
		top2=Toplevel()
		l1=Label(top2,text="You selected option "+str(c))
		l1.pack()
		ee2=Entry(top2)
		ee2.pack()
		ee2.insert(0,"Enter the path of the file ")
		bb2=Button(top2,text="Submit Path",command= lambda: dataset(output_text,top2))
		bb2.pack()

	else:
		e1.delete(0,END)
		e1.insert(0,"Enter your choice")


b1=Button(root,text="Submit Choice",command=submit)
b1.pack()

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