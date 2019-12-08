from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse 

import json
import cv2
from ID_OCR import binarizing,depoint,all_OCR
from StringIO import StringIO
from PIL import Image
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

def extract_ocr(request):
    res = []
    if request.method == 'POST':
        imgstr = request.POST['img']
        tempimg = StringIO(imgstr.decode('base64'))
        im = Image.open(tempimg)
        open_cv_image = numpy.array(im) 

        # Convert RGB to BGR 
        image = open_cv_image[:, :, ::-1].copy() 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        pil_image = Image.fromarray(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
        text = pytesseract.image_to_string(Image.open(filename), lang='chi_tra')
        res.append(text)

    return JsonResponse(ls,json_dumps_params={'ensure_ascii':False},safe=False)