from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm
from django.contrib.auth.models import User
from .forms import Post, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.all_posts()
    json_posts = []
    for post in posts:

        # import pdb; pdb.set_trace()
        pic = Profile.objects.filter(user=post.user.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic =''
        obj = dict(
            image=post.image.url,
            author=post.user.username,
            avatar=pic,
            name=post.title,
            caption=post.caption
            # likes = post.likes

        )
        json_posts.append(obj)
    return render(request, 'home.html', {"posts": json_posts})


def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', context)

def update_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'update_profile.html', context)



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})









# def likes(request):
#     postLike_id = None
#     if requst.method == "GET":
#         postLike = Post.objects.get(id = int(postLike_id))
#         if postLike:
#             likes = postLike.likes + 1
#             postLike.likes = likes
#             postLike.save()
#     return HttpResponse(likes)
        