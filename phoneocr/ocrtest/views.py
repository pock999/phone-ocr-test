from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse 
import json

from ID_OCR import binarizing,depoint,all_OCR
from io import StringIO
# Create your views here.

def index(request):
    return render(request, 'test.html', {})


def ocr_res(request):
    res = []
    if request.method == 'POST':
        imgstr = request.POST['img']
        tempimg = StringIO(imgstr.decode('base64'))
        im = Image.open(tempimg)
        res.append(all_OCR(im))
    return JsonResponse(ls,json_dumps_params={'ensure_ascii':False},safe=False)