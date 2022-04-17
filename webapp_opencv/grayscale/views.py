from django.shortcuts import render
import converter2gray, downloader


# Create your views here.
def index(request):
    return render(request, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/Htmls/index.html')


def cvt2gray(request):
    url = request.GET['image_url']
    downloader.file_downloader(url)
    converter2gray.convert_gray()
    return render(request, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/Htmls/display_image.html')
