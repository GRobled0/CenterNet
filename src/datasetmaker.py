#python datasetmaker.py
#hay que aplicar parametros intrinsecos y extrinsecos de la camara

#ls -v | cat -n | while read n f; do mv -n "$f" "$n.ext"; done  para cambiar los nombres de los archivos de una carpeta por numeros consecutivos

import _init_paths

import os
import cv2
import csv
import argparse
import json

import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import *

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']
threshold = 0.85 #limite para decidir que es una silla

def carga_imagenes(directorio):
  if os.path.isdir(directorio):
    image_names = []
    ls = os.listdir(directorio)
    for file_name in sorted(ls):
        ext = file_name[file_name.rfind('.') + 1:].lower()
        if ext in image_ext:
            image_names.append(os.path.join(directorio, file_name))
  else:
    image_names = [directorio]
  return image_names




#la siguiente funcion cambia el valor de la media de los pixels por la distancia en metros
def distabs(value):
  value_swap = np.array([value], dtype = np.uint16)
  value_swap.byteswap(True)

  imgDepthAbs = depthParam1 / (depthParam2 - value_swap[0]); 

  return imgDepthAbs


def check(bbox, shape):
  checked = bbox
  thresh = 0

  for i in range(0,4):
    if checked[i] < 0:
      checked[i] = 0
    if i % 2 == 0:
       if checked[i] > shape[1]:
         checked[i] = shape[1]
    else:
      if checked[i] > shape[0]:
         checked[i] = shape[0]

  return checked



def analyze_data(opt, image_names, image_names_d):
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  document_data = {'images': [], 'annotations': [], 'categories': []}
  info_image = dict()

  i = 0
  j = 0
  percentage_print = 0
  for image_name in image_names:  #detecta en cada imagen
    ret = detector.run(image_name)
    i = i + 1

    percentage = int(i*100/len(image_names))

    if percentage >= percentage_print:
       string = "["
       for x in range(int(100/2.5)):
         if x <= int(percentage/2.5):
           string = string + "|"
         else:
           string = string + "-"
       string = string + "] "
       print(string + str(percentage) + '%')
       percentage_print = percentage_print + 2.5    

    #print('imagen:' + str(i))

    image_info = {'file_name': '{}'.format(image_name),
                  'id': i,
                  'calib': []}
    document_data['images'].append(image_info)

    for chair in ret['results'][57]: #57 es el id de las sillas en el coco dataset
      if chair[4] > threshold:
        j = j + 1
        img = cv2.imread(image_names_d[i-1],-1)

        checked = check(chair[0:4], img.shape) #comprobar que el bbox no se sale de la imagen

        crop_img = img[int(checked[1]):int(checked[3]), int(checked[0]):int(checked[2])]

        dist = distabs(np.percentile(crop_img, 0.5)) #la mediana caracterizará la distancia
        if dist == 0:
          dist = 0.001 #parece que sino da error

        annon_info= {'image_id': i,
                     'id': int(len(document_data['annotations']) + 1),
                     'category_id': 57,
                     'bbox': list(map(str,chair[0:4])),
                     'score': str(chair[4]),
                     'depth': str(dist)}

        document_data['annotations'].append(annon_info)

  return document_data



def dataset_maker(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  opt.debug = max(opt.debug, 1)
  opt.task = 'ctdet'

  path_dataset = os.path.join(os.path.dirname(os.getcwd()), 'data/custom')
  path_images = os.path.join(path_dataset, 'images')


  #json del dataset para training
  image_names = carga_imagenes(os.path.join(path_images, 'rgb'))
  image_names_d = carga_imagenes(os.path.join(path_images, 'd'))

  print("Dataset principal: ")
  document_data = analyze_data(opt, image_names, image_names_d)
  
  with open(os.path.join(path_dataset, 'dataset.json'), 'w') as file:
    json.dump(document_data, file)

  #json del test
  path_test = os.path.join(path_dataset, 'images_test')

  image_names = carga_imagenes(os.path.join(path_test, 'rgb'))
  image_names_d = carga_imagenes(os.path.join(path_test, 'd'))

  print("Dataset test:")
  document_data = analyze_data(opt, image_names, image_names_d)
  
  with open(os.path.join(path_dataset, 'dataset_test.json'), 'w') as file:
    json.dump(document_data, file)
  

        
if __name__ == '__main__':
  opt = opts().init()
  dataset_maker(opt)
