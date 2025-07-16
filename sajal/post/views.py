from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView,ListView
from post.forms import PostForm
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def post(request):
    return HttpResponse("Hello World")

def list_post_view(request):
    posts = Post.objects.all()
    return render(
        request,
        "post/list.html",
        
        context={
            "all_posts" : posts,
        }
    )

def add_post_view(request):
    context = {
        "author": User.objects.all(),
    }
    return render(request, template_name="post/form.html", context=context)

class CreatePostView(CreateView):
    template_name = "post/form.html"
    form_class = PostForm
    success_url = reverse_lazy("list-post") 

class PostDetailView(DetailView):
    model = Post
    template_name = "post/details.html"
    pk_url_kwarg = "id"

class DeletePostView(DeleteView):
    model = Post
    template_name = "post/delete_confirm.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list-post")

class ListPostView(LoginRequiredMixin,ListView):
    template_name = "post/list.html"
    # queryset = Post.objects.all() # This can be used to get all posts
    context_object_name = "all_posts"

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author=user)
        return posts