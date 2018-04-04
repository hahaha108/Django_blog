from django.shortcuts import render

# Create your views here.


def index(request):
    tpl_name = 'index.html'
    return render(request,tpl_name)

def detail(request):
    pass