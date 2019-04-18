from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category, Profile
from .forms import  ProfileForm,NewProjectForm
from django.contrib.auth.models import User

def shops(request):
    all_pics = Image.all_pics()
    print(all_pics)
    return render(request, 'shops.html',{"pics":all_pics})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})

def display_images_categories(request):    
    pics = Image.pic_categories()

    return render(request, 'category.html', {"pics":pics})

def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.all()
   
    return render(request,'profile.html',{"user":user, "profiles":profiles})


def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('shops')

    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form})

def new_project(request):
    
        current_user = request.user
        title = 'New project'
        if request.method == 'POST':
            form = NewProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = current_user
                project.save()
            return redirect('shops')

        else:
            form = NewProjectForm()
        return render(request, 'new_project.html', {"form": form,"current_user":current_user,"title":title})