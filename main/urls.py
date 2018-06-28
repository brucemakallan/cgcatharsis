from django.urls import path, include

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dance', views.dance, name='dance'),
    path('draw', views.draw, name='draw'),
    path('build', views.build, name='build'),
    path('contact', views.contact, name='contact'),
]