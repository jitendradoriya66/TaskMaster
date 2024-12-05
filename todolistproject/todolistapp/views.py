from django.shortcuts import render,redirect
from todolistapp.models import *


# Create your views here.
def create(request):
    if request.POST:
        name=request.POST['task']
        print(name)
        uid=task.objects.filter(name=name).exists()
        if uid:
            return redirect(home)
        else:
            task.objects.create(name=name)
            return redirect(home)
            
           
            

def home(request):
    data=task.objects.all().order_by('-id')
    contaxt={
            'data':data
            }
    return render(request,'home.html',contaxt)

def update(request,id):
   if request.POST:
        name=request.POST['task_name']
        uid=task.objects.get(id=id)
        uid.name=name
        uid.save()
      
        return redirect(home)
   return render(request,'update.html')
    
def check(request,id):
    print(id)
    cid=task.objects.get(id=id)
    if cid.complete == False:
        cid.complete=True
        cid.save()
        return redirect(home)
    else:
        cid.complete=False
        cid.save()
        return redirect(home)
        
        
def delete_task(request,id):
    d=task.objects.get(id=id)
    d.delete()
    return redirect(home)
