from wsgiref.simple_server import demo_app
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"data":"Welcome to SELCO SCORDS - SELCO SCORDS Uygulamasına Tekrar Hoşgeldiniz"}
    return render(request,'demoapp/index.html', context)
