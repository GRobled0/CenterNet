cmake_minimum_required(VERSION 2.8.3)

set(PROJECT_NAME centernet_ros)
project(${PROJECT_NAME})

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_LIST_DIR}/cmake")


set(CENTERNET_ROS_SOURCE_DIR
    src)

set(CENTERNET_ROS_INCLUDE_DIR
    src
    )

FILE(GLOB_RECURSE CENTERNET_ROS_SOURCE_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/src/*.py
    ${CMAKE_CURRENT_SOURCE_DIR}/src/detectors/*.py
    ${CMAKE_CURRENT_SOURCE_DIR}/src/eternal/*.py
    ${CMAKE_CURRENT_SOURCE_DIR}/src/models/*.py
    ${CMAKE_CURRENT_SOURCE_DIR}/src/utils/*.py)


find_package(catkin REQUIRED
    COMPONENTS rospy std_msgs sensor_msgs image_transport tf_conversions tf message_generation cv_bridge image_transport)

find_package(OpenCV REQUIRED)

catkin_python_setup()


add_message_files(
    FILES
    BoundingBox.msg
    BoundingBoxes.msg
    deteccion.msg
    detecciones.msg
    )

generate_messages(
    DEPENDENCIES
    std_msgs
    sensor_msgs
    )

catkin_package(
    LIBRARIES OpenCV
    CATKIN_DEPENDS rospy std_msgs sensor_msgs image_transport tf_conversions tf message_runtime cv_bridge image_transport
    )


include_directories(${catkin_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})


catkin_install_python(PROGRAMS src/detector.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
