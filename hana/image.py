

import cv2
import numpy as np

# Load the noisy image
#image = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\project\bha.jpeg")
image = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\project\harshi.jpeg")

# Apply Gaussian blur to denoise the image
denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the original and denoised images
cv2.imshow('Noisy Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the denoised image
cv2.imwrite('denoised_image.jpg', denoised_image)


#Image Denoising using Median Blur

import cv2
import numpy as np

# Load the noisy image
#image = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\project\bha.jpeg")
image = cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\project\harshi.jpeg")



# Apply median blur to denoise the image
denoised_image = cv2.medianBlur(image, 5)

# Display the original and denoised images
cv2.imshow('Noisy Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the denoised image
cv2.imwrite('denoised_image.jpg', denoised_image)


#Image Denoising using Non-Local Means

import cv2
import numpy as np

# Load the noisy image
image = cv2.imread(r"")

# Apply non-local means to denoise the image
denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Display the original and denoised images
cv2.imshow('Noisy Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the denoised image
cv2.imwrite('denoised_image.jpg', denoised_image)
