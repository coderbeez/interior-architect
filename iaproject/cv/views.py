from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cv(request):
    #return HttpResponse('CV')
    return render(request, 'cv/cv.html')   
