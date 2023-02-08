import numpy as np
from tensorflow.keras.models import load_model
import cv2

model = load_model('model.h5')


# Choose an image to test
test_image = cv2.imread('Data/Boards/1K6_4B3_1P1p4_2bN3r_1q6_P3p1P1_1pPk1p2_5n2/00001.jpg')

# Resize the image to 500x500
test_image = cv2.resize(test_image, (500, 500))

# Reshape the test image to match the input shape of the model
test_image = np.reshape(test_image, (1, 500, 500, 3))

# Use the model to make predictions
prediction = model.predict(test_image)

# Get the label with the highest probability
predicted_label = np.argmax(prediction)

# Print the prediction
print("Predicted Label:", predicted_label)