from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.

from .models import *
from .forms import *

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
         form=TaskForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/')
    
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update_task.html',context)


def deleteTask(request,pk):
    items=Task.objects.get(id=pk)
    if(request.method=='POST'):
        items.delete()
        return redirect('/')
    context={'item':items}
    return render(request,'delete.html',context)