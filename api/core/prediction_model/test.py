from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2
import os

from django.conf import settings


def classify_image(path_to_image):

    path_to_model = os.path.join(settings.MODEL_URL, 'dme.model')  # add name of model(s) to path
    # load the image
    image = cv2.imread(path_to_image)
    orig = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network
    print("[INFO] loading network...")
    model = load_model(path_to_model)

    # classify the input image
    (normal, dme) = model.predict(image)[0]

    # build the label
    label = "DME" if dme > normal else "NORMAL"
    proba = dme if dme > normal else normal

    # draw the label on the image
    output = imutils.resize(orig, width=496)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,	0.7, (0, 255, 0), 2)

    return label, proba*100
