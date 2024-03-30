from django.shortcuts import render,  get_object_or_404, redirect
from .models import Article


def index(request):
    articles = Article.objects.filter(main_article=True)
    context = {"articles": articles}
    return render(request, 'index.html', context)

def articles(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles.html', context)

def about(request):
    return render(request, 'about_us.html')

def detail(request, id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    context = {"article": article}
    return render(request, 'detail.html', context)

def refund(request):
    return render(request, 'refund.html')

def privacy(request):
    return render(request, 'privacy.html')
