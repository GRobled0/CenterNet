import _init_paths

import os
import cv2

import numpy as np

from camera_params import *



def process_images():
  img = cv2.imread('/home/guillermo/anaconda3/envs/CenterNet/CenterNet/data/custom/images_test/rgb/4_1.ppm',-1)
  imgd = cv2.imread('/home/guillermo/anaconda3/envs/CenterNet/CenterNet/data/custom/images_test/d/4_1.pgm',-1)
  imgd = imgd.astype(np.uint16)
  imgd = (imgd.copy()/256).astype(np.uint8)
  #imgd = cv2.applyColorMap(imgd8, cv2.COLORMAP_JET)


  correction = np.matrix([[0.0, 1.0, 0.0],[1.0, 0.0, 0.0],[0.0, 0.0 ,1.0]])
  unit = np.matrix([[1.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.0, 0.0 ,1.0]])

  #overlay_s = cv2.addWeighted(img, 0.5, imgd, 0.5, 0)

  #cv2.imwrite('start.jpg', overlay_s)

  cammat_rgb = np.matrix([[fx_rgb, 0, cx_rgb],[0, fy_rgb, cy_rgb],[0, 0 ,1]])
  #cammat_rgb = np.matmul(correction, cammat_rgb)
  #cammat_rgb = np.matmul(cammat_rgb, correction)
  cammat_d = np.matrix([[fx_d, 0, cx_d],[0, fy_d, cy_d],[0, 0 ,1]])
  #cammat_d = np.matmul(correction, cammat_d)
  #cammat_d = np.matmul(cammat_d, correction)

  dist_coef_rgb = np.array([k1_rgb, k2_rgb, p1_rgb, p2_rgb, k3_rgb])
  dist_coef_d = np.array([k1_d, k2_d, p1_d, p2_d, k3_d])

  R_cam = np.matrix(R)

  #R_cam = np.matmul(correction, R_cam)
  #R_cam = np.matmul(R_cam, correction)

  T_cam = np.array([t_y, t_x, t_z]) #cambiados los ejes manualmente

  print("")
  print("Matrix y distorsion rgb:")
  print(cammat_rgb)
  print(dist_coef_rgb)
  print("Matrix y distorsion d:")
  print(cammat_d)
  print(dist_coef_d)
  print("R y T:")
  print(R_cam)
  print(T_cam)


  R1 = np.empty([3,3])
  R2 = np.empty([3,3])
  P1 = np.empty([3,4])
  P2 = np.empty([3,4])

  new_size = (640, 480)

  info = cv2.stereoRectify(cammat_rgb, dist_coef_rgb, cammat_d, dist_coef_d,(640, 480), R_cam, T_cam, R1, R2, P1, P2, None,
                    cv2.CALIB_ZERO_DISPARITY, -1, new_size)



  print("R1 y R2:")
  print(R1)
  print(R2)
  print('info')
  print(info[5])
  print(info[6])
  map1_rgb, map2_rgb = cv2.initUndistortRectifyMap(cammat_rgb, dist_coef_rgb, R1, P1, new_size, cv2.CV_16SC2)
  out_rgb = cv2.remap(img, map1_rgb, map2_rgb, cv2.INTER_LANCZOS4)
  cv2.imwrite('rgb.jpg', out_rgb)

  map1_d, map2_d = cv2.initUndistortRectifyMap(cammat_d, dist_coef_d, R2, P2, new_size, cv2.CV_16SC2)

  out_d = cv2.remap(imgd, map1_d, map2_d, cv2.INTER_LANCZOS4)
  out_d = (out_d.copy()*256).astype(np.uint16)
  print(out_d[5][5])

  print(np.percentile(out_d, 50))
  print(np.percentile(out_d[out_d > 0], 50))
  out_d[out_d == 0] = 30000
  cv2.imwrite('d.pgm', out_d)


  #overlay_f = cv2.addWeighted(out_rgb[0], 0.5, out_d, 0.5, 0)


  #cv2.imwrite('finnish.jpg', overlay_f)


if __name__ == '__main__':
  process_images()
