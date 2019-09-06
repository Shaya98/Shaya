from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name= models.CharField(max_length=100,default="ABC")
    email= models.EmailField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
