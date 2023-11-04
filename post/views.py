from django.shortcuts import render
from .models import Posts
from .forms import PostForm

# Create your views here.
def posts(request):
    blog_posts = Posts.objects.all()
    context = {
        "blog_posts":blog_posts
    }
    return render(request, 'blog.html', context)

def post_details(request,id):
    post = Posts.objects.get(id=id)
    context = {
        "id":id,
        "blog_post":post
    }
    return render(request, 'blog_detail.html', context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})