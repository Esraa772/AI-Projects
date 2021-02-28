from cv2 import *
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import time
from os import system

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5',compile=False)
while True:
    s, img = cam.read()
    while not s:
        s, img = cam.read()
    #if s:    # frame captured without any errors
        #namedWindow("cam-test")
        #imshow("cam-test",img)
        #waitKey(0)
        #destroyWindow("cam-test")
    imwrite("test_photo.jpg",img) #save image

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open('test_photo.jpg')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    #image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    
    # run the inference
    prediction = model.predict(data)
    print ("\n" * 10)
    if prediction[0][0]<0.1:
        print("Headphone case: ")
    elif prediction[0][0]<0.2:
        print("Headphone case: #")
    elif prediction[0][0]<0.3:
        print("Headphone case: ##")
    elif prediction[0][0]<0.4:
        print("Headphone case: ###")
    elif prediction[0][0]<0.5:
        print("Headphone case: ####")
    elif prediction[0][0]<0.5:
        print("Headphone case: #####")
    elif prediction[0][0]<0.7:
        print("Headphone case: ######")
    elif prediction[0][0]<0.8:
        print("Headphone case: #######")
    elif prediction[0][0]<0.9:
        print("Headphone case: ########")
    else:
        print("Headphone case: #########")
    if prediction[0][1]<0.1:
        print("Raspberry case: ")
    elif prediction[0][1]<0.2:
        print("Raspberry case: #")
    elif prediction[0][1]<0.3:
        print("Raspberry case: ##")
    elif prediction[0][1]<0.4:
        print("Raspberry case: ###")
    elif prediction[0][1]<0.5:
        print("Raspberry case: ####")
    elif prediction[0][1]<0.5:
        print("Raspberry case: #####")
    elif prediction[0][1]<0.7:
        print("Raspberry case: ######")
    elif prediction[0][1]<0.8:
        print("Raspberry case: #######")
    elif prediction[0][1]<0.9:
        print("Raspberry case: ########")
    else:
        print("Raspberry case: #########")
    print ("\n" * 20)
    time.sleep(0.5)
  #  print(prediction)
