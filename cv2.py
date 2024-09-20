import cv2 

img =cv2.imread('Screenshot 2024-06-08 084704.png')
def circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,255,0),-1)
cv2.namedWindow(winname  = 'name')
cv2.setMouseCallback('name',circle)
while True:
    cv2.imshow('name',img)
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.destroyAllWindows