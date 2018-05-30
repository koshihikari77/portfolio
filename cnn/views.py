# -*- Coding: utf-8 -*-
import tensorflow as tf
import base64
from io import BytesIO
import os
from django.shortcuts import render
from django.views import generic
from .forms import ImageUploadForm
import numpy as np
from PIL import Image
from keras.models import Sequential,model_from_json,model_from_yaml
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

graph = tf.get_default_graph()



class UploadView(generic.FormView):
    template_name = 'cnn/upload.html'
    form_class = ImageUploadForm

    @csrf_exempt
    def form_valid(self,form):
        global graph
        with graph.as_default():
            file = form.cleaned_data['file']

            with open(os.path.join('cnn', 'model.json'), 'r') as f:
                    m = f.read()
                    model = model_from_yaml(m)
            img = Image.open(file).resize((28,28)).convert('L')
            img = np.asarray(img)
            img_array = img.reshape(1, 28, 28, 1) / 255

            pr = model.predict(img_array)

            context = {
                'result':np.argmax(pr),
            }

            return render(self.request,'cnn/results.html',context)


class PaintView(generic.TemplateView):
    template_name = 'cnn/paint.html'

    @csrf_exempt
    def post(self,request):
        global graph
        with graph.as_default():
            base_64_string = request.POST['img-src'].replace(
                'data:image/png;base64,',''
            )
            file = BytesIO(base64.b64decode(base_64_string))

            with open(os.path.join('cnn', 'model.json'), 'r') as f:
                    m = f.read()
                    model = model_from_yaml(m)

            model.load_weights(os.path.join('cnn', 'param.hdf5'))
            img = Image.open(file).resize((28,28)).convert('L')
            img = np.asarray(img)
            img_array = img.reshape(1,28, 28,1)/255

            pr = model.predict(img_array)

            context = {
                'result':np.argmax(pr)
            }

            return render(self.request,'cnn/results.html',context)
