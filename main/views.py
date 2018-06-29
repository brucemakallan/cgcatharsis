from django.shortcuts import render
from django.views import generic

from main.models import Draw


def index(request):
    return render(request, 'main/index.html')


def dance(request):
    return render(request, 'main/dance.html')


class DrawListView(generic.ListView):
    model = Draw
    context_object_name = "drawelements"
    template_name = 'main/draw.html'
