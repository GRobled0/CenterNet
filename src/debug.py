#hay que aplicar parametros intrinsecos y extrinsecos de la camara

import _init_paths

import os
import cv2
import csv

import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import *
from target_depth import *

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']

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


def distabs_seleccion(low_thres, high_thres, img):
  i_max, j_max = img.shape
  img_swap = np.uint16(img.copy())
  img_swap.byteswap(True)

  m = 0
  n = 0

  for i in range (0, i_max):
     for j in range (0, j_max):
       if (img[i][j] < high_thres) and  (img[i][j] > low_thres):
         img[i][j] = 0

  return img


def eval_total_picture(ret, im, imd):
  img = cv2.imread(im,-1)
  imgd = cv2.imread(imd,-1)
  img_deb = img.copy()
  for chair in ret['results'][57]: #57 es el id de las sillas en el coco dataset
    if chair[4] > 0.85:
      crop_img = imgd[int(chair[1]):int(chair[3]), int(chair[0]):int(chair[2])]

      low_thres = np.percentile(crop_img, low_percentile)
      high_thres = np.percentile(crop_img, high_percentile)

      dist = distabs_media(low_thres, high_thres, crop_img.copy())

      img_seleccion = distabs_seleccion(low_thres, high_thres, crop_img.copy())
      cv2.imwrite('/home/guillermo/Escritorio/resultados/seleccion.png', img_seleccion)
      cv2.imwrite('/home/guillermo/Escritorio/resultados/original.png', img)
      cv2.imwrite('/home/guillermo/Escritorio/resultados/crop.png', crop_img)

      img_deb = cv2.rectangle(img, (chair[0], chair[1]), (chair[2], chair[3]), (255,0,0), 2)
      txt = str(chair[5]) + str(" m")
      font = cv2.FONT_HERSHEY_SIMPLEX
      info_size = cv2.getTextSize(txt, font, 0.5, 2)[0]

      img_deb = cv2.rectangle(img_deb.copy(),
                               (chair[0], int(chair[1] - info_size[1] - 2)),
                               (int(chair[0] + info_size[0]), int(chair[1] - 2)),
                               (255,0,0), -1)
      img_deb = cv2.putText(img_deb.copy(), txt, (chair[0], int(chair[1] - 2)), font, 0.5, (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

      cv2.imwrite('/home/guillermo/Escritorio/resultados/gif/1.png', img_deb)

      print(dist)


def eval_point(point, max_shape):
  if point < 0:
    point = 0
  if point > max_shape:
    point = max_shape
  return point


def eval_total(ret, im, imd,i):
  img = cv2.imread(im,-1)
  imgd = cv2.imread(imd,-1)
  img_deb = img.copy()
  e = []
  error = 0
  for chair in ret['results'][57]:
    if chair[4] > 0.85:

      pointy0 = eval_point(int(chair[1]), imgd.shape[0])
      pointy1 = eval_point(int(chair[3]), imgd.shape[0])
      pointx0 = eval_point(int(chair[0]), imgd.shape[1])
      pointx1 = eval_point(int(chair[2]), imgd.shape[1])

      crop_img = imgd[pointy0:pointy1, pointx0:pointx1]


      low_thres = np.percentile(crop_img, low_percentile)
      high_thres = np.percentile(crop_img, high_percentile)

      dist = distabs_media(low_thres, high_thres, crop_img.copy())

      error = chair[5] - dist #calculamos la diferencia entre los predicho y lo real

      img_deb = cv2.rectangle(img_deb, (chair[0], chair[1]), (chair[2], chair[3]), (255,0,0), 2)
      txt = str(chair[5]) + str(" m")
      font = cv2.FONT_HERSHEY_SIMPLEX
      info_size = cv2.getTextSize(txt, font, 0.5, 2)[0]

      img_deb = cv2.rectangle(img_deb.copy(),
                               (chair[0], int(chair[1] - info_size[1] - 2)),
                               (int(chair[0] + info_size[0]), int(chair[1] - 2)),
                               (255,0,0), -1)
      img_deb = cv2.putText(img_deb.copy(), txt, (chair[0], int(chair[1] - 2)), font, 0.5, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
      e.append(error)

  cv2.imwrite('/home/guillermo/Escritorio/resultados/gif/' + str(i) + '.jpg', img_deb)

  return e



def debug(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  
  image_names = carga_imagenes('/home/guillermo/Escritorio/dataset/reception_rooms/images_4')
  image_names_d = carga_imagenes('/home/guillermo/Escritorio/dataset/reception_rooms/depth_4')

  #im = '/home/guillermo/Escritorio/dataset/reception_rooms/images_3/1.ppm'
  #imd = '/home/guillermo/Escritorio/dataset/reception_rooms/depth_3/4.pgm'

  #ret = detector.run(im)
  #eval_total_picture(ret, im, imd)

  error = []
  i = 0
  for image_name in image_names:
    ret = detector.run(image_name)
    im = image_name
    imd = image_names_d[i] 
    i = i + 1
    print(i)
    e = eval_total(ret, im, imd, i)

    for ee in e:
      error.append(ee)

  error_np = np.float64(error)

  mean = np.mean(error_np, dtype=np.float64)
  std = np.std(error_np, dtype=np.float64)

  print("Media: " + str(mean))
  print("Std: " + str(std))

        
if __name__ == '__main__':
  opt = opts().init()
  debug(opt)
