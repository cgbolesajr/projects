from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm






def homePage(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html',{'posts':posts})

def aboutPage(request):
    return render(request, 'blogapp/about.html',{})


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =  post
            comment.save()
            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blogapp/detail.html',{'post':post, 'form':form})
