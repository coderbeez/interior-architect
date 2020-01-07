from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def portfolio(request):
    #return HttpResponse('Portfolio List')
    return render(request, 'portfolio/portfolio.html')   
