#ls -v | cat -n | while read n f; do mv -n "$f" "$n.ext"; done  para cambiar los nombres de los archivos de una carpeta por numeros consecutivos

import _init_paths

import os
import cv2
import csv
import argparse
import json
import re

import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import cal_params as params_1
from camera_params_realsense import cal_params as params_2

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']
threshold = 0.5 #limite para decidir que es una silla


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


def carga_imagenes(directorio):
  if os.path.isdir(directorio):
    image_names = []
    ls = os.listdir(directorio)
    for file_name in sorted_alphanumeric(ls):
        ext = file_name[file_name.rfind('.') + 1:].lower()
        if ext in image_ext:
            image_names.append(os.path.join(directorio, file_name))
  else:
    image_names = [directorio]
  return image_names

#mantiene los valores de la distancia entre 0 y 255
def change_values(img):

  img[img <= 0] = 0
  img = (3276.7 * img).astype(np.int16)
  img[img > 32767] = 32767

  return img

#cambia todos los pixeles de la imagen por distancia en metros
def distabs_img(img, opt):
  if opt.dataset_name == 'custom':
    value_swap = np.array(img, dtype = np.uint16)
    value_swap.byteswap(True)

    imgDepthAbs = params_1.depthParam1 * 1.0 / (params_1.depthParam2 - value_swap)

    imgDepthAbs[imgDepthAbs < 0] = 0

  if opt.dataset_name == 'realsense':
    imgDepthAbs = np.array(img, dtype = np.uint16) * params_2.depth_scale / 1.5 #ajuste manual VALIDAR

  return imgDepthAbs



#la siguiente funcion cambia el valor de la media de los pixels por la distancia en metros
def distabs(value, opt):
  if opt.dataset_name == 'custom':
    value_swap = np.array([value], dtype = np.uint16)
    value_swap.byteswap(True)

    imgDepthAbs = params_1.depthParam1 / (params_1.depthParam2 - value_swap[0])

  if opt.dataset_name == 'realsense':
    imgDepthAbs = value * params_2.depth_scale / 1.5 #ajuste manual VALIDAR
 
  return imgDepthAbs


#funcion para comprobar que no se intenta seleccionar pixeles fuera de la imagen
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



#calibra las imagenes
def calibrate_images(img, rgb_flag, opt):
  if opt.dataset_name == 'custom':
    cal = params_1
  if opt.dataset_name == 'realsense':
    cal = params_2
  

  cammat_rgb = np.matrix([[cal.fx_rgb, 0, cal.cx_rgb],[0, cal.fy_rgb, cal.cy_rgb],[0, 0 ,1]])
  cammat_d = np.matrix([[cal.fx_d, 0, cal.cx_d],[0, cal.fy_d, cal.cy_d],[0, 0 ,1]])
  
  dist_coef_rgb = np.array([cal.k1_rgb, cal.k2_rgb, cal.p1_rgb, cal.p2_rgb, cal.k3_rgb])
  dist_coef_d = np.array([cal.k1_d, cal.k2_d, cal.p1_d, cal.p2_d, cal.k3_d])

  R_cam = np.matrix(cal.R)
  T_cam = np.array([cal.t_y, cal.t_x, cal.t_z]) #son camaras horizontales

  R1 = np.empty([3,3])
  R2 = np.empty([3,3])
  P1 = np.empty([3,4])
  P2 = np.empty([3,4])

  new_size = (640, 480)

  info = cv2.stereoRectify(cammat_rgb, dist_coef_rgb, cammat_d, dist_coef_d,(640, 480), R_cam, T_cam, R1, R2, P1, P2, None,
                           cv2.CALIB_ZERO_DISPARITY, 0, new_size)

  if rgb_flag:
    map1_rgb, map2_rgb = cv2.initUndistortRectifyMap(cammat_rgb, dist_coef_rgb, R1, P1, new_size, cv2.CV_16SC2)
    out = cv2.remap(img, map1_rgb, map2_rgb, cv2.INTER_LANCZOS4)
  else:
    map1_d, map2_d = cv2.initUndistortRectifyMap(cammat_d, dist_coef_d, R2, P2, new_size, cv2.CV_16SC2)
    out = cv2.remap(img, map1_d, map2_d, cv2.INTER_LANCZOS4)
    #out = (out*256).astype(np.uint16)

  return out


