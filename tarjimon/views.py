from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat


def index(request):
    """views bolimida sahifada nima chiqishi yoziladi va unda malumot olish va jonatish mumkin"""
    #soz = request.GET.get(input name ni yoziladi)
    """son = int(request.GET.get(son))
    nat = son * son"""
    #soz = request.GET.get('q', '')
"""    if soz and soz != '':
        natija = Lugat.objects.filter(inglizcha=soz).all()
        for data in natija:
            result = natija.inglizcha
            result2 = natija.uzbekcha"""
    return render(request, 'index.html', {#'key':soz, 'r1':result, 'r2':result2})
