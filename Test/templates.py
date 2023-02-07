import cv2

templates = []
# templates.append(cv2.imread("./templates/black_bishop.png", 0))
# templates.append(cv2.imread("./templates/black_king.png", 0))
# templates.append(cv2.imread("./templates/black_knight.png", 0))
# templates.append(cv2.imread("./templates/black_pawn.png", 0))
# templates.append(cv2.imread("./templates/black_queen.png", 0))
# templates.append(cv2.imread("./templates/black_rook.png", 0))
templates.append(cv2.imread("templates/white-bishop.png", 0))
templates.append(cv2.imread("templates/white-king.png", 0))
templates.append(cv2.imread("templates/white-knight.png", 0))
templates.append(cv2.imread("templates/white-pawn.png", 0))
templates.append(cv2.imread("templates/white-queen.png", 0))
templates.append(cv2.imread("templates/white-rook.png", 0))

#Downscale and make grayscale
for i in range(len(templates)):
    templates[i] = cv2.resize(templates[i], (0,0), fx=0.25, fy=0.25)
    