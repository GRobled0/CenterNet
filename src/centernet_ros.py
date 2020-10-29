from opts import opts
from detectors.detector_factory import detector_factory
import rospy
import os
import cv2
from changer import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image

threshold = 0.5 #limite de score para considerar silla

rospy.init_node('Centernet', anonymous=True)

#init red
opt = opts().init()
os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpus_str
Detector = detector_factory[opt.task]
detector = Detector(opt)

#init comunicacion
pub = rospy.Publisher('/detections', String, queue_size=10)
sub = rospy.Subscriber('/device_0/sensor_1/Color_0/image/data', Image, CenterNet_detection)
rospy.spin()

def CenterNet_detection(img):
  #preprocess - calibracion de la imagen
  bridge = CvBridge()
  cv_image = bridge.imgmsg_to_cv2(img, desired_encoding='passthrough')

  #detection
  ret = detector.run(cv_img)

  detections = []

  #postprocess - kalman
  for chair in ret['results'][57]:
      if chair[4] > threshold:
        detections.append(chair)

  pub.publish(detections)
        
if __name__ == '__main__':
  opt = opts().init()
  demo(opt)
  

