from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'body',
        'author'
    ]

class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
        'body',
        'author'
    ]

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    

def PostDelRedirect(request,*args, **kwargs):
    return redirect('post_list')


# def PostDeleteView(request,*args,**kwargs):
#     # id = request.GET.get('pk')
#     id =1
#     # obj = Post.objects.get(id = id)
#     obj = get_object_or_404(Post, id)
#     print(obj)
#     if request.POST:
#         obj.delete()
#         redirect('/')
    
#     render(request,'post_confirm_delete.html',{"object":obj})