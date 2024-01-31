from django.contrib import admin
from django.urls import path, include
from main.admin import mainadmin

urlpatterns = [
    path('admin/', mainadmin.urls),
    path('', include("main.urls"))
]
