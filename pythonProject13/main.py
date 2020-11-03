import cv2
smile_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")


img = cv2.imread("Nastja.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = smile_cascade_db.detectMultiScale(img_gray, 1.05, 100)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Fighting club", img)
cv2.waitKey(0)
