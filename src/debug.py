import _init_paths

import os
import cv2
import csv
import pandas as pd
import numpy as np

from opts import opts
from detectors.detector_factory import detector_factory

from camera_params import *
import datasetmaker as dm

image_ext = ['jpg', 'jpeg', 'png', 'webp', 'ppm', 'pgm']



def eval_total(ret, im, imd, i, opt, path):
  img = cv2.imread(im,-1)
  imgd = cv2.imread(imd,-1)
  img_deb = img.copy()
  t = []
  p = []
  j = 0
  for chair in ret['results'][57]:
    if chair[4] > 0.65:
      j = j + 1
      checked = dm.check(chair[0:4], img.shape)

      crop_img = imgd[int(checked[1]):int(checked[3]), int(checked[0]):int(checked[2])]
      #cv2.imwrite(os.path.join(path, str(i) + '_' + str(j) + '.png'), crop_img)
      dist = dm.distabs(np.percentile(crop_img, 50))

      if opt.debug > 0:
        img_deb = cv2.rectangle(img_deb, (chair[0], chair[1]), (chair[2], chair[3]), (255,0,0), 2)
        txt = str(chair[5]) + str(" m")
        font = cv2.FONT_HERSHEY_SIMPLEX
        info_size = cv2.getTextSize(txt, font, 0.5, 2)[0]

        img_deb = cv2.rectangle(img_deb.copy(),
                               (chair[0], int(chair[1] - info_size[1] - 2)),
                               (int(chair[0] + info_size[0]), int(chair[1] - 2)),
                               (255,0,0), -1)
        img_deb = cv2.putText(img_deb.copy(),txt, (chair[0], int(chair[1] - 2)),
                              font, 0.5, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
      t.append(dist)
      p.append(chair[5])

  if opt.debug > 0:
    cv2.imwrite(os.path.join(path, str(i) + '.jpg'), img_deb)

  return p, t



def debug(opt):
  os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
  Detector = detector_factory[opt.task]
  detector = Detector(opt)

  path_dataset = os.path.join(os.path.dirname(os.getcwd()), 'data')
  path_dataset = os.path.join(path_dataset, opt.dataset_name)
  path_test = os.path.join(path_dataset, 'images_test')
  path_save = os.path.join(path_dataset, 'debug_images')

  if not os.path.exists(path_save):
    os.makedirs(path_save)
  
  image_names = dm.carga_imagenes(os.path.join(path_test, 'rgb'))
  image_names_d = dm.carga_imagenes(os.path.join(path_test, 'd'))

  pred = []
  target = []
  img_nm = []
  img_idx = []
  i = 0
  percentage_print = 0
  for image_name in image_names:
    ret = detector.run(image_name)
    im = image_name
    imd = image_names_d[i] 
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

    p, t = eval_total(ret, im, imd, i, opt, path_save)

    for pp in p:
      pred.append(pp)
    for tt in t:
      target.append(tt)
      img_nm.append(im)
      img_idx.append(i)

  print("Analisis completado...")

  data = {'Prediction': pred, 'Target': target, 'Img_index': img_idx, 'Img_name': img_nm}
  df = pd.DataFrame(data)
  df.to_excel(os.path.join(path_dataset, 'debug_data.xlsx'))

  print("Archivo creado")

        
if __name__ == '__main__':
  opt = opts().init()
  debug(opt)
