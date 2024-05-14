'''
OpenCV Basics - BGR Exercises
'''
import cv2
import math 

def pixel_count(BGR_image: list)-> int:
    """ Calculates the total number of pixels in a BGR image.

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        int: The number of pixels in a BGR image.
    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()
    return ((len(img))*(len(img[0])))
    # END OF FUNCTION.

def tint_red(BGR_image:list)->list:
    """ This function tints a color image red. Given an input image that is BGR color,
    set the the red channel value of all pixels to 255 

    Args:
        BGR_image (list): A color image represented in a numpy array with 3 channels.

    Returns:
        image (list): The tinted image.

    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()
    
    for r, row in enumerate(img):
        for c, value in enumerate(row):
            img[r][c][2] = 255
    

    return img
    # END OF FUNCTION.

def to_BW(BGR_image: list)-> list:
    """ Converts a BGR image to a black and white image.
        If the pixel value (defined by (B+G+R)/3) in the original image is strictly greater than 128, 
        set the pixel to 255. Otherwise, set the pixel to 0. 

        Notes: 
            - You may NOT use any thresholding functions provided by OpenCV to do this.
            - Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        image (list): The black and white image.
    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()
    
    for r, row in enumerate(img):
        for c, value in enumerate(row):
            if math.trunc((int(value[0]) + int(value[1]) + int(value[2]))/3) > 128:
                img[r][c] = 255
            else:
                img[r][c] = 0
    

    return img
    # END OF FUNCTION.

def to_grayscale(BGR_image: list)-> list:
    """ Converts a BGR image to a grayscale image by taking a uniform average of all 3 
        color channels: (B+G+R)/3
    
        Notes: 
            - Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented by 3 channels of 8-bit integers

    Returns:
        image (list): The grayscale image of 8-bit integers.
    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()
    
    for r, row in enumerate(img):
        for c, value in enumerate(row):
            img[r][c] = math.trunc((int(value[0]) + int(value[1]) + int(value[2]))/3)
    

    return img
    # END OF FUNCTION.

def image_average_BGR(BGR_image1:list, BGR_image2:list)-> list:
    """ Averages the pixels of the two BGR input images by adding up the two input
        images on a per pixel, per channel basis and dividing each by two (truncated).

        Notes: 
            - You may assume image1 and image2 are the SAME size.
            - Be careful not to modify the original image! 
            - Be careful to avoid integer overflow!

    Args:
        BGR_image1 (list): A BGR image represented in an array represented by 3 channels of 8-bit integers
        BGR_image2 (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        image3 (list): An BGR image which is the average of image1 and image2.

    """
    # WRITE YOUR CODE HERE.
    img = BGR_image1.copy()
    img2 = BGR_image2.copy()

    for r, row in enumerate(img):
        for c, (value1, value2) in enumerate(zip(row, img2[r])):
            img[r][c][0] = math.trunc((int(value1[0]) + int(value2[0]))/2)
            img[r][c][1] = math.trunc((int(value1[1]) + int(value2[1]))/2)
            img[r][c][2] = math.trunc((int(value1[2]) + int(value2[2]))/2)
    return img
    # END OF FUNCTION.

def flip_horizontal_BGR(BGR_image:list)->list:
    """ Flips the input image across the horizontal axis. This can be interpreted as 
    switching the first and last column of the image, the second and second to last column, and so on.
    
    Note: Be careful not to modify the original image! 

    Args:
        BGR_image (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        image (list): The horizontally flipped image.

    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()

    for r, row in enumerate(img):
        img[r] = row[::-1]
    return img
    # END OF FUNCTION.

def histogram_BGR(BGR_image:list)->list:
    """ Counts the number of pixels of each value (0 -> 255) in the BGR image

    Args:
        BGR_image (list): A BGR image represented in an array represented by 3 channels of 8-bit integers

    Returns:
        blue_list: A list with 256 elements, where the value of the ith element represents the ith Blue count
        green_list: A list with 256 elements, where the value of the ith element represents the ith Green count
        red_list: A list with 256 elements, where the value of the ith element represents the ith Red count
    """
    # WRITE YOUR CODE HERE.
    img = BGR_image.copy()
    pixelB_list = []
    pixelG_list = []
    pixelR_list = []
    blue_list = [0] * 256
    green_list = [0] * 256
    red_list = [0] * 256
    for r, row in enumerate(img):
        for c, value in enumerate(row):
            pixelB_list.append(img[r][c][0])
            pixelG_list.append(img[r][c][1])
            pixelR_list.append(img[r][c][2])

    for value in range(len(blue_list)):
        blue_list[value] = pixelB_list.count(value)
    
    for value in range(len(green_list)):
        green_list[value] = pixelG_list.count(value)

    for value in range(len(red_list)):
        red_list[value] = pixelR_list.count(value)

    return blue_list, green_list, red_list
    # END OF FUNCTION.

if __name__ == '__main__':
    image1_location='dog.jpg' #400 × 217 pixels
    image2_location='dog2.jpg' #400 × 217 pixels
    img = cv2.imread(image1_location, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image1_location} - original', img) 
    img2 = cv2.imread(image2_location, cv2.IMREAD_COLOR) 
   
    print(f'Pixel Count: {pixel_count(img)}')

    #cv2.imwrite("Tinted.jpg", tint_red(img)) 
    cv2.imshow(f'{image1_location} - tint_red', tint_red(img)) 
    #cv2.imwrite("BW.jpg", to_BW(img)) 
    cv2.imshow(f'{image1_location} - to_BW', to_BW(img)) 
    #cv2.imwrite("GS.jpg", to_grayscale(img)) 
    cv2.imshow(f'{image1_location} - to_grayscale', to_grayscale(img)) 
    #cv2.imwrite("Averaged.jpg", image_average_BGR(img, img2)) 
    cv2.imshow(f'{image1_location} v. {image2_location} - average_BGR', image_average_BGR(img, img2)) 
    #cv2.imwrite("Flipped.jpg", flip_horizontal_BGR(img))
    cv2.imshow(f'{image1_location} - flip_horizontal_BGR', flip_horizontal_BGR(img)) 
    blue_hist, green_hist, red_hist = histogram_BGR(img)
    print(f'Blue Histogram: {blue_hist}')
    print(f'Green Histogram: {green_hist}')
    print(f'Red Histogram: {red_hist}')
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 