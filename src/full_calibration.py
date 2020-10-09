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


opt = opts().init()

path_dataset = os.path.join(os.path.dirname(os.getcwd()), 'data')
path_dataset = os.path.join(path_dataset, opt.dataset_name)
path_images = os.path.join(path_dataset, 'images')

image_names = dm.carga_imagenes(os.path.join(path_images, 'rgb'))

for im in image_names:
  img = cv2.imread(im,-1)
  img = dm.calibrate_images(img, True)
  cv2.imwrite(im, img)

if opt.dataset_test:
  path_test = os.path.join(path_dataset, 'images_test')
  image_names = dm.carga_imagenes(os.path.join(path_test, 'rgb'))

for im in image_names:
  img = cv2.imread(im,-1)
  img = dm.calibrate_images(img, True)
  cv2.imwrite(im, img)
