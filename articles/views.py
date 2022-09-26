from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [{"name":'poke',"price":10000}, {"name":'bibimbob',"price":9000}, {"name":'gimbob',"price":5000}, {"name":'sushi',"price":15000}]
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
    }

    return render(request, 'dinner.html', context)