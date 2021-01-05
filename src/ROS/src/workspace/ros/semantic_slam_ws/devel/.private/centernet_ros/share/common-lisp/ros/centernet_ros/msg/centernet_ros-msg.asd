
(cl:in-package :asdf)

(defsystem "centernet_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBox" :depends-on ("_package_BoundingBox"))
    (:file "_package_BoundingBox" :depends-on ("_package"))
    (:file "BoundingBoxes" :depends-on ("_package_BoundingBoxes"))
    (:file "_package_BoundingBoxes" :depends-on ("_package"))
    (:file "deteccion" :depends-on ("_package_deteccion"))
    (:file "_package_deteccion" :depends-on ("_package"))
    (:file "detecciones" :depends-on ("_package_detecciones"))
    (:file "_package_detecciones" :depends-on ("_package"))
  ))