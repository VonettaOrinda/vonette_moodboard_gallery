from email.mime import image
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Image)
admin.site.register(categories)
admin.site.register(Location)