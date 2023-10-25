from django.shortcuts import render
from .forms import UserInputForm
from .models import UserInput
import tensorflow as tf
import numpy as np
import cv2
import os

def Spiral_Test(image):
    # Load the CNN model and perform classification on the image
    model = tf.keras.models.load_model('classifier\AVGPOOL_PARKV04.h5')
    # Perform classification on the image and return the result
    pred = model.predict(image)
    return pred

def Wave_Test(image):
    # Load the CNN model and perform classification on the image
    model = tf.keras.models.load_model('classifier\WAVE_V01.h5')
    # Perform classification on the image and return the result
    pred = model.predict(image)
    return pred

def predict_result(image_path, image_type):
    # Load the image and preprocess it
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)

    # Perform classification on the image and return the result
    if(image_type=="spiral"):
        result = Spiral_Test(img)
        if (result<0.5):
            return "Healthy"
        else:
            return "Parkinson"
        
    elif(image_type=="wave"):
        result = Wave_Test(img)
        if (result<0.5):
            return "Healthy"
        else:
            return "Parkinson"

def handle_user_input(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the user input data to the database
            user_input = form.save()
            image_type = user_input.image_type
            # Process the uploaded image and classify it
            image_path = user_input.image.path
            result = predict_result(image_path, image_type)
            # Save the result to the database and update the user input record
            user_input.result = result
            user_input.save()
            # Render the results page with the image and the result
            context = {'user_input': user_input}
            return render(request, 'classifier/results.html', context)
    else:
        form = UserInputForm()
    context = {'form': form}
    return render(request, 'classifier/form.html', context)
