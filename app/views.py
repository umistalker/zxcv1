import json

from django.shortcuts import render
from .models import Model
from django.http import HttpRequest


def get_data_view(request):
    if request.method == "GET":
        data = json.dumps(request.GET)
        print(type(data))
        Model.objects.get_or_create(
            text=data
        )

        return render(request, 'index.html')


def show_data_view(request):
    if request.method == "GET":
        data = Model.objects.values_list()
        query_set = {'data': data}
        return render(request, 'data.html', context=query_set)
