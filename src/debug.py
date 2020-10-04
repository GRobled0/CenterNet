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
threshold = 0.45 #limite de score para considerar silla



def dibujar_info(img, chair, info, color, color_txt):
  img = cv2.rectangle(img, (chair[0], chair[1]), (chair[2], chair[3]), color, 2)
  txt = info + str(" m")
  font = cv2.FONT_HERSHEY_SIMPLEX
  info_size = cv2.getTextSize(txt, font, 0.5, 2)[0]

  img = cv2.rectangle(img.copy(),
                         (chair[0], int(chair[1] - info_size[1] - 2)),
                         (int(chair[0] + info_size[0]), int(chair[1] - 2)),
                         color, -1)
  img = cv2.putText(img.copy(),txt, (chair[0], int(chair[1] - 2)),
                         font, 0.5, color_txt, thickness=1, lineType=cv2.LINE_AA)
  return img


def dibujar_texto(texto, img, color):
  overlay = cv2.putText(img.copy(), texto,
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)
  overlay = cv2.addWeighted(overlay, 0.5, img.copy(), 0.5, 0, img.copy())

  return overlay


def eval_total(ret, im, imd, i, opt, path):
  img = cv2.imread(im,-1)
  imgd = cv2.imread(imd,-1)
  img_deb = img.copy()
  imgd8 = (imgd.copy()/256).astype(np.uint8)
  img_deb_d = cv2.applyColorMap(imgd8, cv2.COLORMAP_JET)
  
  t = []
  p = []
  m = []
  q = []
  qq = []

  j = 0
  for chair in ret['results'][57]:
    if chair[4] > threshold:
      j = j + 1
      checked = dm.check(chair[0:4], img.shape)

      crop_img = imgd[int(checked[1]):int(checked[3]), int(checked[0]):int(checked[2])]
      dist = dm.distabs(np.percentile(crop_img, 50))

      q1 = dm.distabs(np.percentile(crop_img, 25))
      q3 = dm.distabs(np.percentile(crop_img, 75))
      mean = dm.distabs(np.mean(crop_img))

      if opt.debug > 0:
        img_deb = dibujar_info(img_deb.copy(), chair, str(chair[5]), (255,0,0), (255,255,255))
        img_deb_d = dibujar_info(img_deb_d.copy(), chair, str(dist), (255,255,255), (0,0,0))

      t.append(dist)
      p.append(chair[5])
      m.append(mean)
      q.append(q1)
      qq.append(q3)

  if opt.debug > 0:
    img_deb = dibujar_texto("Prediction", img_deb.copy(), (0,0,0))
    img_deb_d = dibujar_texto("Target", img_deb_d.copy(), (255,255,255))

    img_debugger = cv2.vconcat([img_deb, img_deb_d]) 
    cv2.imwrite(os.path.join(path, str(i) + '.jpg'), img_debugger)

  return p, t, m, q, qq



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
  media = []
  q1 = []
  q3 = []

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

    p, t, m, q, qq = eval_total(ret, im, imd, i, opt, path_save)

    for pp in p:
      pred.append(pp)
    for tt in t:
      target.append(tt)
      img_nm.append(im)
      img_idx.append(i)
    for mm in m:
      media.append(mm)
    for q11 in q:
      q1.append(q11)
    for q33 in qq:
      q3.append(q33)

  print("Analisis completado...")

  data = {'Prediction': pred, 'Target': target, 'Media': media, 'Q1': q1, 'Q3': q3, 'Img_index': img_idx, 'Img_name': img_nm}
  df = pd.DataFrame(data)
  df.to_excel(os.path.join(path_dataset, 'debug_data.xlsx'))

  print("Archivo creado")

        
if __name__ == '__main__':
  opt = opts().init()
  debug(opt)
