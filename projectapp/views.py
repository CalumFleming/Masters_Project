from django.shortcuts import render

def index(request):

    context_dict = {'boldmessage': 'Bold message here'}

    return render(request, 'projectapp/index.html', context=context_dict)