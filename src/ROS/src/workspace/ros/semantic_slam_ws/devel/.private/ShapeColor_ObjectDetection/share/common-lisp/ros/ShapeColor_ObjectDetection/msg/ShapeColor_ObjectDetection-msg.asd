
(cl:in-package :asdf)

(defsystem "ShapeColor_ObjectDetection-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "DetectedObjects" :depends-on ("_package_DetectedObjects"))
    (:file "_package_DetectedObjects" :depends-on ("_package"))
    (:file "ObjectInfo" :depends-on ("_package_ObjectInfo"))
    (:file "_package_ObjectInfo" :depends-on ("_package"))
  ))