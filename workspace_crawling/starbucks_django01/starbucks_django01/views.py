from django.shortcuts import render
from django.http import JsonResponse
from . import starbuck02


def index(request):
    return render(request, 'index.html')

def starbucks(request):
    list_all = list()

    sido_all = starbuck02.getSiDo()
    for sido in sido_all:
        if sido == '17':
            result = starbuck02.getStore(sido_code=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = starbuck02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbuck02.getStore(gugun_code=gugun)
                print(result)
                list_all.extend(result)

    result_dict = dict()
    result_dict['list'] = list_all

    return JsonResponse(result_dict)