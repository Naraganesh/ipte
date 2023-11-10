from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def kkr(request):
    return render(request,'kkr.html')
def chinna(request):
    return HttpResponse ('<h1><marquee> </marquee></h1>')