from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    # Переконайтеся, що назва (name) співпадає з тою, що в шаблоні:
    path('author/<str:author_name>/', views.author_articles, name='author_articles'),
]