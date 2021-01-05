;; Auto-generated. Do not edit!


(when (boundp 'semantic_SLAM::detecciones)
  (if (not (find-package "SEMANTIC_SLAM"))
    (make-package "SEMANTIC_SLAM"))
  (shadow 'detecciones (find-package "SEMANTIC_SLAM")))
(unless (find-package "SEMANTIC_SLAM::DETECCIONES")
  (make-package "SEMANTIC_SLAM::DETECCIONES"))

(in-package "ROS")
;;//! \htmlinclude detecciones.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass semantic_SLAM::detecciones
  :super ros::object
  :slots (_header _image_header _data ))

(defmethod semantic_SLAM::detecciones
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:image_header __image_header) (instance std_msgs::Header :init))
    ((:data __data) (let (r) (dotimes (i 0) (push (instance semantic_SLAM::deteccion :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _image_header __image_header)
   (setq _data __data)
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
  (:data
   (&rest __data)
   (if (keywordp (car __data))
       (send* _data __data)
     (progn
       (if __data (setq _data (car __data)))
       _data)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/Header _image_header
    (send _image_header :serialization-length)
    ;; semantic_SLAM/deteccion[] _data
    (apply #'+ (send-all _data :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/Header _image_header
       (send _image_header :serialize s)
     ;; semantic_SLAM/deteccion[] _data
     (write-long (length _data) s)
     (dolist (elem _data)
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
   ;; semantic_SLAM/deteccion[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (let (r) (dotimes (i n) (push (instance semantic_SLAM::deteccion :init) r)) r))
     (dolist (elem- _data)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get semantic_SLAM::detecciones :md5sum-) "b4be5ca1bc1bc58da3c9b891aa8e7a4c")
(setf (get semantic_SLAM::detecciones :datatype-) "semantic_SLAM/detecciones")
(setf (get semantic_SLAM::detecciones :definition-)
      "Header header
Header image_header
deteccion[] data

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
MSG: semantic_SLAM/deteccion
string Class
float64 probability
int64 xmin
int64 ymin
int64 xmax
int64 ymax
float64 depth


")



(provide :semantic_SLAM/detecciones "b4be5ca1bc1bc58da3c9b891aa8e7a4c")


