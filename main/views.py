from django.shortcuts import render

from main.models import Draw, Dance


def index(request):
    return render(request, 'main/index.html')


def dance(request):
    danceelements = Dance.objects.all()

    if request.method == "POST":  # Like button clicked
        item_id = request.POST.get("item_id")
        selected_element = Dance.objects.get(id=item_id)
        selected_element.likes = selected_element.likes + 1
        selected_element.save()

    return render(request, 'main/dance.html', dict(danceelements=danceelements))


def draw(request):
    drawelements = Draw.objects.all()

    if request.method == "POST":  # Like button clicked
        item_id = request.POST.get("item_id")
        selected_element = Draw.objects.get(id=item_id)
        selected_element.likes = selected_element.likes + 1
        selected_element.save()

    return render(request, 'main/draw.html', dict(drawelements=drawelements))


def video(request, pk):
    selected_element = Dance.objects.get(id=pk)

    if request.method == "POST":  # Like button clicked
        item_id = request.POST.get("item_id")
        selected_element = Dance.objects.get(id=item_id)
        selected_element.likes = selected_element.likes + 1
        selected_element.save()
    else:
        selected_element.views = selected_element.views + 1
        selected_element.save()

    return render(request, 'main/video.html', dict(selected_element=selected_element))
