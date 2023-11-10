from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rr(request):
    return render (request,'rr.html')
def ganesh(request):
    return HttpResponse ('<h1><marquee>chinna </marquee></h1>')