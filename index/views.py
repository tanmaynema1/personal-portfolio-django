from django.shortcuts import render
from index.models import Contact

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
        
        print(name, email, phone, concern)
        
        obj = Contact(name = name, email = email, phone = phone, concern = concern)
        obj.save()
        
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')

def about(request):
    return render(request, 'about.html')