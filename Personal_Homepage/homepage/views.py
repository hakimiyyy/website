from asyncio import QueueFull
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .models import User, Item

# Create your views here.
def homepage (request):
    data=User.objects.all()
    return render (request, "lost/homepage.html")

# METHOD POST
def log_in (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = authenticate(request, username=username, password=password)
        data=User.objects.all()
        for m in data:
            if username == m.username:
                if password == m.password:
                    dict = {
                        'message':'Hello and Welcome to KPMB Lost and Found!'
                    }
                    return render (request, "lost/homepage.html",dict)
                else:
                    dict={
                        'message':'INVALID PASSWORD OR ID'
                    }
                    return render (request, "lost/log_in.html", dict)
    else:
        return render (request, "lost/log_in.html")
                

def reporteditems (request):
    items = Item.objects.all()  # Retrieve all items from the database
    context = {'items': items}  # Create a context dictionary with the items
    
    return render(request, 'lost/reporteditems.html', context)

# METHOD POST
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = User(username=username, full_name=full_name, email=email, password=password)
        data.save()
        dict = {
            'message': 'You are registered.'
        }
        return render(request, "lost/signup.html", dict)
    else:
        dict = {
            'message': ''
        }
        return render(request, "lost/signup.html", dict)


def lostitem (request):
    return render(request, "lost/lostitem.html")


# METHOD PUT/UPDATE
def update(request):
    if request.method=='POST':
        item_id=request.POST['item_id']
        description=request.POST['description']
        Item.objects.filter(item_name=item_id).update(description=description)
        list1 = Item.objects.filter(Q(item_id=item_id))
        return render(request, 'lost/update.html', {'menu':list1})
    else:
        return render(request,'lost/update.html')

# METHOD GET
def profile (request):
    username=request.GET.get('search')
    data = User.objects.filter(Q(username=username))
    return render(request, 'lost/profile.html', {'data':data})

# METHOD DELETE
def delete (request, username):
    data = User.objects.get(username=username)
    data.delete()
    return HttpResponseRedirect(reverse("profile"))
    



def inputitem (request):
    return render(request, "lost/inputitem.html")


# POST METHOD
def inputitem(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')

        item = Item(item_name=item_name, description=description)
        item.save()

        return redirect('lost/inputitem') 

    return render(request, 'lost/inputitem.html')