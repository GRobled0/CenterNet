import pyrealsense2 as rs
import numpy as np
import cv2
import os
#import keyboard
import time

import datasetmaker as dm

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)


path = os.path.join(os.path.dirname(os.getcwd()), 'data')
path = os.path.join(path, 'realsense/images')

a = len(dm.carga_imagenes(os.path.join(path, 'rgb')))
b = len(dm.carga_imagenes(os.path.join(path, 'd')))

i = a

try:
    while True:
        i = i + 1
        time.sleep(0.05) #quitar esto para grabar test
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        cv2.imwrite(os.path.join(os.path.join(path, 'd'), str(i) + '.pgm'), depth_image)
        cv2.imwrite(os.path.join(os.path.join(path, 'rgb'), str(i) + '.ppm'), color_image)

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()



