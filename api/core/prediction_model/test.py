from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2

from django.conf import settings


def classify_image(path_to_image):

    path_to_model = settings.MODEL_URL  # add name of model(s) to path
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
    label = "Diabetic Macular Edema" if dme > normal else "Normal"
    proba = dme if dme > normal else normal
    label = "{}: {:.2f}%".format(label, proba * 100)
    print("{} {}".format(label, proba*100))


    # draw the label on the image
    output = imutils.resize(orig, width=496)
    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,	0.7, (0, 255, 0), 2)

    return label
