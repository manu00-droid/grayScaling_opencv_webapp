import cv2 as cv
import os


def convert_gray():
    path = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/downloads/image1'
    image = cv.imread(path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imwrite('/webapp_opencv/grayscale/downloads_converted/converted1.jpg',
               gray)
    os.remove(path)

#
# convert_gray()
