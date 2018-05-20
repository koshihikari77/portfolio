
from django.urls import path
from . import views

urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
]