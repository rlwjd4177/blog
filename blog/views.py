from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.utils import timezone
from .forms import *
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    b_list = Blog.objects.all()
    paginator = Paginator(b_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'home.html',{'posts':posts})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    comments = Comment.objects.filter(blog_id = blog.id)
    return render(request, 'detail.html',{'blog':blog,'comments':comments})

def new(request):
    if request.method == 'POST' :
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pup_date = timezone.now()
            content.save()
            return redirect('home')

    else : 
        form = BlogForm()
        return render(request,'new.html',{'form':form})


def edit(request,blog_id):
    question = get_object_or_404(Blog, pk = blog_id)
    
    if request.method == 'POST' :
        form = BlogForm(request.POST, request.FILES, instance= question)
        if form.is_valid():
            content = form.save()
            return redirect('detail',blog_id)

    else :
        form = BlogForm(instance=question)
        return render(request,'edit.html',{'form':form})
        

# def update(request,blog_id):
#     update_blog=get_object_or_404(Blog, pk = blog_id)
#     update_blog.title= request.POST['title']
#     update_blog.pup_date = timezone.datetime.now()
#     update_blog.body = request.POST['body']
#     update_blog.save()
#     return redirect('detail', update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('home')

def comment_new(request,blog_id):
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.pup_date = timezone.now()
            content.user = request.user
            content.blog = get_object_or_404(Blog, pk=blog_id)
            content.save()
            return redirect('home')

    else : 
        form = CommentForm()
        return render(request,'new.html',{'form':form})




#{%url 'edit' question.id%}
#