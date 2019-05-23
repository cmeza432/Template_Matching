"""
Name:           Carlos Meza
Description:
 Using two images of different sizes, find the smaller(template image) within the bigger(main image)
 using the match template function from skimage feature.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.feature import match_template

# Function for displaying image
def show_images(n, image, title):
    plt.figure(n)
    plt.imshow(image, cmap = plt.cm.gray)
    plt.title(title)

# Convert an image into greyscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Function that finds best match for the template in the main image
def findImage(mainImage, template) :
    # Read both images
    temp_main = mpimg.imread(mainImage)
    temp_small = mpimg.imread(template)
    
    # Convert both images into grayscale
    main = rgb2gray(temp_main)
    small = rgb2gray(temp_small)
    
    # Create an array of those pixel values
    main_data = np.array(main, dtype=None)
    template_data = np.array(small, dtype=None)
    
    # Print out both original images in greyscale
    show_images(0, main_data, "Main Image w/ greyscale")
    show_images(1, template_data, "Template image w/ greyscale")

    # Apply the match template function
    result = match_template(main_data, template_data, pad_input=True)
    
    # Variables to hold index values, size of half of template
    temp_row = int(len(template_data) / 2)
    temp_col = int(len(template_data[0]) / 2)
    rows = 0
    cols = 0
    temp = result[0][0]
    i = 0

    # Loop through main image and find highest correlation value as center
    while(i <= int(len(result)) - 1):
        k = 0
        while(k <= int(len(result)) - 1):
            if(result[i][k] > temp):
                temp = result[i][k]
                rows = i
                cols = k
            k += 1
        i += 1

    # Assign index values on main image to know area of template
    beg_row = rows - temp_row
    beg_col = cols - temp_col
    rows = rows + temp_row
    cols = cols + temp_col 

    # Black out the image from the main image with index values
    main_data[beg_row:rows, beg_col:cols] = 0

    # Plot out final image with black square where template is found
    show_images(2, main_data, "Main image w/ template removed")
    plt.show()
    
#############  main  #############
if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    findImage(mainImage, template)
