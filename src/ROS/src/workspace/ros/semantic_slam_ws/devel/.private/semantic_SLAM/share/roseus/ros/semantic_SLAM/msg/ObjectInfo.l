;; Auto-generated. Do not edit!


(when (boundp 'semantic_SLAM::ObjectInfo)
  (if (not (find-package "SEMANTIC_SLAM"))
    (make-package "SEMANTIC_SLAM"))
  (shadow 'ObjectInfo (find-package "SEMANTIC_SLAM")))
(unless (find-package "SEMANTIC_SLAM::OBJECTINFO")
  (make-package "SEMANTIC_SLAM::OBJECTINFO"))

(in-package "ROS")
;;//! \htmlinclude ObjectInfo.msg.html


(defclass semantic_SLAM::ObjectInfo
  :super ros::object
  :slots (_type _prob _tl_x _tl_y _width _height ))

(defmethod semantic_SLAM::ObjectInfo
  (:init
   (&key
    ((:type __type) "")
    ((:prob __prob) 0.0)
    ((:tl_x __tl_x) 0)
    ((:tl_y __tl_y) 0)
    ((:width __width) 0)
    ((:height __height) 0)
    )
   (send-super :init)
   (setq _type (string __type))
   (setq _prob (float __prob))
   (setq _tl_x (round __tl_x))
   (setq _tl_y (round __tl_y))
   (setq _width (round __width))
   (setq _height (round __height))
   self)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:prob
   (&optional __prob)
   (if __prob (setq _prob __prob)) _prob)
  (:tl_x
   (&optional __tl_x)
   (if __tl_x (setq _tl_x __tl_x)) _tl_x)
  (:tl_y
   (&optional __tl_y)
   (if __tl_y (setq _tl_y __tl_y)) _tl_y)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; string _type
    4 (length _type)
    ;; float32 _prob
    4
    ;; int32 _tl_x
    4
    ;; int32 _tl_y
    4
    ;; int32 _width
    4
    ;; int32 _height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; float32 _prob
       (sys::poke _prob (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _tl_x
       (write-long _tl_x s)
     ;; int32 _tl_y
       (write-long _tl_y s)
     ;; int32 _width
       (write-long _width s)
     ;; int32 _height
       (write-long _height s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _prob
     (setq _prob (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _tl_x
     (setq _tl_x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _tl_y
     (setq _tl_y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _width
     (setq _width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _height
     (setq _height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get semantic_SLAM::ObjectInfo :md5sum-) "55a63526fe7c32ce41ef4e85ff85bb42")
(setf (get semantic_SLAM::ObjectInfo :datatype-) "semantic_SLAM/ObjectInfo")
(setf (get semantic_SLAM::ObjectInfo :definition-)
      "string type
float32 prob
int32 tl_x
int32 tl_y
int32 width
int32 height

")



(provide :semantic_SLAM/ObjectInfo "55a63526fe7c32ce41ef4e85ff85bb42")


