
(cl:in-package :asdf)

(defsystem "centernet_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBoxes" :depends-on ("_package_BoundingBoxes"))
    (:file "_package_BoundingBoxes" :depends-on ("_package"))
    (:file "ObjectInfo" :depends-on ("_package_ObjectInfo"))
    (:file "_package_ObjectInfo" :depends-on ("_package"))
    (:file "detecciones" :depends-on ("_package_detecciones"))
    (:file "_package_detecciones" :depends-on ("_package"))
    (:file "DetectedObjects" :depends-on ("_package_DetectedObjects"))
    (:file "_package_DetectedObjects" :depends-on ("_package"))
    (:file "BoundingBox" :depends-on ("_package_BoundingBox"))
    (:file "_package_BoundingBox" :depends-on ("_package"))
  ))