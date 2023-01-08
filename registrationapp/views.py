from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Create your views here.
def show_reg_form(request):
    context={}
    # якщо тип запиту є POST (тобто користувач надіслав форму)
    if request.method == "POST":
        # записуємо данні з форми в змінні
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # записуємо данні зі змінних в контекст щоб потім видати користовачу не 
        # пусту форму, а форму з раніше заповненими данними
        context = {
            'password':password,
            'password_confirm':password_confirm,
            'username':username,
        }
        # якщо повторення паролю співпадає з паролем
        if password == password_confirm:
            # якщо немає помилок при введенні данних
            try:
                # створюємо користувача в БД
                User.objects.create_user(username = username, password = password)
                # перенаправляє на сторінку "Реєстрація успішна"
                return redirect("reg_success")
            # якщо користувач вже існує у БД
            except IntegrityError:
                # передає в контекст текст помилки
                context['error_text']= 'Такий користувач вже існує!'
        else:
            # передає в контекст текст помилки
            context['error_text']= 'Паролі не співпадають!'

    return render(request,'registrationapp/reg_form.html', context)
    
     
def show_reg_success(request):
    return render(request,'registrationapp/reg_success.html')