import tensorflow as tf
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Initialize lists to store the images and labels
images = []
labels = []

# Loop through the folders containing the images
for folder in os.listdir('Data/Boards'):
    folder_path = os.path.join('Data/Boards', folder)
    label = folder
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        #Resize the image to 500x500
        image = cv2.resize(image, (500, 500))
        images.append(image)
        labels.append(label)

# Convert the lists of images and labels into numpy arrays
images = np.array(images)
labels = np.array(labels)

le = LabelEncoder()
labels = le.fit_transform(labels)
labels = tf.keras.utils.to_categorical(labels)


X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(500, 500, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(np.unique(labels)), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save the model
model.save('model.h5')
