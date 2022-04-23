import wget
from pytube import YouTube
import pytube
import os


def image_downloader(url):
    # path_download = '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_downloads/'
    # filename = wget.download(url)
    # # arr=os.listdir(path_download)
    # print(filename)
    site_url = 'http://www.randomdatabase.com/database_files/csv/main_database.csv'
    file_name = wget.download(site_url)
    print(file_name)

image_downloader('https://parade.com/wp-content/uploads/2019/10/Life-Quotes-Dolly-680x430.jpg')


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
