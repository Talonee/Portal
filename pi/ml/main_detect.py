from imutils.video import VideoStream
import imutils, time, cv2

import argparse
import sys
import time

import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

import serial

# initialize the video stream and allow the camera sensor to
# warmup
vs = VideoStream(usePiCamera=1).start()
time.sleep(2.0)

def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool, ser: serial.Serial) -> None:
    global frame

    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = time.time()
  
    # Start capturing video input from the camera
    #cap = cv2.VideoCapture(camera_id)
    #vs = VideoStream(usePiCamera=1).start()
    #vs.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    #vs.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #time.sleep(2.0)

    # Visualization parameters
    row_size = 22  # pixels
    left_margin = 24  # pixels
    text_color = (128, 0, 255)  # magenta # red
    font_size = 1.2
    font_thickness = 2
    fps_avg_frame_count = 10
  
    # Initialize the object detection model
    base_options = core.BaseOptions(
        file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
    detection_options = processor.DetectionOptions(
        max_results=2, score_threshold=0.6)
    options = vision.ObjectDetectorOptions(
        base_options=base_options, detection_options=detection_options)
    detector = vision.ObjectDetector.create_from_options(options)

    while True:
        frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #frame_bigger = cv2.resize(frame, (500,500), interpolation = cv2.INTER_AREA)

        counter += 1
        image = cv2.flip(frame, 1)
        image = cv2.resize(frame, (width,height), interpolation = cv2.INTER_AREA)



        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Create a TensorImage object from the RGB image.
        input_tensor = vision.TensorImage.create_from_array(rgb_image)
    
        # Run object detection estimation using the model.
        detection_result = detector.detect(input_tensor)
    
        # Draw keypoints and edges on input image
        image = utils.visualize(image, detection_result, ser)

        # Calculate the FPS
        if counter % fps_avg_frame_count == 0:
          end_time = time.time()
          fps = fps_avg_frame_count / (end_time - start_time)
          start_time = time.time()
    
        # Show the FPS
        fps_text = 'FPS = {:.1f}'.format(fps)
        text_location = (left_margin, row_size)
        cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    font_size, text_color, font_thickness)



        # Stop the program if the ESC key is pressed.
        if cv2.waitKey(1) == 27:
          break
        cv2.imshow('object_detector', image)

    cap.release()
    cv2.destroyAllWindows()

        #cv2.imshow("Live Video", image)
        #cv2.waitKey(50)





def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Path of the object detection model.',
      required=False,
      default='efficientdet_lite0.tflite')
  parser.add_argument(
      '--cameraId', help='Id of camera.', 
      required=False, type=int, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      type=int,
      default=640) # SD:640x480 HD:1280x720
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      type=int,
      default=360) # SD:640x480 HD:1280x720
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      type=int,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  args = parser.parse_args()

  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.reset_input_buffer()

  run(args.model, int(args.cameraId), args.frameWidth, args.frameHeight,
      int(args.numThreads), bool(args.enableEdgeTPU), ser)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        vs.stop() # release the video stream pointer
        
    
