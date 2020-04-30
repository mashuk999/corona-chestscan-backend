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
    urllib.request.urlretrieve(r"https://www.kaggleusercontent.com/kf/32860195/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Ol5U3viyss2EFMlmRThC7Q.Lcs2jz0DJb-2DOCAWJoyPn9LGHNoqKt-B__NCTOoyTIANuRk8Rels1US3KBGwrXFfchjU2rVWU6P0r1KlmpL8HQePJXYnKw5Gjdr7WPZiWIxTI21zhqir_kGCq7eP_UvixwJ0KQdndyi7wbXF2wPwJ0vWRs9QV6ehfsFrM_Gy3sibriEZaSvHvY6WuhT7lnk65y3u4My_AdWJ0b4FZz08BD8jSRznWJMsu-_JmPCWWc_AEYMNE3ImSvvrgeiy83LNYvebgNDqV_-705PA8wNhZ0H8grS-NXpLiPu-ek8bDwQy1DYjuUhVhkcad9GETlaOhOXH_F5rpokX0OlWj9YQ2f7FOxjMA4J61IznMb-gAHAbJuQpZg8ZF1nuLXlPHSMPkgEJ8rL8z8FRyic99ZQCdEaOiHmpoIAEOfFn1b70m28ikTKinAyjSgVPJjvsty0HSNEJx-BW47W5-D4M_QIhA65mwo01KW2pnN8OWfsSCEZxAXn_VqeUDdlv2y5hVCcwDf1Vr6vEJun7EMiY2Mobqm5DE6HjKa-ZB1BTOQYYTyXilzdDT76nsSzBTD3dTC3hDYhc25NRXTYghvAqltZg84lduABU4iiYc-fXDASipv9YP-HUdtkdoFWO-uUF1vn4xFPJN_5uGq2mfLmiz37bYf7RQki8q3jglMaj1fXOhY.8rdfdnyUuF82dk_PXyoDnA/__results___files/__results___11_0.png", './image.jpg')
    img = open_image('./image.jpg')
    pred_class,pred_idx,outputs = learn.predict(img)
    return render(request,'index.html',{'datapredicted':pred_class,'predidx':pred_idx,'outputs':outputs})