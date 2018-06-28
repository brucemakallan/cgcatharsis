from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def dance(request):
    return render(request, 'main/dance.html')


def draw(request):
    return render(request, 'main/draw.html')


def build(request):
    return render(request, 'main/build.html')


def contact(request):
    return render(request, 'main/contact.html')