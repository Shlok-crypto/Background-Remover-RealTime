# Background-Remover-RealTime 
# Prerequisite
OpenCv 
Python 
Numpy 

# Input
Live Video
# Output
Foreground frame 
Background frame 
New Background frame w/ Foreground 

# Procedure
Read in the live frame 
Read in the replacement frame(background) 
Apply Thresholding on to the live frame 
Dilate the thresholded frame 
find Contoues in the dilated frame 
optimize/process the contours 
Draw(fill) the contour => this will be the foreground roi 
separate the foreground from Background (cv.bitwize_and)
remove the foreground Roi from the New Background (cv.bitwize_and(inverseRoi, NewBackground) 
Combine the New Background Roi and foreground Roi (cv.bitwize_or(NewBackground, Foreground)
