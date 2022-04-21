import converter2gray
import downloader
import send_email
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/Htmls/index.html')


def cvt2gray(request):
    url = request.POST['image_url']
    name = request.POST['name']
    email_id = request.POST['email_id']
    choice = request.POST['choice_im_vi']
    if choice == 'image':
        downloader.image_downloader(url)
        converter2gray.image_convert2gray()
        send_email(name, email_id)
        return render(request,
                      '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/Htmls/display_image.html')

    else:
        downloader.video_downloader(url)
        converter2gray.video_convert2gray()
        return render(request, '/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/Htmls/video_thankyou'
                               '.html')
