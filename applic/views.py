import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *


def rsa_view(request):

    return render(request, 'rsa.html')

def elgamal_view(request):

    return render(request, 'elgamal.html')

def rabin_view(request):

    return render(request, 'rabin.html')


@csrf_exempt
def send(request):
    '''Обработка запроса на шифрование по Эль-Гамаля'''
    params = json.loads(request.body.decode("utf-8"))
    bitsize, M = int(params['bitsize']), params['mess']

    cipher = EL_Gamal(bitsize)
    x,y = cipher.public_key()
    (C_ , C__ ), R = cipher.encrypt(M,y)
    Z,Z_inv,M_ = cipher.decrypt(C_,C__,x)
    return JsonResponse({
        'message': {'p': str(cipher.p), 'g':str(cipher.g), \
                    'x': str(x), 'y': str(y), "C'":str(C_), "C''":str(C__), \
                    "R":str(R),"Z":str(Z), "Z'":str(Z_inv),"M'":M_.decode('utf-8')}
    }, safe=False)

@csrf_exempt
def rsasend(request):
    '''Обработка запроса на шифрование по RSA'''
    params = json.loads(request.body.decode("utf-8"))
    bitsize, M = int(params['bitsize']), params['mess']

    cipher = RSA(bitsize)
    print()
    C = cipher.encrypt(M)
    M_ = cipher.decrypt(C)
    return JsonResponse({
        'message': {'p':str(cipher.p), 'q':str(cipher.q), 'n':str(cipher.n),\
                    'phi':str(cipher.phi), 'e':str(cipher.e), 'd':str(cipher.d),
                    'C (hex)': str(hex(C).split('x')[-1]), "M'":M_.decode('utf-8')}
    }, safe=False)

@csrf_exempt
def rsasign(request):
    '''Обработка запроса на подпись по RSA'''
    params = json.loads(request.body.decode("utf-8"))
    bitsize, M = int(params['bitsize']), params['mess']

    cipher = EDS_RSA(bitsize)
    S = cipher.sign(M)
    ans = cipher.verify(S,M)

    return JsonResponse({
        'message': {'Подпись': f'{M} - ({S})', "Проверка":ans}
    }, safe=False)

@csrf_exempt
def rabinsend(request):
    '''Обработка запроса на шифрование по Рабину'''
    params = json.loads(request.body.decode("utf-8"))
    bitsize, M = int(params['bitsize']), params['mess']

    cipher = Rabin(bitsize)
    C = cipher.encrypt(M)
    mp1,mq1,mp2,mq2,a,b,M_ = cipher.decrypt(C)
    M__ = [i for i in M_ if i[:4] == b"Mes:"][0][4:].decode('utf-8')
    return JsonResponse({
        'message': {'p':str(cipher.p), 'q':str(cipher.q), 'n':str(cipher.n), \
                    'mp1':str(mp1), 'mq1':str(mq1), 'mp2':str(mp2), \
                    'mq2':str(mq2), 'a':str(a), 'b':str(b),\
                    'C (hex)': str(hex(C).split('x')[-1]), "M'":M__}
    }, safe=False)