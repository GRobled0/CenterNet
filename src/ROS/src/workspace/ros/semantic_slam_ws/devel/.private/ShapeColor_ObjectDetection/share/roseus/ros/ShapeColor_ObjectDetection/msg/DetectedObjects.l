;; Auto-generated. Do not edit!


(when (boundp 'ShapeColor_ObjectDetection::DetectedObjects)
  (if (not (find-package "SHAPECOLOR_OBJECTDETECTION"))
    (make-package "SHAPECOLOR_OBJECTDETECTION"))
  (shadow 'DetectedObjects (find-package "SHAPECOLOR_OBJECTDETECTION")))
(unless (find-package "SHAPECOLOR_OBJECTDETECTION::DETECTEDOBJECTS")
  (make-package "SHAPECOLOR_OBJECTDETECTION::DETECTEDOBJECTS"))

(in-package "ROS")
;;//! \htmlinclude DetectedObjects.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ShapeColor_ObjectDetection::DetectedObjects
  :super ros::object
  :slots (_header _objects ))

(defmethod ShapeColor_ObjectDetection::DetectedObjects
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:objects __objects) (let (r) (dotimes (i 0) (push (instance ShapeColor_ObjectDetection::ObjectInfo :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _objects __objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; ShapeColor_ObjectDetection/ObjectInfo[] _objects
    (apply #'+ (send-all _objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; ShapeColor_ObjectDetection/ObjectInfo[] _objects
     (write-long (length _objects) s)
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; ShapeColor_ObjectDetection/ObjectInfo[] _objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _objects (let (r) (dotimes (i n) (push (instance ShapeColor_ObjectDetection::ObjectInfo :init) r)) r))
     (dolist (elem- _objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ShapeColor_ObjectDetection::DetectedObjects :md5sum-) "a74ced4691e2f209ce4fbe3dd6d24c31")
(setf (get ShapeColor_ObjectDetection::DetectedObjects :datatype-) "ShapeColor_ObjectDetection/DetectedObjects")
(setf (get ShapeColor_ObjectDetection::DetectedObjects :definition-)
      "Header header
ObjectInfo[] objects


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
MSG: ShapeColor_ObjectDetection/ObjectInfo
string type
float32 prob
int32 tl_x
int32 tl_y
int32 width
int32 height

")



(provide :ShapeColor_ObjectDetection/DetectedObjects "a74ced4691e2f209ce4fbe3dd6d24c31")


