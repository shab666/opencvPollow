import cv2 as cv
import sys

# Charger directement le fichier capot.png présent dans ton dossier
img = cv.imread("capot.png")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("copie_capot.png", img)