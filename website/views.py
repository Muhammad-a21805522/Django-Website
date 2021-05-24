from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import datetime

# Create your views here.
def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)


def intro_page_view(request):
    return render(request, 'website/intro.html')

def multi_page_view(request):
    return render(request, 'website/multi.html')