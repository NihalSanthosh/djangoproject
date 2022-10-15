from django.db import models

# Create your models here.
class Studentsid(models.Model):
    Sl_num=models.IntegerField()
    Name=models.CharField(max_length=20)
    Reg_num=models.IntegerField()
    Place=models.CharField(max_length=20)
    
class Negister(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class Gallery(models.Model):
    Image=models.ImageField(upload_to='media/',null=True,blank=True)
    Name=models.CharField(max_length=10)