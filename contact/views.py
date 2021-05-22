from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def send_massage(request):
    myInfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = f"From: {email} \n {request.POST['message']}"
        send_mail(
            subject,
            message,
            email,  # from
            [settings.EMAIL_HOST_USER]  # list of emails to send this message to
        )
    return render(request, 'contact/contact.html', {'myInfo': myInfo})
