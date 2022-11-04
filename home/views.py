from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):

    blogsdata =Blog.objects.all()
    context = {"blogs":blogsdata}
    return render(request, "index.html", context=context)

