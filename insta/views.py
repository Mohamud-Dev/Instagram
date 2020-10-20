from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm
from django.contrib.auth.models import User
from .forms import Post, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def home(request):
    posts = Post.all_posts()
    json_posts = []
    for post in posts:

        # import pdb; pdb.set_trace()
        pic = Profile.objects.filter(user=post.user.id).first()
        pic = pic.profile_pic.url
        obj = dict(
            image=post.image.url,
            author=post.user.username,
            avatar=pic,
            name=post.title,
            caption=post.caption

        )
        json_posts.append(obj)
    return render(request, 'home.html', {"posts": json_posts})


def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', context)


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
    # current_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            # image.profile = current_profile
            image.save()
            # print(current_profile)
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
