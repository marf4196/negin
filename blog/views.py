from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return HttpResponse('<h1>HEY</h1>')