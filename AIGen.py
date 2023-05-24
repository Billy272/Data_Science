#Generate an AI that creates an image based on a given image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = mpimg.imread('image.webp')
# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, channels = img.shape
# Display the image dimensions
print(height, width, channels)
# Display the image
plt.imshow(img)
plt.show()
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Display the grayscale image
plt.imshow(gray_img, cmap='gray')
plt.show()
# Normalize the image

# Get the maximum and minimum values of the pixel
min_val = np.amin(gray_img)
max_val = np.amax(gray_img)
# Normalize the pixels in the range 0-1
normalized_img = (gray_img - min_val) / (max_val - min_val)
# Display the normalized image
plt.imshow(normalized_img, cmap='gray')
plt.show()
# Create a new figure
plt.figure()
# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)
# Show the normalized image
plt.subplot(1, 2, 2)
plt.imshow(normalized_img, cmap='gray')
# Show the figure
plt.show()
# Create a new figure
plt.figure()
# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)
# Show the normalized image
plt.subplot(1, 2, 2)
plt.imshow(normalized_img, cmap='gray', vmin=0, vmax=1)
# Show the figure
plt.show()
# Create a new figure
plt.figure()
# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)
# Show the normalized image
plt.subplot(1, 2, 2)
plt.imshow(normalized_img, cmap='gray', vmin=0.5, vmax=1)