import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# prepare object points
nx = 9#TODO: enter the number of inside corners in x
ny = 6#TODO: enter the number of inside corners in y

objpoints = []
imgpoints = []

f, ax = plt.subplots(4, 5, figsize=(20, 20))

ax = ax.ravel()

objp = np.zeros((nx*ny,3), np.float32)
objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2) # x,y coord

images = glob.glob("./camera_cal/*.jpg")

# Make a list of calibration images
imgno=0

for fname in images:
    print (fname)
    img = mpimg.imread(fname)
    print (img.shape)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print (gray.shape)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    print ("Find -> ",ret,corners)
    # If found, draw corners
    if ret == True:
        imgpoints.append(corners)
        objpoints.append(objp)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
        #print (corners[0], corners[nx-1],corners[-1],corners[-nx])
        ax[imgno].imshow(img)
        imgno += 1


plt.subplots_adjust(hspace=0.3)
plt.show()
