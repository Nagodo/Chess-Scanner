import cv2
import numpy as np

# Load the image
image = cv2.imread('board1.jpg')

#Resize the image to 1/4
image = cv2.resize(image, (0,0), fx=0.25, fy=0.25)

#Convert to black and white
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold, threshold_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#FInd the biggest contour
biggest_contour = max(contours, key=cv2.contourArea)

#Draw the biggest contour
cv2.drawContours(image, [biggest_contour], 0, (0, 255, 0), 3)

# #Find the convex hull
# hull = cv2.convexHull(biggest_contour)

# #Draw the convex hull
# cv2.drawContours(image, [hull], 0, (0, 0, 255), 3)

# #Find the convexity defects
# hull = cv2.convexHull(biggest_contour, returnPoints=False)
# defects = cv2.convexityDefects(biggest_contour, hull)

#Find all black pixels in the image and draw them
black_pixels = np.where(threshold_image == 255)

#Get the coords of the contour
contour_coords = biggest_contour[:, 0, :]
contour_x_coords = contour_coords[:, 0]
contour_y_coords = contour_coords[:, 1]



#FInd min and max x and y coords
min_x = np.min(contour_x_coords)
max_x = np.max(contour_x_coords)
min_y = np.min(contour_y_coords)
max_y = np.max(contour_y_coords)



print(min_x, max_x, min_y, max_y)

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

#Loop through image pixels
for x in range(image.shape[1]):
    for y in range(image.shape[0]):
        #If the pixel is not in the contour, remove it
        if x < min_x or x > max_x or y < min_y or y > max_y:
            image[y, x] = (0, 0, 0)

#Resize the image to remove black pixels
image = image[min_y:max_y, min_x:max_x]



#Split the image into 8x8 squares
square_width = int(image.shape[1] // 8)
square_height = int(image.shape[0] // 8)

#Loop through all squares
for x in range(8):
    for y in range(8):
        #Get the coords of the square
        square_x = x * square_width
        square_y = y * square_height

        #Get the square
        square = image[square_y:square_y + square_height, square_x:square_x + square_width]

        #Find the average color of the square
        average_color = np.average(square, axis=(0, 1))

        #If the average color is not black, draw a red square
        if average_color[0] != 0 or average_color[1] != 0 or average_color[2] != 0:
            cv2.rectangle(image, (square_x, square_y), (square_x + square_width, square_y + square_height), (0, 0, 255), 2)


        
        
        


cv2.imshow('image', image)
cv2.waitKey(0)


cv2.destroyAllWindows()