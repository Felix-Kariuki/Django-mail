from django.shortcuts import render
from Contactform.forms import ContactFormEmail
from django.core.mail import send_mail

def ContactSendMail(request):
    if request.method == "GET":
        form = ContactFormEmail()
    else:
        form = ContactFormEmail(request.POST)
        if form.is_valid():
            fromemail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,fromemail,['felixmurimi280@gmail.com'])
    return render(request,'contactform.html',{'form':form})