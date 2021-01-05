import pyrealsense2 as rs
import numpy as np
import cv2
import os
#import keyboard
import time

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

align = rs.align(rs.stream.color)

#path = os.path.join(os.path.dirname(os.getcwd()), 'data')
#path = os.path.join(path, 'realsense/images')

path = '/home/guillermo/Escritorio/images'#/media/guillermo/60F9-DB6E/external/images'

a = len(os.listdir(os.path.join(path, 'rgb')))

i = a

try:
    while True:
        i = i + 1
        time.sleep(0.05) #quitar esto para grabar test
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        depth_frame = aligned_frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        cv2.imwrite(os.path.join(os.path.join(path, 'd'), str(i) + '.pgm'), depth_image)
        cv2.imwrite(os.path.join(os.path.join(path, 'rgb'), str(i) + '.ppm'), color_image)

        colorizer = rs.colorizer()
        depth_image_colorized = np.asanyarray(colorizer.colorize(depth_frame).get_data())

        # Show images
        combined = cv2.addWeighted(color_image, 0.5, depth_image_colorized, 0.5, 0)
        cv2.namedWindow('RGB-D', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RGB-D', combined)
        cv2.waitKey(1)

except KeyboardInterrupt:

    # Stop streaming
    pipeline.stop()



