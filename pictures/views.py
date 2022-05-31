from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from.models import*
# from .models import Image, Location, categories
from django.core.exceptions import ObjectDoesNotExist
 


# Create your views here.
def home(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = categories.objects.all()


    return render(request,"all-pictures/pictures.html",{"images":images,"location":location,"category":category})

def search_results(request):

    if 'categories' in request.GET and request.GET['categories']:
        search_images = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"pictures.html", {"image":image})