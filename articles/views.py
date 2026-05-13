from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'articles/list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})
def author_articles(request, author_name):
    # ORM запит: фільтруємо за полем author
    articles = Article.objects.filter(author=author_name).order_by('-published_date')
    return render(request, 'articles/list.html', {
        'articles': articles, 
        'author_filter': author_name
    })
def author_filter(request, author_name):
    # Фільтрація ORM за конкретним автором (Завдання 2)
    articles = Article.objects.filter(author=author_name)
    return render(request, 'articles/list.html', {
        'articles': articles, 
        'author_mode': author_name
    })