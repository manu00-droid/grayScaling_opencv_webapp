import cv2 as cv
import wget


def file_downloader(url):
    wget.download(url, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/downloads/image1')

#
# file_downloader(
#     url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.sz1kZWYU9QtL6ChRFMC8XQHaEK%26pid%3DApi&f=1')
