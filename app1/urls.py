from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('posts/', views.blog_list),
    path('posts/<id>', views.blog_detail),

    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_details')

    
]