from django.shortcuts import render
from datetime import date
from .models import Article

def home(request):
    articles = Article.objects.all()  
    context = {
        "title": "Bienvenue sur notre site !",
        "welcome_message": "Ceci est un site dynamique avec Django.",
        "articles": articles,
        "year": date.today().year,
    }
    return render(request, 'home.html', context)

