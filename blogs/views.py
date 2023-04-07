from django.shortcuts import render, HttpResponse
import requests


def index(request):
    headers = {
        'api-key': '<dev.to api key>',
    }
    response = requests.get('https://dev.to/api/articles/me', headers=headers)

    if response.status_code == 200:
        posts = response.json()
        return render(request, 'blogs/index.html', {'posts': posts})
    else:
        # Handle the error
        return HttpResponse("An error occurred while retrieving the posts")
