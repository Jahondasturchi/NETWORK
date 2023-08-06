from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Profile,Post
from .forms import PostForm
# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('accounts/login')
    else:
        if request.method == "POST":
            form = PostForm(request.POST or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("app1:dashboard")
        followed_dweets = Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
        form = PostForm()
        return render(request, "app1/dashboard.html", {'form':form, "dweets": followed_dweets})

def allprofiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'app1/allprofiles.html',{'profiles':profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "app1/profile.html", {"profile": profile})