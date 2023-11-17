from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhotoForm
from .models import Photo

def index(request):
    return HttpResponse("Image")


def UploadImage(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The image saved successfully')
    else:
        form = PhotoForm()
    context = {
            'form':form,
        }
    return render(request, 'image_upload/photo_form.html', context)


def photo_list(request):
    lists = Photo.objects.all()
    context = {'lists':lists}
    return render(request, 'image_upload/photo_list.html', context)


def photo_detail(request, id):
    photo = Photo.objects.get(pk=id)
    context = {'photo':photo}
    return render(request, 'image_upload/photo_detail.html', context)