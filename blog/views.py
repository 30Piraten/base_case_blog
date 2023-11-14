from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

# Create your views here.


class Content(ListView):
    model = Post
    template_name = "home.html"


class ContentDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class CreateContent(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "author", "body"]


class UpdateContent(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ["title", "body"]
