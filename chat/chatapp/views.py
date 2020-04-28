from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message
# Create your views here.

def chat(request):
    if request.method == 'POST':
        message = request.POST['message']
        user_id = int(request.user.id)
        user = User.objects.get(id=user_id)
        Message.objects.create(message=message, user_id=user)
        # if request.POST['query']:
        #     request.GET = request.POST['query']

    # if request.GET:
    #     username = request.GET['user']
    #     users = User.objects.all()
    #     messages = Message.objects.all()
    #     bool(users)
    #     bool(messages)
    #     # for x in users:
    #     #     if x.username == username:
    #     #         user = x
    #     first = []
    #     for x in users:
    #         for z in messages:
    #             if z.user_id.username == x.username:
    #                 first.append(z.message)
    #                 break

    #     messages_set = [x.message for x in messages if x.user_id.username == username]
    #     users_set = [x.username for x in users]
    #     first_msg = dict(zip(users_set, first))

    # username = 'wirter'
    # users = User.objects.all()
    # messages = Message.objects.all()
    # bool(users)
    # bool(messages)
    # first = []
    # messages_set = [x for x in messages if x.user_id.username == username]
    # users_set = [x.username for x in users]
    # for x in users_set:
    #     for z in messages:
    #         if z.user_id.username == x:
    #             first.append(z.message)
    #             break


    # first_msg = dict(zip(users_set, first))


    
    context = {
        'messages': Message.objects.all(),
    }

    return render(request, 'pages/chat.html', context)