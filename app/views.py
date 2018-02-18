from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    parsed_data = []
    if request.method == 'POST':
        user_name = request.POST.get('user')
        json_list = []
        user_data = {}

        req = requests.get('https://api.github.com/users/' + user_name)
        if req.status_code is 200:
            json_list.append(json.loads(req.text))
            for data in json_list:
                user_data['name'] = data['name']
                user_data['blog'] = data['blog']
                user_data['email'] = data['email']
                user_data['public_gists'] = data['public_gists']
                user_data['public_repos'] = data['public_repos']
                user_data['avatar_url'] = data['avatar_url']
                user_data['followers'] = data['followers']
                user_data['following'] = data['following']
        else:
            user_data['name'] = "User does not exist"

        parsed_data.append(user_data)

    return render(request, 'app/profile.html', {'data': parsed_data})