def analyze_data(opt, image_names, image_names_d):
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  document_data = {'images': [], 'annotations': [], 'categories': []}
  info_image = dict()

  i = 0
  j = 0
  n_det = 0
  percentage_print = 0
  for image_name in image_names:  #detecta en cada imagen
    ret = detector.run(image_name)
    i = i + 1

    percentage = int(i*100/len(image_names))
    #para sacar por pantalla el progreso
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


    image_info = {'file_name': '{}'.format(image_name),
                  'id': i,
                  'calib': []}
    document_data['images'].append(image_info)

    for chair in ret['results'][57]: #57 es el id de las sillas en el coco dataset
      if chair[4] > threshold:
        j = j + 1

        img = cv2.imread(image_names_d[i-1],-1)
        img_real = img.copy()

        #matriz con las distancias a cada punto
        if opt.dataset_name == 'custom':
          img_real = distabs_img(img_real, opt)
          img_real = change_values(img_real)
          img_real = calibrate_images(img_real.copy(), False, opt)
          img_real = img_real/3276.7
        
      vector = chair[0:4].copy()
      if opt.dataset_name == 'realsense':
          vector[0] = vector[0] - 25
          vector[2] = vector[2] - 25

      checked = check(vector, img.shape) #comprobar que el bbox no se sale de la imagen
      crop_img = img_real[int(checked[1]):int(checked[3]), int(checked[0]):int(checked[2])]


      if not np.all(crop_img <= 0):
        dist = np.percentile(crop_img[crop_img > 0.05], 50) #la mediana medira la distancia, no se tienen en cuenta valores nulos
        if dist == 0:
          dist = 0.0001 #evita que algun error
        if dist > 0: #evita errores
          n_det = n_det + 1
          annon_info= {'image_id': i,
                       'id': int(len(document_data['annotations']) + 1),
                       'category_id': 57,
                       'bbox': list(map(str,chair[0:4])),
                       'score': str(chair[4]),
                       'depth': str(dist)}

          document_data['annotations'].append(annon_info)

  return document_data, n_det



def dataset_maker(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  opt.debug = max(opt.debug, 1)
  opt.task = 'ctdet'

  path_dataset = os.path.join(os.path.dirname(os.getcwd()), 'data')
  path_dataset = os.path.join(path_dataset, opt.dataset_name)
  path_images = os.path.join(path_dataset, 'images')


  #json del dataset para training
  image_names = carga_imagenes(os.path.join(path_images, 'rgb'))
  image_names_d = carga_imagenes(os.path.join(path_images, 'd'))

  print("Dataset principal: ")
  document_data, n_det = analyze_data(opt, image_names, image_names_d)
  
  with open(os.path.join(path_dataset, 'dataset.json'), 'w') as file:
    json.dump(document_data, file)

  print("Total detections in datatset:")
  print(n_det)

  #json del test
  if opt.dataset_test:
    path_test = os.path.join(path_dataset, 'images_test')

    image_names = carga_imagenes(os.path.join(path_test, 'rgb'))
    image_names_d = carga_imagenes(os.path.join(path_test, 'd'))

    print("Dataset test:")
    document_data, n_det = analyze_data(opt, image_names, image_names_d)
  
    with open(os.path.join(path_dataset, 'dataset_test.json'), 'w') as file:
      json.dump(document_data, file)

    print("Total detections in datatset:")
    print(n_det)  

        
if __name__ == '__main__':
  opt = opts().init()
  dataset_maker(opt)
