import os.path
import cv2 as cv
import converter2gray
import os


def rescale_frame(rescale_to):
    path_of_downloaded_img = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_downloads/image1'
    img = cv.imread(path_of_downloaded_img)
    width = int(img.shape[1] * rescale_to)
    height = int(img.shape[0] * rescale_to)
    dimensions = (width, height)
    resized_img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    path_of_scaled_img = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_scaled'
    cv.imwrite(os.path.join(path_of_scaled_img, 'scaled_img.jpg'), resized_img)
    os.remove(path_of_downloaded_img)
    converter2gray.image_convert2gray()


# rescale_frame(0.2)
#
# capture = cv.VideoCapture('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_downloads'
#                           '/myvideomp4.mp4')
# frame_width = int(capture.get(3))
# frame_height = int(capture.get(4))
# size = (frame_width, frame_height)
# newVideo = cv.VideoWriter('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_converted/gray'
#                           '.mp4', cv.VideoWriter_fourcc(*'mp4v'), 60, size, isColor=False)
#
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescale_frame(frame, rescale_to=0.5)
#     if isTrue:
#         gray_frame = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
#         newVideo.write(gray_frame)
#     else:
#         break
# capture.release()
# newVideo.release()
#
# # img = cv.imread('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/images_converted/converted1.jpg')
# # resized = rescale_frame(img, rescale_to=0.5)
# # cv.imshow('resized', resized)
# # cv.waitKey(0)
