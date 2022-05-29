from django.shortcuts import redirect, render
from django.http  import HttpResponse

from mygallery.models import ImageModel
# Create your views here.
def index(request):
    photos =   ImageModel.objects.all()
    categories = []
    locations =[];
    for item in photos:
        categories.append(item.category.name)
        locations.append(item.location.name) 

    return  render(request,'index.html', {"photos":photos, "categories":list(set(categories)), "locations":list(set(locations))}, )


def image_details(request,id):
    photo = ImageModel.objects.get(pk=id)
    return  render(request, "single.html",{"photo":photo})


def view_category(request,category):
    photos =   ImageModel.objects.filter(category__name=category)
  
    return  render(request,'category.html', {"photos":photos})

def view_location(request,location):
    photos =   ImageModel.objects.filter(location__name=location)
  
    return  render(request,'location.html', {"photos":photos})

def search_photo(request):
    text =request.POST["search_text"]
    if(text==""):
        return redirect('home')

    photos =   ImageModel.objects.filter(name__icontains=text,description__icontains=text,)
  
    return  render(request,'location.html', {"photos":photos})