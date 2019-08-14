from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == 'GET':
        prize = "НЕО_ГУРЦЫ"
        # TODO: сделать много призов
        return render(request, 'index.html', {'prize': prize})

    if request.method == 'POST':

        email = request.POST.get('email', '')

        if email == '':
            return HttpResponse('Enter email')
        # TODO: сохранить данные в файл
        return redirect('/success')

def success(request):
    # TODO: сделать красивый шаблон
    return HttpResponse("I'am success")
