import pickle
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2


model = pickle.load(open('./model/digits_recognition.pkl', 'rb'))
pca = pickle.load(open('./model/pca.pkl', 'rb'))

def pca_transform(data):
    arr = data.flatten()
    arr = arr.reshape(1, -1)
    pca.transform(arr)  
    return  pca.transform(arr) 

def predict(data):
    return model.predict(data)

def predict_proba(data):
    return model.predict_proba(data)