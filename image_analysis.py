import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale

if __name__ == '__main__':
    image1_location='dog.png'
    img = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
    cv2.imshow(f'{image1_location} - original', img) 

    print(f'grayscale Histogram: {histogram_grayscale(img)}')
    
    # define data values
    x = range(256) 
    y = histogram_grayscale(img)
    
    plt.plot(x, y, label = "luminosity", color='grey') 
    plt.legend()
    plt.title("Luminosity -Frequency Analysis", loc='center')
    plt.show()  # display
    cv2.waitKey() 
    cv2.destroyAllWindows() 