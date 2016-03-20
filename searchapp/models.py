from django.db import models

# Create your models here.
class linkmodel(models.Model):
	linkid = models.CharField(max_length=50)
	linkurl = models.CharField(max_length=200)
	  
class imagesmodel(models.Model):
	linkid  = models.CharField(max_length=50)
	imageurl = models.CharField(max_length=200)
