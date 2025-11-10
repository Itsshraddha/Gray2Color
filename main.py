import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Read grayscale image ---
# Make sure the image (e.g. BwImage.jpg) is in the same folder as this script
gray_image = cv2.imread('BwImage.jpg', cv2.IMREAD_GRAYSCALE)

if gray_image is None:
    raise FileNotFoundError("Image not found! Make sure 'BwImage.jpg' is in the same directory.")

# --- Step 2: Apply a color map to simulate colorization ---
colored_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_INFERNO)

# --- Step 3: Display results ---
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title('Black & White Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Colorized Image')
plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# --- Step 4: Save the colorized output ---
cv2.imwrite('Colorized_BwImage.jpg', colored_image)
print("✅ Colorized image saved as 'Colorized_BwImage.jpg'")
