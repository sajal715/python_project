"""
URL configuration for sajal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post.views import post,list_post_view,add_post_view,CreatePostView, PostDetailView, DeletePostView,ListPostView


urlpatterns = [
    path('developers.admin/',admin.site.urls),
    path('admin/', admin.site.urls),
    path('manager.admin/',admin.site.urls),
    path('super.admin/',admin.site.urls),
    path('post/',post),
    path('list-post-view/',list_post_view, name="list-post"),
    path("add_post_view/",add_post_view, name="add-post"),
    path("create-post/",CreatePostView.as_view(), name="create-post"),
    path("post-details/<int:id>/", PostDetailView.as_view(), name="post-detail"),
    path('post/<int:id>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('list-post/', ListPostView.as_view(), name="list-posts"),
    path('auth/', include('authentication.urls')),
]
