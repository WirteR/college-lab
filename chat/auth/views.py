from django.shortcuts import render, redirect, render_to_response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.

def main(request):
    print(request.user)
    return render_to_response('pages/auth.html', {'user': request.user})

def register_page(request):
    print(request.user)
    return render(request, 'user_action/register.html')

def login_page(request):
    print(request.GET)
    if request.GET:
        url = request.GET['path']
    else:
        url = 'auth'
    request.GET = url
    return render(request, 'user_action/auth.html')


def register(request):
    if request.GET:
        url = request.GET['path']
    else:
        url = None
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            url = request.POST['url']
        except:
            url = ' '

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'user_action/register.html', {'error':'Логін уже зайнятий', 'url':url})
            else:
                User.objects.create_user(username=username, password=password1)
                return render(request, 'user_action/wait.html', {
                    'message':"Ви успішно зареєструвались!",
                    'url': '/auth/login/',
                    'url2':url
                })

        else:
            return render(request, 'user_action/register.html', {'error':'Паролі не співпадають', 'url':url})
    return render(request, 'user_action/register.html', {'url':url})

def login_view(request):
    if request.GET:
        url = request.GET['path']
    else:
        url = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            url = request.POST['url']
        except:
            url = 'auth'

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'user_action/wait.html', {
                'message':"Ви успішно увійшли!",
                'url': '/' + url +'/'
                })
            # return render(request, 'pages/auth.html', {'user': request.user})
        else:
            return render(request, 'user_action/auth.html', {'error':'Неправильний логін чи пароль', 'url':url })
    
    return render(request, 'user_action/auth.html', {'url':url})

def logout_view(request):
    if request.GET:
        url = request.GET['path']
    else:
        url = 'auth'
    logout(request)
    return render(request, 'user_action/wait.html', {
        'message': 'Ви вийшли. Переадресація',
        'url': '/'+ url +'/'
    })
    # return render(request, 'pages/auth.html')
