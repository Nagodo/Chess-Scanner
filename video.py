import cv2


#Tænder kameraet
cap = cv2.VideoCapture(0)

WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

FIELD_WIDTH = 50
FIELD_HEIGHT = 50

x_offset = int((WIDTH - FIELD_WIDTH * 8) // 2)
y_offset = int((HEIGHT - FIELD_HEIGHT * 8) // 2)

print(WIDTH, HEIGHT)

def CropImage():    
    image = cv2.imread('image.png')

    #Crop image
    image = image[y_offset:y_offset + FIELD_HEIGHT * 8, x_offset:x_offset + FIELD_WIDTH * 8]
    #Save image
    cv2.imwrite('image.png', image)

#Viser video fra kameraet
while True:
    #Vis video
    ret, frame = cap.read()

    #Tegner 8x8 firkanter på billedet
    for x in range(8):
        for y in range(8):
            square_x = int((x * FIELD_WIDTH) + x_offset)

            square_y = int((y * FIELD_HEIGHT) + y_offset)
 
            #Tegner i midten af frame
            cv2.rectangle(frame, (square_x, square_y), (square_x + 50, square_y + 50), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    #Når der trykkes på ENTER, gemmes billedet
    if cv2.waitKey(1) & 0xFF == ord('k'):
        print('Gemmer billede...')
        cv2.imwrite('image.png', frame)
        print('Billede gemt')
        CropImage()
        break

    #Luk programmet hvis der trykkes på q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()