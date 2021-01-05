#!/usr/bin/env python3
import rospy
import os
import cv2
import sys
import roslib; roslib.load_manifest('cv_bridge')
from cv_bridge import CvBridge
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from sensor_msgs.msg import Image
from opts import opts
from detectors.detector_factory import detector_factory
from centernet_ros.msg import BoundingBox
from centernet_ros.msg import BoundingBoxes

threshold = 0.25 #limite de score para empezar a considerar silla

def dibujar_info(img, chair):
  img = cv2.rectangle(img, (chair[0], chair[1]), (chair[2], chair[3]), (0, 255, 0), 2)
  txt = "{:.2f}".format(chair[5]) + str(" m")
  font = cv2.FONT_HERSHEY_SIMPLEX
  info_size = cv2.getTextSize(txt, font, 0.5, 2)[0]

  img = cv2.rectangle(img.copy(),
                         (chair[0], int(chair[1] - info_size[1] - 2)),
                         (int(chair[0] + info_size[0]), int(chair[1] - 2)),
                         (0, 255, 0), -1)
  img = cv2.putText(img.copy(),txt, (chair[0], int(chair[1] - 2)),
                         font, 0.5, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
  return img


def CenterNet_detection(img):
  #preprocess - recepcion y calibracion de la imagen
  bridge = CvBridge()
  cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough') #'8UC3'

  #detection
  ret = detector.run(cv_image)

  detections = []

  msg = BoundingBoxes()
  msg.image_header = img.header

  #postprocess - mensaje
  for chair in ret['results'][57]:
      if chair[4] > threshold:
        msg.bounding_boxes.append(BoundingBox())
        msg.bounding_boxes[-1].Class = 'chair'
        msg.bounding_boxes[-1].probability = float(chair[4])
        msg.bounding_boxes[-1].xmin = int(chair[0])
        msg.bounding_boxes[-1].xmax = int(chair[2])
        msg.bounding_boxes[-1].ymin = int(chair[1])
        msg.bounding_boxes[-1].ymax = int(chair[3])
        msg.bounding_boxes[-1].depth = float(chair[5])

        cv_image = dibujar_info(cv_image, chair)

  img_msg = bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")

  pub.publish(msg)
  pub_im.publish(img_msg)


rospy.init_node('Centernet', anonymous=True)

#init red
opt = opts().init()
os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
Detector = detector_factory[opt.task]
detector = Detector(opt)

#init comunicacion
pub = rospy.Publisher('/centernet/detections', BoundingBoxes, queue_size=10)
pub_im = rospy.Publisher('/centernet/processed_images', Image, queue_size=10)
sub = rospy.Subscriber('/camera/color/image_raw', Image, CenterNet_detection)
rospy.spin()
  

