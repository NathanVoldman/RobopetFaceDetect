import cv2

# path
path = 'toy/images/temp/toy_001.jpg'

# Reading an image in default mode
image = cv2.imread(path)

h_i, w_i, c = image.shape

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (int(0.01*w), int(0.01*h))

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (int(0.98*w), int(0.98*h))

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
