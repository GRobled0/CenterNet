; Auto-generated. Do not edit!


(cl:in-package semantic_SLAM-msg)


;//! \htmlinclude ObjectInfo.msg.html

(cl:defclass <ObjectInfo> (roslisp-msg-protocol:ros-message)
  ((type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (prob
    :reader prob
    :initarg :prob
    :type cl:float
    :initform 0.0)
   (tl_x
    :reader tl_x
    :initarg :tl_x
    :type cl:integer
    :initform 0)
   (tl_y
    :reader tl_y
    :initarg :tl_y
    :type cl:integer
    :initform 0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0))
)

(cl:defclass ObjectInfo (<ObjectInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name semantic_SLAM-msg:<ObjectInfo> is deprecated: use semantic_SLAM-msg:ObjectInfo instead.")))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:type-val is deprecated.  Use semantic_SLAM-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'prob-val :lambda-list '(m))
(cl:defmethod prob-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:prob-val is deprecated.  Use semantic_SLAM-msg:prob instead.")
  (prob m))

(cl:ensure-generic-function 'tl_x-val :lambda-list '(m))
(cl:defmethod tl_x-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:tl_x-val is deprecated.  Use semantic_SLAM-msg:tl_x instead.")
  (tl_x m))

(cl:ensure-generic-function 'tl_y-val :lambda-list '(m))
(cl:defmethod tl_y-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:tl_y-val is deprecated.  Use semantic_SLAM-msg:tl_y instead.")
  (tl_y m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:width-val is deprecated.  Use semantic_SLAM-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ObjectInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader semantic_SLAM-msg:height-val is deprecated.  Use semantic_SLAM-msg:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectInfo>) ostream)
  "Serializes a message object of type '<ObjectInfo>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'type))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'prob))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'tl_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'tl_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectInfo>) istream)
  "Deserializes a message object of type '<ObjectInfo>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prob) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tl_x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tl_y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectInfo>)))
  "Returns string type for a message object of type '<ObjectInfo>"
  "semantic_SLAM/ObjectInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectInfo)))
  "Returns string type for a message object of type 'ObjectInfo"
  "semantic_SLAM/ObjectInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectInfo>)))
  "Returns md5sum for a message object of type '<ObjectInfo>"
  "55a63526fe7c32ce41ef4e85ff85bb42")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectInfo)))
  "Returns md5sum for a message object of type 'ObjectInfo"
  "55a63526fe7c32ce41ef4e85ff85bb42")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectInfo>)))
  "Returns full string definition for message of type '<ObjectInfo>"
  (cl:format cl:nil "string type~%float32 prob~%int32 tl_x~%int32 tl_y~%int32 width~%int32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectInfo)))
  "Returns full string definition for message of type 'ObjectInfo"
  (cl:format cl:nil "string type~%float32 prob~%int32 tl_x~%int32 tl_y~%int32 width~%int32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectInfo>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'type))
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectInfo
    (cl:cons ':type (type msg))
    (cl:cons ':prob (prob msg))
    (cl:cons ':tl_x (tl_x msg))
    (cl:cons ':tl_y (tl_y msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
))
