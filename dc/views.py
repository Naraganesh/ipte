from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def dc(requst):
    return render(request,'dc.html')


def dcr(request):
    return HttpResponse ('<h1><marquee> pant</marquee></h1>')