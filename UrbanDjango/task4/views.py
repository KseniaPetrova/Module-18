from django.shortcuts import render

# Create your views here.
def webpage_homepage(request):
    title = "Добро пожаловать в Steam"
    text = 'Какой-то рандосный текст из переменной в mysite/app/views.py'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, "fourth_task/homepage.html", context)

def webpage_store(request):
    games = ["Assassin's Creed", "Baldur's Gate 3", "Space Engineers"]
    context = {
        'games': games,
    }
    return render(request, "fourth_task/store.html", context)

def webpage_cart(request):
    return render(request, "fourth_task/cart.html")