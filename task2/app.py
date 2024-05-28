import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import streamlit as st

st.header("Image Recognition or Object Detection")
model=load_model('Image_Classification.keras')

data_cat=['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'sapna sarkar',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']

image=st.text_input("Enter image name",'apple.jpg')

img_width=180
img_height=180

image_load=tf.keras.utils.load_img(image,target_size=(img_height,img_width))
img_arr=tf.keras.utils.array_to_img(image_load)
img_bat=tf.expand_dims(img_arr,0)
predict=model.predict(img_bat)
score=tf.nn.softmax(predict)
st.image(image,width=200)

st.write('This image is '+data_cat[np.argmax(score)])
st.write('with accuracy of'+str(np.max(score)*100))

#st.write("veg/fruite in image is {} with accuracy of {:0.2f}".format(data_cat[np.argmax(score)],str(np.max(score)*100)))