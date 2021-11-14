"""todoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from main.views import*

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("test/", test, name="test"), 
    path("test2/", second),
    path("meeting/", meeting, name="meeting"),
    path("add-todo/", add_todo, name="add-todo"),
    path("add-tomeet/", add_tomeet, name="add-tomeet"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("mark-todo/<id>/", mark_todo, name="mark-todo"),
    path("unmark-todo/<id>/", unmark_todo, name="unmark-todo"),
    path("close-todo/<id>/", close_todo, name="close-todo"),
    path("delete-tomeet/<id>/", delete_tomeet, name="delete-tomeet"),
    path("marked-tomeet/<id>/", marked_tomeet, name="marked-tomeet"),
    path("unmark-tomeet/<id>/", unmark_tomeet, name="unmark-tomeet"),
    path("closed-tomeet/<id>/", closed_tomeet, name="closed-tomeet"),
    path("habit/", habit, name="habit"),
    path("add-habit/", add_habit, name="add-habit"),
    path("delete-habit/<id>/", delete_habit, name="delete-habit"),
    path("marked-habit/<id>/", marked_habit, name="marked-habit"),
    path("unmark-habit/<id>/", unmark_habit, name="unmark-habit"),
    path("closed-habit/<id>/", closed_habit, name="closed-habit"),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
