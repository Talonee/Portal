"""Utility functions to display the pose detection results."""
#!/usr/bin/env python3

import cv2
import numpy as np
from tflite_support.task import processor

import serial
import time

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_TEXT_COLOR = (0, 0, 255)  # BG_Red_


def visualize(
    image: np.ndarray,
    detection_result: processor.DetectionResult,
    #ser: serial.Serial
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.

  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.

  Returns:
    Image with bounding boxes.
  """
  
  grass_detected = False

  for detection in detection_result.detections:
    # Define colors for different objects
    category = detection.categories[0]
    category_name = category.category_name
    
    if (category_name == "grass"):
      text_color = (128, 0, 255) # magenta
    elif (category_name == "dirt"):
      text_color = (251, 148, 55) # sky
    else:
      text_color = _TEXT_COLOR  # red
      text_color = (205, 251, 83) # turquoise
		
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, text_color, 3)

    # Draw label and score
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (_MARGIN + bbox.origin_x,
                     _MARGIN + _ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE, text_color, _FONT_THICKNESS)
    
    if (category_name == "grass"): # encapsulate movement to only grass detection
      grass_detected = True;
      #mv_code = serial_output(bbox, ser)

    # Debug
    cv2.circle(image, (round(bbox.origin_x + bbox.width / 2), round(bbox.origin_y + bbox.height / 2)), 
               10, (102, 255, 255), -1)

  # Stop car if no objects detected. Scan surrounding if objs detected but no grass
  #if not detection_result.detections:
  #  mv_code = 4
  #elif not grass_detected:
  #  mv_code = 1

  # send int via Serial requires conversion to str(), then encode('utf-8')
  #ser.write(str(mv_code).encode('utf-8'))


  # Debug 
  width = 640
  height = 350
  cv2.rectangle(image, (round(width / 2 - 50), round(height / 2 - 50)), 
                (round(width / 2 + 50), round(height / 2 + 50)), (102, 255, 255), 3)

  return image

def serial_output(bbox: np.ndarray, ser: serial.Serial) -> int:
  # SD:640x480 HD:1280x720
  width = 640
  bbox_midp = bbox.origin_x + bbox.width / 2
  safe_lim_r = (width / 2 + 50)
  safe_lim_l = (width / 2 - 50)

  # Send signal to move in correspondent to relative bounding box position
  # Middle range buffer: 50 pixels left & right from center
  if (bbox_midp < safe_lim_r) and (bbox_midp > safe_lim_l): # object in safe zone
    mv = 0
  elif (bbox_midp < safe_lim_l): # object on left, turn right (img reversed)
    mv = 3
  elif (bbox_midp > safe_lim_r): # object on right, turn left (img reversed)
    mv = 1
  else:
    mv = 4

  return mv
