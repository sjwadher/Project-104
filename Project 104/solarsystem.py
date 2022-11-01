import cv2

img=cv2.imread("solar-system.jpg")


cv2.putText(img,
            "SUN",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "Mercury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "venus",
            (200,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "earth",
            (280,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "mars",
            (370,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "jupiter",
            (550,390),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "saturn",
            (800,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "uranus",
            (980,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))
cv2.putText(img,
            "neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0))



cv2.imshow("output",img)

cv2.waitKey(0)




cv2.imwrite("SSN.jpg",img)