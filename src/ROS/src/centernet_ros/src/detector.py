#!/usr/bin/env python3
import rospy
import roslib; roslib.load_manifest('cv_bridge')
import os
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from sensor_msgs.msg import Image
from opts import opts
from detectors.detector_factory import detector_factory

threshold = 0.5 #limite de score para considerar silla

def CenterNet_detection(img):
  #preprocess - calibracion de la imagen
  bridge = CvBridge()
  cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough') #'8UC3'

  #detection
  ret = detector.run(cv_image)

  detections = []
  #postprocess - kalman
  for chair in ret['results'][57]:
      if chair[4] > threshold:
        for item in chair:
          detections.append(float(item))

  msg = Float32MultiArray()
  msg.layout.dim.append(MultiArrayDimension())
  msg.layout.dim[0].size = int(len(detections)/6)
  msg.layout.dim[0].stride = int(len(detections))
  msg.layout.dim[0].label = 'chair'
  msg.layout.dim.append(MultiArrayDimension())
  msg.layout.dim[1].size = int(6)
  msg.layout.dim[1].stride = int(6)
  msg.layout.dim[1].label = 'individual_data'
  msg.layout.data_offset = int(0)
  msg.data = detections

  pub.publish(msg)


rospy.init_node('Centernet', anonymous=True)

#init red
opt = opts().init()
os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
Detector = detector_factory[opt.task]
detector = Detector(opt)

#init comunicacion
pub = rospy.Publisher('/detections', Float32MultiArray, queue_size=10)
sub = rospy.Subscriber('/device_0/sensor_1/Color_0/image/data', Image, CenterNet_detection)
rospy.spin()
  

