# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 02:55:35 2022

@author: hashem
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from flask import Flask, request , render_template
import pickle

app = Flask("__name__")


@app.route("/", methods =["Get"] )
def loadPage():
	return render_template("index.html")



@app.route("/", methods=['POST'])
def predict():
    columns = pd.read_csv("selected.csv")    
    columns.drop("Unnamed: 0", axis = 1, inplace = True)
    ColumnList = columns.columns.values
    
    j = 0
    inputQuery = []
    for i in ColumnList:
        inputQuery[j] = request.form[str(i)]
        j += 1
        
    listinput = ColumnList.copy()
        
    for i in range (38):
        if listinput[i] in inputQuery:
            listinput[i] = 1
        else:
            listinput[i] = 0
    
    model = pickle.load(open("model.sav", "rb"))
    single = model.predict(listinput.reshape(1,-1))
    probablity = model.predict_proba(listinput.reshape(1,-1))[:,1]
    
    o1 = "You have been diagnosoed with "+str(single)
    o2 = "Confidence = "+str(probablity)
            
            
          
           
    return render_template('index.html', output1=o1, output2=o2, 
                               inputQuery = request.form[ColumnList]
                               )
    
if __name__ == '__main__':
    app.run()        
        
  