from django.shortcuts import render
from django.urls import path


# Create your views here.

def integers(request):
    return render(request, 'integers.html', context={'text': 'Hello World'})


urlpatterns = [
    path('', integers, name='integers')
]
