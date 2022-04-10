from django.shortcuts import render
from django.urls import path


def graph(request):
    return render(request, 'base.html', context={'text': 'hello world'})


urlpatterns = [
    path('', graph, name='graph'),
]
