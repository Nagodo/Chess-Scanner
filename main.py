import cv2
import numpy as np

# Indlæser billedet
image = cv2.imread('board1.jpg')

#Gøre billedet mindre
image = cv2.resize(image, (0,0), fx=0.25, fy=0.25)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold, threshold_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#FInder den største kant
biggest_contour = max(contours, key=cv2.contourArea)

#Tegner den 
cv2.drawContours(image, [biggest_contour], 0, (0, 255, 0), 3)


#Finder alle de sorte pixels i billedet. Det må være de sorte felter
black_pixels = np.where(threshold_image == 255)

#Finder alle x og y koordinaterne for de sorte pixels
contour_coords = biggest_contour[:, 0, :]
contour_x_coords = contour_coords[:, 0]
contour_y_coords = contour_coords[:, 1]



#FInd min and max x and y coords
min_x = np.min(contour_x_coords)
max_x = np.max(contour_x_coords)
min_y = np.min(contour_y_coords)
max_y = np.max(contour_y_coords)


# Loop through all black pixels and get the coords
for i in range(len(black_pixels[0])):
    x = black_pixels[1][i]
    y = black_pixels[0][i]

    #If the pixel is not in the contour, remove it
    if x < min_x or x > max_x or y < min_y or y > max_y:
        black_pixels[0][i] = -1
        black_pixels[1][i] = -1


#Draw the black pixels
image[black_pixels] = (0, 0, 255)


#Finder alle felterne. De skal laves om til individuelle billeder. (Ikke færdigt)
for x in range(8):
    for y in range(8):
        pass

cv2.imshow('image', image)
cv2.waitKey(0)


cv2.destroyAllWindows()