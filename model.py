# model.py
from tensorflow.keras.applications.mobilenet import MobileNet, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

model = MobileNet(weights="imagenet")

def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return decode_predictions(preds, top=1)[0][0][1]  # Return label only
