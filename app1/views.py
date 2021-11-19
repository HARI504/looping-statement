from django.shortcuts import render


def looping(request):
    d={'a': 100,'b':101,'c':99,'name':'Tarun'}
    return render(request,'h1.html',d)

# Create your views here.
