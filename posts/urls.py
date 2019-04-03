from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDelRedirect
)

urlpatterns = [
    path('',PostListView.as_view(), name = 'post_list'),
    path('post/<int:pk>/detail/',PostDetailView.as_view(), name = 'post_detail'),
    path('post/create/',PostCreateView.as_view(), name = 'post_create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:int>/delete/Post', PostDelRedirect)
]