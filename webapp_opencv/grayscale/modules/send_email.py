# from django.conf import settings
# from django.core.mail import send_mail
#
#
# def sending_email(name, email_id):
#     subject = 'Image converted'
#     message = f'Hi {name}, thank you for using this service.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email_id]
#     send_mail(subject, message, email_from, recipient_list)

from django.core.mail import EmailMessage


def send_email(name, email_id):
    email = EmailMessage(
        'Hello',
        'Thank you for using this service',
        to=[email_id]
    )
    email.attach_file('/home/manav/PycharmProjects/django_openCV/webapp_opencv/grayscale/image_converted'
                      '/converted_img.jpg')
    email.send()
