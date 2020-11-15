; Auto-generated. Do not edit!


(cl:in-package semantic_SLAM-msg)


;//! \htmlinclude DetectedObjects.msg.html

(cl:defclass <DetectedObjects> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (objects
    :reader objects
    :initarg :objects
    :type (cl:vector semantic_SLAM-msg:ObjectInfo)
   :initform (cl:make-array 0 :element-type 'semantic_SLAM-msg:ObjectInfo :initial-element (cl:make-instance 'semantic_SLAM-msg:ObjectInfo))))
)

(cl:defclass DetectedObjects (<DetectedObjects>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectedObjects>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectedObjects)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name semantic_SLAM-msg:<DetectedObjects> is deprecated: use semantic_SLAM-msg:DetectedObjects instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DetectedObjects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:header-val is deprecated.  Use semantic_SLAM-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <DetectedObjects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:objects-val is deprecated.  Use semantic_SLAM-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectedObjects>) ostream)
  "Serializes a message object of type '<DetectedObjects>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectedObjects>) istream)
  "Deserializes a message object of type '<DetectedObjects>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'semantic_SLAM-msg:ObjectInfo))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectedObjects>)))
  "Returns string type for a message object of type '<DetectedObjects>"
  "semantic_SLAM/DetectedObjects")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectedObjects)))
  "Returns string type for a message object of type 'DetectedObjects"
  "semantic_SLAM/DetectedObjects")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectedObjects>)))
  "Returns md5sum for a message object of type '<DetectedObjects>"
  "a74ced4691e2f209ce4fbe3dd6d24c31")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectedObjects)))
  "Returns md5sum for a message object of type 'DetectedObjects"
  "a74ced4691e2f209ce4fbe3dd6d24c31")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectedObjects>)))
  "Returns full string definition for message of type '<DetectedObjects>"
  (cl:format cl:nil "Header header~%ObjectInfo[] objects~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: semantic_SLAM/ObjectInfo~%string type~%float32 prob~%int32 tl_x~%int32 tl_y~%int32 width~%int32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectedObjects)))
  "Returns full string definition for message of type 'DetectedObjects"
  (cl:format cl:nil "Header header~%ObjectInfo[] objects~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: semantic_SLAM/ObjectInfo~%string type~%float32 prob~%int32 tl_x~%int32 tl_y~%int32 width~%int32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectedObjects>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectedObjects>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectedObjects
    (cl:cons ':header (header msg))
    (cl:cons ':objects (objects msg))
))
