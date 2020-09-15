#python datasetmaker.py ctdet
#hay que aplicar parametros intrinsecos y extrinsecos de la camara

#ls -v | cat -n | while read n f; do mv -n "$f" "$n.ext"; done  para cambiar los nombres de los archivos de una carpeta por numeros consecutivos

import _init_paths

import os
import cv2
import csv

import json

import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import *

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']
threshold = 0.85

low_percentile = 25
high_percentile = 75 #el blanco contiene menos información, a partir de 10 m todos los valores son identicos

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



def guardar_imagen(directorio, id1, id2):
  out_dir = []
  out_dir.append(directorio)
  out_dir.append('/')
  out_dir.append(str(id1))
  out_dir.append('_')
  out_dir.append(str(id2))
  out_dir.append('.png')
  out = ''.join(out_dir)
  return out 


def distabs_media(low_thres, high_thres, img):
  i_max, j_max = img.shape
  img_swap = np.uint16(img.copy())
  img_swap.byteswap(True)

  m = 0
  n = 0

  for i in range (0, i_max):
     for j in range (0, j_max):

       if (img[i][j] < high_thres) and  (img[i][j] > low_thres):
         imgDepthAbs = depthParam1 / (depthParam2 - img_swap[i][j]); 

         if imgDepthAbs > maxDepth:
           imgDepthAbs = maxDepth   
    
         if imgDepthAbs < 0:
           imgDepthAbs = 0

         m = m + imgDepthAbs
         n = n + 1
  if n == 0:
    n = 1
  return m/n



def dataset_maker(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  opt.debug = max(opt.debug, 1)
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  document_data = {'images': [], 'annotations': [], 'categories': []}
  info_image = dict()
  
  image_names = carga_imagenes('/home/guillermo/Escritorio/dataset/reception_rooms/images_3')
  image_names_d = carga_imagenes('/home/guillermo/Escritorio/dataset/reception_rooms/depth_3') #carga imagenes d

  i = 0
  j = 0
  for image_name in image_names:  #detecta en cada imagen
    ret = detector.run(image_name)
    i = i + 1 #cada imagen rgb tiene en la misma posicion su imagen d

    print('imagen:' + str(i))

    image_info = {'file_name': '{}'.format(image_name),
                  'id': i,
                  'calib': []}
    document_data['images'].append(image_info)

    for chair in ret['results'][57]: #57 es el id de las sillas en el coco dataset
      if chair[4] > threshold:
        j = j + 1
        img = cv2.imread(image_names_d[i+3],-1) #cambiar si duese necesario, +3 parece que en dataset estan movidas
        crop_img = img[int(chair[1]):int(chair[3]), int(chair[0]):int(chair[2])]

        low_thres = np.percentile(crop_img, low_percentile)
        high_thres = np.percentile(crop_img, high_percentile)

        dist = distabs_media(low_thres, high_thres, crop_img.copy())
        if dist == 0:
          dist = 0.01 #parece que sino da error

        annon_info= {'image_id': i,
                     'id': int(len(document_data['annotations']) + 1),
                     'category_id': 57,
                     'bbox': list(map(str,chair[0:4])),
                     'score': str(chair[4]),
                     'depth': str(dist)}

        document_data['annotations'].append(annon_info)

  with open('dataset_3.json', 'w') as file:
    json.dump(document_data, file)


        
if __name__ == '__main__':
  opt = opts().init()
  dataset_maker(opt)
