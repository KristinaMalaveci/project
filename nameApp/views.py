from django.shortcuts import render
from.models import *

# Create your views here.
def home (request):
    staffs= Staff.objects.all()
    context = {"allStaff":staffs}
    return render(request, 'home.html', context)
  

def about(request):
    staffs= Staff.objects.all()
    context = {"allStaff":staffs}
    return render(request, 'about.html', context)

def profile(request, id):
    staff= Staff.objects.get(pk=id)
    context={"profile":staff}
    return render(request, 'profile.html', context)

def contact(request):
    return render(request, 'contact.html')

