from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name="homePage"),
    path('about/', views.about, name="aboutPage"),
    path('contact/', views.contact, name="contactPage"),
    path('profilePage/<id>', views.profile,name="profilePage"),
    path('categoryPage/<id>', views.categoryInfo,name="categoryPage")
]
