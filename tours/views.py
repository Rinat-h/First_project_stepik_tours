from random import randint

from django.http import HttpResponseServerError, Http404
from django.shortcuts import render

from tours import data


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера....Починим как только так сразу!')


def main_view(request):
    rand_list = {}
    for numb in range(1, 7):
        rand_number = randint(1, 14)
        rand_list['tour_' + str(numb)] = data.tours[rand_number]
        rand_list['tour_' + str(numb)].update({'id_tour': rand_number})
    rand_list.update({
        'index_title': data.title,
        'index_subtitle': data.subtitle,
        'index_description': data.description
    })
    return render(request, 'tours/index.html', rand_list)


def departure_view(request, departure):
    if departure in data.departures:
        departure_req = {}
        departure_req_price = []
        departure_req_nights = []
        tour_numb = 1
        for tour_id, tour_info in data.tours.items():
            if data.tours[tour_id]['departure'] == departure:
                departure_req.update({'tour_' + str(tour_numb): data.tours[tour_id]})
                departure_req['tour_' + str(tour_numb)].update({'id_tour': tour_id})
                departure_req_price.append(data.tours[tour_id]['price'])
                departure_req_nights.append(data.tours[tour_id]['nights'])
                tour_numb += 1
        departure_dict = {}
        departure_dict.update({
            'departure_req': departure_req,
            'quant': len(departure_req),
            'price_min': min(departure_req_price),
            'price_max': max(departure_req_price),
            'nights_min': min(departure_req_nights),
            'nights_max': max(departure_req_nights),
            'city': departure
        })
        return render(request, 'tours/departure.html', departure_dict)
    else:
        raise Http404


def tour_view(request, tour_id):
    if tour_id in data.tours:
        return render(request, 'tours/tour.html', data.tours[tour_id])
    else:
        raise Http404
