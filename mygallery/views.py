from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def index(request):
    return  render(request,'index.html', {"photos":[1,2,3,4,5]})


def image_details(request,id):
    return  render(request, "single.html")