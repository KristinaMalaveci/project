from django.db import models

# Create your models here.

class Staff (models.Model):
    staff_name = models.CharField(max_length=200, null=True, blank=True)
    staff_surname = models.CharField(max_length=200, null=True, blank=True)
    staff_position = models.CharField(max_length=200, null=True, blank=True)
    staff_email = models.EmailField(max_length=200, null=True, blank=True)
    staff_image = models.ImageField(upload_to='staff/', null=True, blank=True)

    def __str__(self):
        return f"{self.staff_name} {self.staff_surname}"