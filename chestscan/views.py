from django.shortcuts import render
from fastai.vision import *
from fastai.utils.mem import *
from fastai.callbacks.hooks import *
import os
import urllib.request

# Create your views here.
def homepage(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR,'model/')
    learn = load_learner(path, 'exported.pkl')
    urllib.request.urlretrieve(r"https://upload.wikimedia.org/wikipedia/commons/a/a1/Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg", './image.jpg')
    img = open_image('./image.jpg')
    pred_class,pred_idx,outputs = learn.predict(img)
    return render(request,'index.html',{'datapredicted':pred_class,'predidx':pred_idx,'outputs':outputs})