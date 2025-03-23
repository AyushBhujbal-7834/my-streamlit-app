import numpy as np
import pickle
import math
from flask import Flask ,request, jsonity,render_template

app = Flask(_name_),template_folder=("template",static_folder="staticfiles") ## assign flask = app
model = pickel.load(open('model.pkl','rb'))

@app.route('/')  ##root folder
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction  == 1:
        return render_template('index.html',prediction_text="Loan is rejected").format(prediction)
    else:
        return render_template('index.html',prediction_text="Loan is approved").format(prediction)
    
   if _name_ == "_main_":
       app.run(host="0.0.0.0",port=8080)
