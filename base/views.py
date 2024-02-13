from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config
import smtplib
import requests

def index(request):
  return render (request, 'base/base.html')

def about(request):
  return render (request, 'about/about.html')

def email_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        
        msg = MIMEMultipart()
        msg['From'] = 'wajiwos14@gmail.com'
        msg['To'] = 'wajiwos14@gmail.com'
        msg['Subject'] = 'New Message From: ' + name
        
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText('\nName: '+ name +'\nEmail: '+ email,'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config('ID', cast=str), config('PASS', cast=str))
        server.send_message(msg)
        server.quit()

        return render (request, 'about/thank.html')
    else:
        return render(request, 'about/about.html')


def portfolio(request):
  return render(request, 'blogs/portfolio.html')


def my_github_repos(request):

    response = requests.get(config('GIT-KEY', cast=str))
    repos = response.json()
    
    return render(request, 'blogs/portfolio.html', {'repos': repos})
