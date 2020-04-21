from django.shortcuts import render
from Mail import forms
from django.core.mail import send_mail


import re
def index(request):
    return render(request,'index.html')

def send_M(request):
    send=forms.Mail_send()
    if(request.method=='POST'):
        send=forms.Mail_send(request.POST)

        if(send.is_valid()):
            print(send['email'].value())
            print('sending!!!')
            send_mail(subject=send['subject'].value(),message=send['message'].value(),from_email='gokul35srinath@gmail.com',recipient_list=[send['email'].value()])
            print('sent!!!')
            return render(request,'index.html',{'rec':re.split('@',send['email'].value())[0]})
    return render(request,'base.html',{'form':send})