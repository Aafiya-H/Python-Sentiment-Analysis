from tkinter import *
from tkinter import filedialog,ttk
import pickle
import numpy as np
import tkinter.font as font
from PIL import ImageTk, Image
from fastai import *
from fastai.text import *
import torch
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.configure(background="#85eaed")
root.title('Sentiment Analysis')
root.iconbitmap("Images\\LOGO.ico")
count_single=0
def nothing(event):
	pass

txt = "Welcome to the Sentiment Analysis application"
img = ImageTk.PhotoImage(Image.open("Images\\LOGO_cropped.png"))
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
# e1 = Entry(root, border=2)
# e1.pack()
# e1.insert(0, "Enter your choice")
opts=['Option 1','Option 2']
e1=StringVar()
e1.set(opts[0])

drop=OptionMenu(root,e1,*opts)
drop.pack(pady=20)

dataset_path = ''

def single(statement, my_frame2):
    s = "\"" + statement + " \""
    ls = Label(my_frame2, text=s, bg="#85eaed")
    ls['font'] = info_font
    ls.pack()
    l_space2 = Label(my_frame2, text='\n', bg="#85eaed")
    l_space2.pack(fill=X)
    # img_single=ImageTk.PhotoImage(Image.open("Images\\pie_chart_single.png"))
    # canvas=Canvas(my_frame2,width=300,height=300)
    # canvas.pack()
    path_single="./Images/pie_chart_single"+str(count_single)+".png"
    img_single=ImageTk.PhotoImage(Image.open(path_single))
    # canvas.create_image(20,20, anchor=NW, image=img_single)  
    img_label = Label(my_frame2, image=img_single, bg='#420de0')  # '#420de0'
    img_label.image=img_single
    img_label.pack(fill=X)
    return


def get_path():
    global dataset_path
    top2.filename = filedialog.askopenfile(initialdir='./', title='Select file',filetypes=[("All files",'*.*')])
    print(top2.filename.name)
    dataset_path = top2.filename.name


def predict_result(ee1):
    input_s=ee1.get()
    loaded_model=load_learner('./',"ulmfit_model.pkl")
    predicted_val=loaded_model.predict(input_s)
    print("Statement is: ",input_s,end= ' ')
    print(str(predicted_val[0]))
    negative_percentage = predicted_val[2].tolist()[0]
    positive_percentage = predicted_val[2].tolist()[1]

    print(positive_percentage)
    print(negative_percentage)
    if str(predicted_val[0])=='positive':
        output_text = "Positivity always wins…Always :D :) ^.^"
    else:
        output_text = "Negative :/ :("
    sizes=[negative_percentage,positive_percentage]
    labels=['negative','positive']
    # plt.figure.suptitle('This is a somewhat long figure title', fontsize=16)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Pie chart to show percentage of positive and negative Sentiment for :\n'+input_s)
    global count_single
    count_single+=1
    path_single="./Images/pie_chart_single"+str(count_single)+".png"
    plt.savefig (path_single)
    plt.show()
    return output_text

def dataset_predict(dataset_path,my_frame2): 
    loaded_model=load_learner('./',"ulmfit_model.pkl")
    reviews = pd.read_csv(dataset_path)
    predictions = []
    positive=[]
    plt.title('Bar graph to show percentage of positive and negative sentiment for each statement')
    for index,row in reviews.iterrows():
        current_review = row['Reviews']
        predicted_value = loaded_model.predict(current_review)
        positive.append(predicted_value[2].tolist()[1])
        predictions.append(str(predicted_value[0]))

    positive=np.array(positive)
    negative=1-positive
    ids=range(len(positive))
    plt.bar(ids,positive,bottom=0,color='#17e80c')
    plt.bar(ids,negative,bottom = positive,color='#a30a0a')

    plt.xlabel('Statements')
    plt.ylabel('Positive and Negative percentage')
    plt.legend(('Positive', 'Negative'))
    # plt.show()
    plt.savefig ( "./Images/bar_graph_dataset.png" )
    reviews['Predictions'] = predictions
    reviews.to_csv(dataset_path,index=False)

    img_dataset=ImageTk.PhotoImage(Image.open("./Images/bar_graph_dataset.png"))
    # canvas.create_image(20,20, anchor=NW, image=img_single)  
    img_label = Label(my_frame2, image=img_dataset, bg='#420de0')  # '#420de0'
    img_label.image=img_dataset
    img_label.pack(fill=X)
    # print("Done :D :D ")


