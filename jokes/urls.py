from django.shortcuts import render
from django.urls import path


def jokes(request):
    return render(request, 'jokes.html')


urlpatterns = [
    path('', jokes, name='jokes'),
]
