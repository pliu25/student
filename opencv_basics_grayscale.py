'''
OpenCV Basics - Greyscale Exercises
'''
import cv2
import math

def pixel_count(GS_image: list)-> int:
    """ Calculates the total number of pixels in an image.

    Args:
        GS_image (list): A grayscale image of 8-bit integers.

    Returns:
        int: The number of pixels in an image.
    """
    # WRITE YOUR CODE HERE.
    img = GS_image.copy()
    return ((len(img))*(len(img[0])))
    # END OF FUNCTION.

def average_pixel_value(GS_image: list) -> int:
    """ Calculates the average pixel value of a grayscale image.

    Args:
        GS_image (list): A grayscale image of 8-bit integers.

    Returns:
        int: Average pixel value (truncated) in the image (Range of 0-255).
    """
    # WRITE YOUR CODE HERE.
    img = GS_image.copy()

    pixel_values = []
    for list in GS_image:
        for pixel in list:
            pixel_values.append(pixel)
    return math.trunc((sum(pixel_values))/((len(img))*(len(img[0]))))
    #return (math.trunc(img/img[0][0]))
    # END OF FUNCTION.

def to_BW(GS_image: list)-> list:
    """ Converts a grayscale image to a black and white image.
        If the pixel value in the original image is strictly greater than 128, 
        set the pixel to 255. Otherwise, set the pixel to 0. 

        Notes: 
            - You may NOT use any thresholding functions provided by OpenCV to do this.
            - Be careful not to modify the original image! 

    Args:
        GS_image (list): A grayscale image of 8-bit integers.

    Returns:
        image (list): The black and white image.
    """
    # WRITE YOUR CODE HERE.
    img = GS_image.copy()
    
    for r, row in enumerate(img):
        for c, value in enumerate(row):
            if value > 128:
                img[r][c] = 255
            else:
                img[r][c] = 0

    return img
    # END OF FUNCTION.

def image_average_grayscale(GS_image1:list, GS_image2:list)-> list:
    """ Averages the pixels of the two grayscale input images by adding up the two input
        images on a per pixel basis and dividing them by two (truncated).

        Notes: 
            - You may assume image1 and image2 are the SAME size.
            - Be careful not to modify the original image! 
            - Be careful to avoid integer overflow!

    Args:
        GS_image1 (list): A grayscale image represented in an array of 8-bit integers.
        GS_image2 (list): A grayscale image represented in an array of 8-bit integers.

    Returns:
        image3 (list): An image which is the average of image1 and image2.

    """
    # WRITE YOUR CODE HERE.
    pixel_values = []

    for list in GS_image1:
        for list2 in GS_image2:
            for pixel in list:
                for pixel2 in list2:
                    pixel_values.append(math.trunc((pixel + pixel2)/2))
    image3 = pixel_values 
    return image3
    # END OF FUNCTION.

def flip_horizontal_grayscale(GS_image:list)->list:
    """ Flips the input image across the horizontal axis. This can be interpreted as 
    switching the first and last column of the image, the second and second to last column, and so on.
    
    Note: Be careful not to modify the original image! 

    Args:
        GS_image (list): A grayscale image represented in an array of 8-bit integers.

    Returns:
        image (list): The horizontally flipped image.

    """
    # WRITE YOUR CODE HERE.

    # END OF FUNCTION.

def histogram_grayscale(GS_image:list)->list:
    """ Counts the number of pixels of each value (0 -> 255) in the grayscale image

    Args:
        GS_image (list): A grayscale image represented in an array of 8-bit integers.

    Returns:
        list: A list with 256 elements, where the value of the ith element represents the ith value count

    """
    # WRITE YOUR CODE HERE.

    # END OF FUNCTION.

if __name__ == '__main__':
    image1_location='dog.jpg' #400 × 217 pixels
    image2_location='dog2.jpg' #400 × 217 pixels
    img = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
    cv2.imshow(f'{image1_location} - original', img) 
    img2 = cv2.imread(image2_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity  
   

    print(f'Pixel Count: {pixel_count(img)}')
    print(f'Average Pivel Value: {average_pixel_value(img)}')
    #cv2.imwrite("BW.jpg", to_BW(img)) 
    cv2.imshow(f'{image1_location} - to_BW', to_BW(img)) 
    #cv2.imwrite("Averaged.jpg", image_average_grayscale(img, img2)) 
    cv2.imshow(f'{image1_location} v. {image2_location} - average_grayscale', image_average_grayscale(img, img2)) 
    #cv2.imwrite("Flipped.jpg", flip_horizontal_grayscale(img))
    #cv2.imshow(f'{image1_location} - flip_horizontal_grayscale', flip_horizontal_grayscale(img)) 
    #print(f'Grayscale Histogram: {histogram_grayscale(img)}')

    cv2.waitKey() 
    cv2.destroyAllWindows() 