from django.db import models

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.category_title}"
    

class Staff (models.Model):
    staff_name = models.CharField(max_length=200, null=True, blank=True)
    staff_surname = models.CharField(max_length=200, null=True, blank=True)
    staff_position = models.CharField(max_length=200, null=True, blank=True)
    staff_email = models.EmailField(max_length=200, null=True, blank=True)
    staff_image = models.ImageField(upload_to='staff/', null=True, blank=True)
    staff_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.staff_name} {self.staff_surname}"
    
class Contact(models.Model):
    contact_name = models.CharField(max_length = 30, null=True, blank=True)  
    contact_surname = models.CharField(max_length = 30, null=True, blank=True)  
    contact_email = models.EmailField(max_length = 100, null=True, blank=True)   
    contact_comment = models.TextField(max_length = 1000, null=True, blank=True) 

    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"