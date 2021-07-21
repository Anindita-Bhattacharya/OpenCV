import cv2
img=cv2.imread('lena.jpg',1) #this will read the image
print(img) #this will print the image in the form of  matrix
cv2.imshow('image',img) #this will show the image
k=cv2.waitKey(5000) #this will show the image for 5000 miliseconds means for 5 seconds
if k==27: #when escape button is pressed then all the windows get closed
    cv2.distroyAllWindow()  # this will distroy the window which is created
elif k==ord('a'):
    #windows are destroyed when we press a but before that file is created
    cv2.imwrite('lena_copy.png', img)  # to write an image in the form of file
    cv2.distroyAllWindow()  # this will distroy the window which is created





