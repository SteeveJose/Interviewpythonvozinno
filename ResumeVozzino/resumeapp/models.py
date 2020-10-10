from django.db import models

class personaldetails(models.Model):
    Email=models.CharField(max_length=100,unique=True)
    Password=models.CharField(max_length=120)
    Full_Name=models.CharField(max_length=100)
    Date_of_birth=models.CharField(max_length=15)
    lastdegree=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")


    def __str__(self):
        return self.Full_Name
