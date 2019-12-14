from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from app.settings import BUS_STATION_CSV
from urllib.parse import urlencode
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(BUS_STATION_CSV, 'r', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = list(data)
        data_list.pop(0)
        bus_stations_full_list = []
        for i in data_list:
            bus_stations_full_list.append({'Name': i[1], 'Street': i[4], 'District': i[6]})
        bus_stations_paginator = Paginator(bus_stations_full_list, 10)
        current_page = request.GET.get('page', 1)
        bus_stations_list = bus_stations_paginator.get_page(current_page)
        context = {
            'bus_stations': bus_stations_list,
            'current_page': bus_stations_list.number
        }
        if bus_stations_list.has_previous():
            prev_page_num = bus_stations_list.previous_page_number()
            prev_page = {'page': prev_page_num}
            prev_page_url = f'?{urlencode(prev_page)}'
            context['prev_page_url'] = prev_page_url
        if bus_stations_list.has_next():
            next_page_num = bus_stations_list.next_page_number()
            next_page = {'page': next_page_num}
            next_page_url = f'?{urlencode(next_page)}'
            context['next_page_url'] = next_page_url

    return render_to_response('index.html', context)
