from django.http import HttpResponse
from .models import Category , Photo
from django.shortcuts import render , redirect

# Create your views here.

def home(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)

    categories = Category.objects.all()
    return render(request,"photos/gallery.html",{"categories":categories,"photos":photos})

def viewphoto(request , pk):

    photo = Photo.objects.get(id=pk)

    return render(request,"photos/photo.html",{'photo':photo})


def addphoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get("image")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data['category_new'] != "" :
            category, created = Category.objects.get_or_create(name=data["category-new"])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )

        return redirect("home")

    return render(request,"photos/add.html",{"categories":categories})