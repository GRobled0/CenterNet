;; Auto-generated. Do not edit!


(when (boundp 'centernet_ros::BoundingBooxes)
  (if (not (find-package "CENTERNET_ROS"))
    (make-package "CENTERNET_ROS"))
  (shadow 'BoundingBooxes (find-package "CENTERNET_ROS")))
(unless (find-package "CENTERNET_ROS::BOUNDINGBOOXES")
  (make-package "CENTERNET_ROS::BOUNDINGBOOXES"))

(in-package "ROS")
;;//! \htmlinclude BoundingBooxes.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass centernet_ros::BoundingBooxes
  :super ros::object
  :slots (_header _image_header _bounding_boxes ))

(defmethod centernet_ros::BoundingBooxes
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:image_header __image_header) (instance std_msgs::Header :init))
    ((:bounding_boxes __bounding_boxes) (let (r) (dotimes (i 0) (push (instance centernet_ros::BoundingBoox :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _image_header __image_header)
   (setq _bounding_boxes __bounding_boxes)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:image_header
   (&rest __image_header)
   (if (keywordp (car __image_header))
       (send* _image_header __image_header)
     (progn
       (if __image_header (setq _image_header (car __image_header)))
       _image_header)))
  (:bounding_boxes
   (&rest __bounding_boxes)
   (if (keywordp (car __bounding_boxes))
       (send* _bounding_boxes __bounding_boxes)
     (progn
       (if __bounding_boxes (setq _bounding_boxes (car __bounding_boxes)))
       _bounding_boxes)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/Header _image_header
    (send _image_header :serialization-length)
    ;; centernet_ros/BoundingBoox[] _bounding_boxes
    (apply #'+ (send-all _bounding_boxes :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/Header _image_header
       (send _image_header :serialize s)
     ;; centernet_ros/BoundingBoox[] _bounding_boxes
     (write-long (length _bounding_boxes) s)
     (dolist (elem _bounding_boxes)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; std_msgs/Header _image_header
     (send _image_header :deserialize buf ptr-) (incf ptr- (send _image_header :serialization-length))
   ;; centernet_ros/BoundingBoox[] _bounding_boxes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bounding_boxes (let (r) (dotimes (i n) (push (instance centernet_ros::BoundingBoox :init) r)) r))
     (dolist (elem- _bounding_boxes)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get centernet_ros::BoundingBooxes :md5sum-) "37a46cf41c29ddce83a4a450ac620f6e")
(setf (get centernet_ros::BoundingBooxes :datatype-) "centernet_ros/BoundingBooxes")
(setf (get centernet_ros::BoundingBooxes :definition-)
      "Header header
Header image_header
BoundingBoox[] bounding_boxes

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: centernet_ros/BoundingBoox
string Class
float64 probability
int64 xmin
int64 ymin
int64 xmax
int64 ymax
float64 depth

")



(provide :centernet_ros/BoundingBooxes "37a46cf41c29ddce83a4a450ac620f6e")


