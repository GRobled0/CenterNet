; Auto-generated. Do not edit!


(cl:in-package semantic_SLAM-msg)


;//! \htmlinclude detecciones.msg.html

(cl:defclass <detecciones> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (image_header
    :reader image_header
    :initarg :image_header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (data
    :reader data
    :initarg :data
    :type (cl:vector semantic_SLAM-msg:deteccion)
   :initform (cl:make-array 0 :element-type 'semantic_SLAM-msg:deteccion :initial-element (cl:make-instance 'semantic_SLAM-msg:deteccion))))
)

(cl:defclass detecciones (<detecciones>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <detecciones>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'detecciones)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name semantic_SLAM-msg:<detecciones> is deprecated: use semantic_SLAM-msg:detecciones instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <detecciones>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:header-val is deprecated.  Use semantic_SLAM-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'image_header-val :lambda-list '(m))
(cl:defmethod image_header-val ((m <detecciones>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:image_header-val is deprecated.  Use semantic_SLAM-msg:image_header instead.")
  (image_header m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <detecciones>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:data-val is deprecated.  Use semantic_SLAM-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <detecciones>) ostream)
  "Serializes a message object of type '<detecciones>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image_header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <detecciones>) istream)
  "Deserializes a message object of type '<detecciones>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image_header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'semantic_SLAM-msg:deteccion))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<detecciones>)))
  "Returns string type for a message object of type '<detecciones>"
  "semantic_SLAM/detecciones")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'detecciones)))
  "Returns string type for a message object of type 'detecciones"
  "semantic_SLAM/detecciones")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<detecciones>)))
  "Returns md5sum for a message object of type '<detecciones>"
  "b4be5ca1bc1bc58da3c9b891aa8e7a4c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'detecciones)))
  "Returns md5sum for a message object of type 'detecciones"
  "b4be5ca1bc1bc58da3c9b891aa8e7a4c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<detecciones>)))
  "Returns full string definition for message of type '<detecciones>"
  (cl:format cl:nil "Header header~%Header image_header~%deteccion[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: semantic_SLAM/deteccion~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%float64 depth~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'detecciones)))
  "Returns full string definition for message of type 'detecciones"
  (cl:format cl:nil "Header header~%Header image_header~%deteccion[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: semantic_SLAM/deteccion~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%float64 depth~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <detecciones>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image_header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <detecciones>))
  "Converts a ROS message object to a list"
  (cl:list 'detecciones
    (cl:cons ':header (header msg))
    (cl:cons ':image_header (image_header msg))
    (cl:cons ':data (data msg))
))
