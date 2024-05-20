import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale

if __name__ == '__main__':
    image1_location='cinnamoroll.png'
    img = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) #Value/Luminosity 
    cv2.imshow(f'{image1_location} - original', img) 
    cv2.imwrite('modified95.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.imwrite('modified75.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
    cv2.imwrite('modified50.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    imgmod95 = cv2.imread('modified95.jpg', cv2.IMREAD_GRAYSCALE) 
    imgmod75 = cv2.imread('modified75.jpg', cv2.IMREAD_GRAYSCALE) 
    imgmod50 = cv2.imread('modified50.jpg', cv2.IMREAD_GRAYSCALE) 

    cv2.imshow(f'modified95.jpg', imgmod95)
    cv2.imshow(f'modified75.jpg', imgmod75)
    cv2.imshow(f'modified70.jpg', imgmod50)
    print(f'grayscale Histogram: {histogram_grayscale(img)}')
    
    # define data values
    x = range(256) 
    y = histogram_grayscale(img)
    y95 = histogram_grayscale(imgmod95)
    y75 = histogram_grayscale(imgmod75)
    y50 = histogram_grayscale(imgmod50)
    
    plt.plot(x, y, label = "luminosity", color='grey') 
    plt.plot(x, y95, label = "luminosity", color='grey') 
    plt.plot(x, y75, label = "luminosity", color='grey') 
    plt.plot(x, y50, label = "luminosity", color='grey') 
    plt.legend()
    plt.title("Luminosity -Frequency Analysis", loc='center')
    plt.show()  # display
    cv2.waitKey() 
    cv2.destroyAllWindows() 