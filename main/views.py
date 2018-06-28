from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def dance(request):
    return render(request, 'main/dance.html')


def draw(request):
    return render(request, 'main/draw.html')
