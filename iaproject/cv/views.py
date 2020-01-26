from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    #return HttpResponse('CV')
    return render(request, 'cv/about.html')   


def contact(request):
    #return HttpResponse('CV')
    return render(request, 'cv/contact.html')   
  

