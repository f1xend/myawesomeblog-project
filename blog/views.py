from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
import events.views


# Create your views here.
def showblog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': post})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            messages.error(request, "Account creation failed")

        return redirect("events:home")

    form = UserCreationForm()
    return render(request, "account/base.html", {"form": form})
