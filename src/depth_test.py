#python depth_test.py ddd --demo /home/guillermo/anaconda3/envs/CenterNet/CenterNet/images/19064748793_bb942deea1_k.jpg --exp_id /home/guillermo/Escritorio/dataset/predicciones --load_model ../models/ddd_3dop.pth

#ddd usa kitti por default
import _init_paths

import os
import cv2
import csv

import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import *

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']
threshold = 0.85


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


def red(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  opt.debug = max(opt.debug, 1)
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  image_names = carga_imagenes(opt.demo) #carga imagenes rgb

  for (image_name) in image_names:  #detecta en cada imagen
    ret = detector.run(image_name)
    print(ret['results'])


        
if __name__ == '__main__':
  opt = opts().init()
  red(opt)
