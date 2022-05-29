from django.shortcuts import render
from django.http  import HttpResponse

from mygallery.models import ImageModel
# Create your views here.
def index(request):
    photos =   ImageModel.objects.all()
    return  render(request,'index.html', {"photos":photos})


def image_details(request,id):
    photo = ImageModel.objects.get(pk=id)
    return  render(request, "single.html",{"photo":photo})