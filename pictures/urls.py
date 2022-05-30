from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [

    path('',views.home,name = 'home'),
    path('',views.search_results, name='search_results'),
    path('image/<id>',views.get_image_by_id,name ='image'),
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
