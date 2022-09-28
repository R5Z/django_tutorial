from django.shortcuts import render, redirect
import random
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [{"name":'poke',"price":10000}, {"name":'bibimbob',"price":9000}, {"name":'gimbob',"price":5000}, {"name":'sushi',"price":15000}]
    pick = random.choice(menus)
    articles = Article.objects.order_by('-pk')
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()

    return redirect('/articles/dinner/<str:name>/')