#Use the chess_best_model.h5 model to find chess pieces in an image
import cv2
from keras.models import load_model
from keras.utils import load_img , img_to_array
import numpy as np

classes = ["Bishop","King","Knight", "Pawn","Queen","Rook"]
model = load_model('Chessman-image-dataset/chess_best_model.h5')



img = cv2.imread('chessboard.png')
imgHeight = 256
imgWidth = 256


def prepareImage(pathToImage) :
    image = load_img(pathToImage , target_size=(imgHeight, imgWidth))
    imgResult = img_to_array(image)
    imgResult = np.expand_dims(imgResult , axis=0 )
    imgResult = imgResult / 255.
    return imgResult

img = prepareImage('chessboard.png')

#Get first 50x50 pixels of the image
img = img[0:256, 0:256]


detections = model.predict(img, batch_size=32, verbose=1)
print(detections)
answer = np.argmax(detections , axis=1 )

text = classes[answer[0]]
print ('Predicted : '+ text)

#Show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()







