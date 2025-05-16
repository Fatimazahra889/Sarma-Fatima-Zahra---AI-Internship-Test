import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load the model
model = MobileNet(weights='imagenet')
print("✅ MobileNet model loaded!")

# Load an example image from local (replace with your own if you want)
img_path = "cat.jpg"
img = image.load_img(img_path, target_size=(224, 224))

# Preprocess the image
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Predict
preds = model.predict(x)
decoded = decode_predictions(preds, top=3)[0]

print("🔮 Predictions:")
for i, (imagenetID, label, prob) in enumerate(decoded):
    print(f"{i+1}. {label}: {prob:.4f}")
