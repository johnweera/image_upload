from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.UploadImage, name='add'),
    path('list/', views.photo_list, name='list'),
    path('list/<int:id>/', views.photo_detail, name='detail'),
]