; Auto-generated. Do not edit!


(cl:in-package centernet_ros-msg)


;//! \htmlinclude BoundingBooxes.msg.html

(cl:defclass <BoundingBooxes> (roslisp-msg-protocol:ros-message)
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
   (bounding_boxes
    :reader bounding_boxes
    :initarg :bounding_boxes
    :type (cl:vector centernet_ros-msg:BoundingBoox)
   :initform (cl:make-array 0 :element-type 'centernet_ros-msg:BoundingBoox :initial-element (cl:make-instance 'centernet_ros-msg:BoundingBoox))))
)

(cl:defclass BoundingBooxes (<BoundingBooxes>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BoundingBooxes>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BoundingBooxes)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name centernet_ros-msg:<BoundingBooxes> is deprecated: use centernet_ros-msg:BoundingBooxes instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <BoundingBooxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader centernet_ros-msg:header-val is deprecated.  Use centernet_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'image_header-val :lambda-list '(m))
(cl:defmethod image_header-val ((m <BoundingBooxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader centernet_ros-msg:image_header-val is deprecated.  Use centernet_ros-msg:image_header instead.")
  (image_header m))

(cl:ensure-generic-function 'bounding_boxes-val :lambda-list '(m))
(cl:defmethod bounding_boxes-val ((m <BoundingBooxes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader centernet_ros-msg:bounding_boxes-val is deprecated.  Use centernet_ros-msg:bounding_boxes instead.")
  (bounding_boxes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BoundingBooxes>) ostream)
  "Serializes a message object of type '<BoundingBooxes>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image_header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'bounding_boxes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'bounding_boxes))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BoundingBooxes>) istream)
  "Deserializes a message object of type '<BoundingBooxes>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image_header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'bounding_boxes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'bounding_boxes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'centernet_ros-msg:BoundingBoox))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BoundingBooxes>)))
  "Returns string type for a message object of type '<BoundingBooxes>"
  "centernet_ros/BoundingBooxes")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BoundingBooxes)))
  "Returns string type for a message object of type 'BoundingBooxes"
  "centernet_ros/BoundingBooxes")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BoundingBooxes>)))
  "Returns md5sum for a message object of type '<BoundingBooxes>"
  "37a46cf41c29ddce83a4a450ac620f6e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BoundingBooxes)))
  "Returns md5sum for a message object of type 'BoundingBooxes"
  "37a46cf41c29ddce83a4a450ac620f6e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BoundingBooxes>)))
  "Returns full string definition for message of type '<BoundingBooxes>"
  (cl:format cl:nil "Header header~%Header image_header~%BoundingBoox[] bounding_boxes~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: centernet_ros/BoundingBoox~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%float64 depth~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BoundingBooxes)))
  "Returns full string definition for message of type 'BoundingBooxes"
  (cl:format cl:nil "Header header~%Header image_header~%BoundingBoox[] bounding_boxes~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: centernet_ros/BoundingBoox~%string Class~%float64 probability~%int64 xmin~%int64 ymin~%int64 xmax~%int64 ymax~%float64 depth~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BoundingBooxes>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image_header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'bounding_boxes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BoundingBooxes>))
  "Converts a ROS message object to a list"
  (cl:list 'BoundingBooxes
    (cl:cons ':header (header msg))
    (cl:cons ':image_header (image_header msg))
    (cl:cons ':bounding_boxes (bounding_boxes msg))
))
