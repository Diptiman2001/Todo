from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            TO = todo(title=title, desc=desc)
            TO.save()
            request.method='GET'
    alltodos = todo.objects.all()
    d = {'alltodos':alltodos}
    return render(request, 'index.html', d)
sno=0
def update(request):
    if request.method =='GET':
        sno=request.GET.get('pk')
        TO = todo.objects.get(sno=sno)
        d={'TO':TO}
        return render(request,'update.html',d)
    elif request.method =='POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO=todo.objects.filter(sno=sno)
        TO.update(title=title , desc=desc)
        alltodos = todo.objects.all()
        d = {'alltodos':alltodos}
        return render(request, 'index.html', d)

def delete(request):
    if request.method =='GET':
        sno=request.GET.get('pk')
        TO = todo.objects.get(sno=sno)
        TO.delete()

        alltodos = todo.objects.all()
        d = {'alltodos':alltodos}
        return render(request, 'index.html', d)
        