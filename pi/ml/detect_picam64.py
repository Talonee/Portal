from picamera2 import Picamera2
import time, cv2, argparse, sys, serial

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils


cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(
    main={"format": 'XRGB8888', "size": (width, height)}))

def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:
    global frame
    
    picam2.start()

    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = time.time()
  
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
        image = picam2.capture_array()

        counter += 1
        image = cv2.flip(image, 1)
        #image = cv2.resize(image, (width,height), interpolation = cv2.INTER_AREA)
        
        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a TensorImage object from the RGB image.
        input_tensor = vision.TensorImage.create_from_array(rgb_image)
    
        # Run object detection estimation using the model. 
        # Brain of the operation, causal of 8 FPS.
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

        # (Q)uit the program if key is pressed.
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
        cv2.imshow('Live cam', image)
    
    picam2.stop()
    cv2.VideoCapture(0).release()
    cv2.destroyAllWindows()

def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Path of the object detection model.',
      required=False,
      default='grass0_new.tflite')
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

  run(args.model, int(args.cameraId), args.frameWidth, args.frameHeight,
      int(args.numThreads), bool(args.enableEdgeTPU))


if __name__ == '__main__':
    main()
        
    
