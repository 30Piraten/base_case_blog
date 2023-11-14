from django.urls import path
from .views import (
    Content, ContentDetail, CreateContent, UpdateContent
)

urlpatterns = [
    path("post/<int:pk>/edit/", UpdateContent.as_view(), name="edit_post"),
    path("post/new/", CreateContent.as_view(), name="new_post"),
    path("post/<int:pk>/", ContentDetail.as_view(), name="post_detail"),
    path("", Content.as_view(), name="home"),
]
