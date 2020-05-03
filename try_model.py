from fastai import *
from fastai.text import *


input_s = input("Enter:   ")
loaded_model=load_learner('/home/talha/Desktop/Python-Sentiment-Analysis',"ulmfit_model.pkl")
predicted_val=loaded_model.predict(input_s)
print(str(predicted_val[0]))