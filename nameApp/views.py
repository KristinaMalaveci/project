from django.shortcuts import render
from.models import *
from django.contrib import messages

# Create your views here.
def home (request):
    staffs= Staff.objects.all()
    categories = Category.objects.all()
    context = {"allStaff":staffs, "infoCategories":categories}
    return render(request, 'home.html', context)
  

def about(request):
    staffs= Staff.objects.all()
    categories = Category.objects.all()
    contacts = Contact.objects.all()
    context = {"allStaff":staffs, "infoContact":contacts, "infoCategories":categories}
    return render(request, 'about.html', context)

def profile(request, id):
    staff= Staff.objects.get(pk=id)
    categories = Category.objects.all()
    context={"profile":staff, "infoCategories":categories}
    return render(request, 'profile.html', context)

def contact(request):
    categories = Category.objects.all()
    context={"infoCategories":categories}
    if request.method == "POST":
        #marrja e inf nga inputi

        name_contact = request.POST['nameField']
        surname_contact = request.POST['lastField']
        email_contact = request.POST['emailField']
        comment_contact = request.POST['messageField']
        if name_contact != "" and surname_contact != "" and email_contact != "" and comment_contact != "":
                

            #ruajtje tek modeli

                Contact(contact_name=name_contact,
                        contact_surname=surname_contact,
                        contact_email=email_contact,
                        contact_comment=comment_contact
                        ).save()
                messages.success(request, "Message Sended!")
        else:
                messages.error(request, "Message not Sended! Fill all the fields!")    
    return render(request, 'contact.html', context)

def categoryInfo(request, id):
     categories = Category.objects.all()
     category = Category.objects.get(pk = id)
     elementeCategory = Staff.objects.filter(staff_category=category)
     context={ "infoCategories":categories, "detailCategory":category, "elementeCategory":elementeCategory}
     return render(request,"category.html", context)
