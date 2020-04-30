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
    urllib.request.urlretrieve("https://www.healthimaging.com/sites/default/files/styles/media_image_mobile/public/assets/articles/4996132.jpg", './image.jpg')
    img = open_image('./image.jpg')
    pred_class,pred_idx,outputs = learn.predict(img)
    return render(request,'index.html',{'datapredicted':pred_class,'predidx':pred_idx,'outputs':outputs})