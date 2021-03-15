from django.db import models

# Create your models here.
class Elements(models.Model):
    imgf=models.ImageField()
    xmlf=models.FileField()
class Details(models.Model):
    picname=models.CharField(max_length=350)
    objectname=models.CharField(max_length=150)
    xmin=models.IntegerField()
    ymin=models.IntegerField()
    xmax=models.IntegerField()
    ymax=models.IntegerField()
    timestamp=models.DateField(auto_now_add=True)