import wget
from pytube import YouTube
import pytube


def image_downloader(url):
    wget.download(url, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/downloads/image1')


def video_downloader(url):
    save_path = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/video_downloads/'
    link = url
    video_youtube_obj = YouTube(link)
    video_youtube_obj.title = 'myvideo'
    # myVideoStreams = video_youtube_obj.streams
    # print(myVideoStreams.all())

    video_stream_obj = video_youtube_obj.streams
    mp4file = video_stream_obj.filter(mime_type='video/mp4')
    mp4file.first().download(save_path)


# video_downloader(
#     url='https://www.youtube.com/watch?v=TAltjiZawV4')