def submit():
    c = e1.get()
    if (c == 'Option 1'):
        top1 = Toplevel()
        top1.title('Single')
        top1.iconbitmap("Images\\LOGO.ico")
        my_notebook=ttk.Notebook(top1)
        # my_notebook.pack(pady=15)
        my_frame1=ttk.Frame(my_notebook,width=500,height=500)
        my_frame2=ttk.Frame(my_notebook,width=500,height=500)#,bg='#85eaed'
        my_notebook.add(my_frame1,text="Statement")
        my_notebook.add(my_frame2,text="Result")
        my_notebook.pack(pady=15)
        # top1.configure(background="#85eaed")
        
        s2 = Label(my_frame1, text='\n', bg="#85eaed")
        s2.pack(fill=X)
        l1 = Label(my_frame1, text="You selected " + str(c), bg="#85eaed", fg="#072d2e")
        l1['font'] = font.Font(family='Helvetica', size=20, weight='bold')
        l1.pack(fill=X)

        lspace1 = Label(my_frame1, text='\n', bg="#85eaed")
        lspace1.pack(fill=X)

        ee1 = Entry(my_frame1, border=2)
        ee1.insert(0, 'Enter your statement')
        ee1.pack(fill=X)
        lspace2 = Label(my_frame1, text='\n', bg="#85eaed")
        lspace2.pack(fill=X)
        bb1 = Button(my_frame1, text="Submit for testing", command=lambda: single(predict_result(ee1), my_frame2))
        bb1.pack()

        lspace3 = Label(my_frame1, text='\n', bg="#85eaed")
        lspace3.pack(fill=X)

        exit = Button(top1, text="Exit", command=top1.quit)
        exit.pack()
        # top1.mainloop()

    elif (c == 'Option 2'):
        
        global top2
        top2 = Toplevel()
        top2.iconbitmap("Images\\LOGO.ico")
        my_notebook=ttk.Notebook(top2)
        my_frame1=ttk.Frame(my_notebook,width=500,height=500)
        my_frame2=ttk.Frame(my_notebook,width=500,height=500)#,bg='#85eaed'
        my_notebook.add(my_frame1,text="Upload")
        my_notebook.add(my_frame2,text="Result")
        my_notebook.pack(pady=15)
        s2 = Label(top2, text='\n', bg="#85eaed")
        s2.pack(fill=X)
        l1 = Label(my_frame1, text="You selected " + str(c), bg="#85eaed", fg="#072d2e")
        l1['font'] = font.Font(family='Helvetica', size=20, weight='bold')
        l1.pack()

        lspace1 = Label(my_frame1, text='\n', bg="#85eaed")
        lspace1.pack(fill=X)

        upload = Label(my_frame1, text="Upload file", bg="#85eaed")
        upload['font'] = info_font
        upload.pack()
        l_space = Label(my_frame1, text='\n', bg="#85eaed")
        l_space.pack()
        
        open_file = Button(my_frame1, text='Open file', command=get_path).pack()
        l_space1 = Label(my_frame1, text='\n', bg="#85eaed")
        l_space1.pack()

        bb2 = Button(my_frame1, text="Submit for testing", command=lambda : dataset_predict(dataset_path,my_frame2))
        bb2.pack()
        l_space2 = Label(my_frame1, text='\n', bg="#85eaed")
        l_space2.pack()
        
        exit = Button(top2, text="Exit", command=top2.quit)
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












