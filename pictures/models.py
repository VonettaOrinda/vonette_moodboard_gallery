from django.db import models
import datetime as dt
from django.contrib.auth.models import User



# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    gallery_image = models.ImageField(upload_to='uploads/')
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        categories = cls.objects.filter(categories=cat)
        return categories