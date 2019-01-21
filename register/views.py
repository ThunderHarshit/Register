from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import team,participant

def register(request):
    return render(request,'index.html')

def successfull(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        teamname = request.POST['teamname']
        mem1 = request.POST['mem1']
        mem2 = request.POST['mem2']
        mem3 = request.POST['mem3']
        teamm = team()
        teamm.team_name = teamname
        teamm.team_email = email
        teamm.save()

        zerosms.sms(phno='9140299514',passwd='Shubhank12',message='Sent Using django',receivernum='+919589861196')

        participants = participant()
        participants.team = teamm
        participants.member1 = mem1
        participants.member2 = mem2
        participants.member3 = mem3
        participants.save()

        subject = "Kodeathon Registration Successfull"
        message = "Hii " + name +",\nThis is to inform you that your team("+teamname +") have been registered Successfully for kodethon to be held on 23/01/2019.\nThank you very much\n-Team bitwise"
        #message = 'hii' + name
        from_email = settings.EMAIL_HOST_USER
        to_list = [str(email)]
        send_mail(subject,message,from_email,to_list)
        return HttpResponse('successfull')
