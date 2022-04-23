import cv2 as cv
import os


def image_convert2gray():
    path_of_scaled_img = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_scaled/imageScaled.jpg'
    image = cv.imread(path_of_scaled_img)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    path = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/images_converted'
    cv.imwrite(os.path.join(path, 'converted_img.jpg'), gray)
    os.remove(path_of_scaled_img)

# image_convert2gray()


def video_convert2gray(rescale_to):
    capture = cv.VideoCapture('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_downloads'
                              '/myvideomp4.mp4')
    frame_width = int(capture.get(3))
    frame_height = int(capture.get(4))
    size = (frame_width, frame_height)
    newVideo = cv.VideoWriter('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_converted/gray'
                              '.mp4', cv.VideoWriter_fourcc(*'mp4v'), 60, size, isColor=False)

    while True:
        isTrue, frame = capture.read()
        frame_resized = scaler.rescale_frame(frame, rescale_to)
        if isTrue:
            gray_frame = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
            newVideo.write(gray_frame)
        else:
            break
    capture.release()
    newVideo.release()


# video_convert2gray(0.5)
