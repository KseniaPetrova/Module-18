from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

users = ['Камила', 'Артем', 'УбийцаБогов']

def sign_up_by_django(request):
    info = {}
    form = UserRegister()

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f"Приветствуем, {username}!"
                users.append(username)
        else:
            info['error'] = 'Пожалуйста, исправьте ошибки в форме.'

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age_str = request.POST.get('age')

        try:
            age = int(age_str)
        except ValueError:
            info['error'] = 'Введите корректный возраст.'
            return render(request, 'fifth_task/registration_page.html', info)

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['message'] = f"Приветствуем, {username}!"
            users.append(username)  # Добавляем пользователя в список

    return render(request, 'fifth_task/registration_page.html', info)

