import _init_paths

import os
import cv2
import csv

import numpy as np
import statistics as sta

from camera_params import *

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


def mostrar_seleccion(low_thres,high_thres, img):
  i_max, j_max = img.shape
  cv2.imshow('original',img)
  for i in range (0, i_max):
     for j in range (0, j_max):

       if (img[i][j] < high_thres) and  (img[i][j] > low_thres):
         img[i][j] = 0

  cv2.imshow('seleccion',img)
  cv2.waitKey()
  cv2.destroyAllWindows()



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


def target():
  image_names = carga_imagenes('/home/guillermo/Escritorio/dataset/test_all/3_3.png')

  for (image_name) in image_names:

    img = cv2.imread(image_name,-1)

    low_thres = np.percentile(img, low_percentile)
    high_thres = np.percentile(img, high_percentile)

    media = distabs_media(low_thres, high_thres, img.copy())
    print('media:',media, 'metros')
    mostrar_seleccion(low_thres,high_thres, img.copy())
    


if __name__ == '__main__':
  target()
