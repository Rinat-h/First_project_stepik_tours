from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, проект еще в доработке')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера....Починим как только так сразу!')


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')
