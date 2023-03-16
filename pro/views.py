from django.shortcuts import render

# Create your views here.

def python(request):
    d={'a':20,'b':10,'c':5}
    return render(request,'python.html',context=d)

def loop(request):
    d={'name':'paddhu'}
    return render(request,'loop.html',d)