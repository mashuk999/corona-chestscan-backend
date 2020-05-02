from django.shortcuts import render
from fastai.vision import *
from fastai.utils.mem import *
from fastai.callbacks.hooks import *
import os
import urllib.request
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import io
from . import models,serializer
from django.core.files import File

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        imageurl = request.POST['imageurl']
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(BASE_DIR,'model/')
        learn = load_learner(path, 'exported.pkl')
        urllib.request.urlretrieve(imageurl, './image.jpg')
        img = open_image('./image.jpg')
        pred_class,pred_idx,outputs = learn.predict(img)
        return render(request,'index.html',{'datapredicted':pred_class,'predidx':pred_idx,'outputs':outputs})
    else:
        return render(request,'form.html')

@api_view(['GET', 'POST'])
def getClientResponse(request):
    if request.method == 'POST':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(BASE_DIR,'model/')
        learn = load_learner(path, 'exported.pkl')

        print(request.FILES)

        uploadedFile = request.FILES["photo"]
        model_file = File(uploadedFile)
        model_file.save(('./'+uploadedFile.name), f.readlines(), true)
        img = open_image('./'+uploadedFile.name)
        pred_class,pred_idx,outputs = learn.predict(img)
        print(pred_class)
        dataRes = models.ResponseModel(category="norma;",confidence='100')
        ser = serializer.ResponseSerializer(dataRes)
        return Response(ser.data)
    else:
        data = [{'category': 'no found', 'tensors': 'invalid'}]
        return JsonResponse(data, safe=False)
