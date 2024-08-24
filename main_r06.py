import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 gradient image
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
image_array = (X + Y) / 2 * 255  # Combine X and Y for a gradient effect

# Display the image
plt.imshow(image_array, cmap='gray')
plt.axis('off')  # Turn off axis labels
plt.show()
