from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
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
    return render(request, 'detail.html',{'blog':blog})

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
    edit_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog=get_object_or_404(Blog, pk = blog_id)
    update_blog.title= request.POST['title']
    update_blog.pup_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request,blog_id):
    delete_blog = get_object_or_404(Blog, pk = blog_id)
    delete_blog.delete()
    return redirect('home')


#{%url 'edit' question.id%}
#