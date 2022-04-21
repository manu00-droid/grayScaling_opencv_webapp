import cv2 as cv
import os


def image_convert2gray():
    path = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_downloads/image1'
    image = cv.imread(path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imwrite('/webapp_opencv/grayscale/images_converted/converted1.jpg',
               gray)
    os.remove(path)


def video_convert2gray():
    capture = cv.VideoCapture('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_downloads'
                              '/myvideomp4.mp4')
    frame_width = int(capture.get(3))
    frame_height = int(capture.get(4))
    size = (frame_width, frame_height)
    newVideo = cv.VideoWriter('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_converted/gray'
                              '.mp4', cv.VideoWriter_fourcc(*'mp4v'), 60, size, isColor=False)

    while True:
        isTrue, frame = capture.read()
        if isTrue:
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            newVideo.write(gray_frame)
        else:
            break
    capture.release()
    newVideo.release()


# video_convert2gray()
