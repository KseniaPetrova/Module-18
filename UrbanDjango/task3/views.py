from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def webpage_homepage(request):
    title = "Добро пожаловать в Steam"
    text = 'Какой-то рандосный текст из переменной в mysite/app/views.py'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, "third_task/homepage.html", context)

def webpage_store(request):
    return render(request, "third_task/store.html")

def webpage_cart(request):
    return render(request, "third_task/cart.html")

