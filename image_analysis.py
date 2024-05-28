import cv2
import matplotlib.pyplot as plt
from opencv_basics_grayscale import histogram_grayscale
from opencv_basics_BGR import histogram_BGR

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
    imgBGR = cv2.imread(image1_location) 
    cv2.imwrite('modified95BGR.jpg', imgBGR, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.imwrite('modified75BGR.jpg', imgBGR, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
    cv2.imwrite('modified50BGR.jpg', imgBGR, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    imgmod95BGR = cv2.imread('modified95BGR.jpg') 
    imgmod75BGR = cv2.imread('modified75BGR.jpg') 
    imgmod50BGR = cv2.imread('modified50BGR.jpg') 

    cv2.imshow(f'modified95.jpg', imgmod95)
    cv2.imshow(f'modified75.jpg', imgmod75)
    cv2.imshow(f'modified50.jpg', imgmod50)

    cv2.imshow(f'modified95BGR.jpg', imgmod95BGR)
    cv2.imshow(f'modified75BGR.jpg', imgmod75BGR)
    cv2.imshow(f'modified50BGR.jpg', imgmod50BGR)
    print(f'grayscale Histogram: {histogram_grayscale(img)}')
    print(f'BGR Histogram: {histogram_BGR(imgBGR)}')
    
    # define data values
    x = range(256) 
    y = histogram_grayscale(img)
    y95 = histogram_grayscale(imgmod95)
    y75 = histogram_grayscale(imgmod75)
    y50 = histogram_grayscale(imgmod50)

    yB, yG, yR = histogram_BGR(imgBGR)
    y95B, y75G, y50R = histogram_BGR(imgmod95BGR)
    y75B, y75G, y75R = histogram_BGR(imgmod75BGR)
    y50B, y50G, y50R = histogram_BGR(imgmod50BGR)

    f1 = plt.figure(1)
    plt.plot(x, y50, color="#C4C4C4", label = "jpeg, 50% quality") 
    plt.plot(x, y75, color="#828282", label = "jpeg, 75% quality") 
    plt.plot(x, y95, color="#505050", label = "jpeg, 95% quality") 
    plt.plot(x, y, color="#3C3C3C", label = "original png") 
    plt.legend()
    plt.title("Luminosity -Frequency Analysis", loc='center')
    f2 = plt.figure(2)
    plt.plot(x, y50B, color="#C4C4C4", label = "blue") 
    plt.plot(x, y50G, color="#C4C4C4", label = "green") 
    plt.plot(x, y50R, color="#C4C4C4", label = "red") 
    plt.plot(x, y50, color="#C4C4C4", label = "luminosity") 
    plt.title("Luminosity and Color-Frequency Analysis, 50% Quality JPEG", loc='center')
    f3=plt.figure(3)
    plt.plot(x, y75B, color="#828282", label = "blue") 
    plt.plot(x, y75G, color="#828282", label = "green") 
    plt.plot(x, y75R, color="#828282", label = "red") 
    plt.plot(x, y75, color="#828282", label = "luminosity") 
    plt.title("Luminosity and Color-Frequency Analysis, 75% Quality JPEG", loc='center')
    f3=plt.figure(4)
    plt.plot(x, y95B, color="#505050", label = "jpeg, 95% quality") 
    plt.plot(x, y95B, color="#505050", label = "jpeg, 95% quality") 
    plt.plot(x, y95B, color="#505050", label = "jpeg, 95% quality") 
    plt.plot(x, y95B, color="#505050", label = "jpeg, 95% quality") 
    plt.title("Luminosity and Color-Frequency Analysis, 95% Quality JPEG", loc='center')
    f3=plt.figure(4)
    plt.plot(x, yBGR, color="#3C3C3C", label = "original png") 
    plt.title("Luminosity and Color-Frequency Analysis, Original png", loc='center')
    plt.legend()
    plt.show()  # display
    cv2.waitKey() 
    cv2.destroyAllWindows() 