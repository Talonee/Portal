Link to repo: https://github.com/AutonomousLawnmower/computer-vision.git

## Context: 
The desired outcome was to have the object detection model operate fast enough such that our lawnmower can navigate in real-time without much help from the sensors. A test was made to see how responsive the wheels are to the image capturing speed, the wheels moved continuously while the images output to 4-6 FPS. This difference results in the situation where the images haven't caught up to the actual, real-time position but the wheels continue to run at full speed due to the images being used as indicators--a undesirable lag. To circumvent this effect, researches and a few approaches were attempted to increase the frames output.

## Notes:

#### Approach 1: Overclocking
FPS improves if the Pi is overclocked (+1 FPS) but throttles hard if maintaining a high activation over long-term (-2 FPS).
- Average temperature:
   - Resting: 50&deg;
   - Active model (1.5 GHz): 83&deg;
   - Active model (2.0 GHz): 84&deg;
- Average frequency:
   - Resting: 0.6 GHz
   - Active model (1.5 GHz): 1.6 GHz
   - Active model (2.0 GHz): 1.78 GHz

Using the same ML model as benchmark, overall performance doesn't differ much despite overclocking. Temperature consistently peaked around 83&deg regardless which mode it was in (default vs. overclocked), same goes for the frequency. I can only assume the model automatically consume for itself all the resources available to maximize performance. 

#### Approach 2: Remove VNC Viewer being the display port component
FPS improves if working without the VNC Viewer, which draws extra resources for streaming (+/- 2 FPS). A frame rate increase of 2 frames can mean 30%-50% improvement; such a change is noticable. Directly connecting the Pi to an external monitor or SSH from a separate device ensures we get the accurate representation of how much FPS we can expect.

#### Approach 3: Remove color filter (red/yellow) and image masking
Zero effects although thereotically expected. Regardless of whether our images are masked to be mostly black, white, or fully colored, the model scan images on a pixel-by-pixel basis, therefore, the output is all the same. Additionally, color filtering may be counterproductive/unnecessary as we want to avoid reliance on colors anyway and, instead, focus on learning the general shapes and compositions of *multiple* objects.

#### Approach 4: Pi camera over webcam
Type of cable can affect USB webcam's resolution. A regular USB-C interface locks the resolution to 640x360 when attempting to change through python-cv2. The proprietary cable that came with the webcam, however, allows the webcam to change anywhere between 640x360 to 1920x1080--resolution may possibly be greater than the FHD range, but cannot go lower than the minimum. However, since image resolution scales inversely with FPS: lower resolution -> higher FPS, higher resolution -> lower FPS; lower resolution is the preferred choice to maximize FPS.

Switching out the webcam for the Pi camera, without the object detection model, frames rate breaks to a record 120-130 FPS. Interesting, but unfortunately, the FPS is minimally affect, if at all, when applied the EfficientDet model(s). Nevertheless, the Pi camera will be used for 3 main benefits: a dedicated camera slot on the Pi board frees up a USB slot that would've otherwise been occupied by the webcam, being much lighter in weight means easier placement on the vehicle. 

#### Approach 5: Object detection model choices between speed vs. accuracy
FPS can be improved using different object detection models:
   - No model: Maximum uncapped FPS allowed (30 - 130 FPS)
   - Efficientdet0: 8.5 FPS
   - Efficientdet1: 6.2 FPS

#### Approach 6: Reformatting Raspberry Pi OS's processor
The default processor for the Pi has been a 32-bit system, but we can boost the overall computational power and memory addresses using the recently released 64-bit processor version designed for the Raspberry Pi 4. The outcome:
   - An Efficientdet0 model averaging around 8.5 FPS on the 32-bit system increases to an average 13.5 FPS on the 64-bit. A 58.82% increase, how about that?

### Solution:
Overall, only approaches 2, 4, 5, and 6 yielded some form of success that brings a meaningful addition to the project. Although 13 FPS proves to be more viable and elimiates the lagging effect, in lieu of using the machine learning model with the least accuracy, computer vision alone will not be the sole determiner to drive the autonomous vehicle. The set of 4 ultrasonic sensors will instead take on that role, while the 13 FPS performance is used for occasional object detection when we need to identify if the objects ahead is potentially hazardous.

### Tools:
- Install labelImg for labeling: https://gpiocc.github.io/learn/ml/2021/08/28/martin-ku-create-object-detection-dataset-with-labelimg.html
- Raspberry Pi 64-bit breaks the picamera completely and, along with it, legacy Python libraries that support it. Here is the alternative, PiCamera2: sudo apt install -y python3-picamera2
