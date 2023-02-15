## Context: 
The desired outcome was to have the object detection model operate fast enough such that our lawnmower can navigate in real-time without much help from the sensors. A test was made to see how responsive the wheels are to the image capturing speed, the wheels moved continuously while the images output to 4-6 FPS. This difference results in the situation where the images haven't caught up to the actual, real-time position but the wheels continue to run at full speed due to the images being used as indicators--a undesirable lag. To circumvent this effect, a lot of research and approaches were attempted to increase the frames output.

## Notes:
- Type of cable can affect USB webcam's resolution. A regular USB-C interface locks the resolution to 640x360 when attempting to change through python-cv2. The proprietary cable that came with the webcam, however, allows the webcam to change anywhere between 640x360 to 1920x1080--resolution may possibly be greater than the FHD range, but cannot go lower than the minimum.
- Image resolution scales inversely with FPS.
- FPS can be improved using different object detection models:
   - No model: 30.0 FPS
   - Efficientdet0: 8.5 FPS
   - Efficientdet1: 6.2 FPS
- FPS improves if working without VNC Viewer (+/- 2 FPS).
- FPS improves if overclocked (+1 FPS) but throttles hard if high activation over long-term (-2 FPS).
- Average temperature:
   - Resting: 50&deg;
   - Active model (1.5 GHz): 83&deg;
   - Active model (2.0 GHz): 84&deg;
- Average frequency:
   - Resting: 0.6 GHz
   - Active model (1.5 GHz): 1.6 GHz
   - Active model (2.0 GHz): 1.78 GHz

#### Approach 1: Overclocking
The ML model doesn't differ much despite overclocking away from the default frequency of the Pi4. My temperature peaked around 83&deg; regardless which mode it was in (default vs. overclocked), same goes for the frequency. I can only assume the model automatically consume for itself all the resources available to maximize performance. 

#### Approach 2: Remove VNC Viewer being the display port component
A frame rate increase of 2 frames means 30%-50% improvement; such a change is noticable.

#### Approach 3: Remove color filter (red/yellow) and image masking
Zero effects although thereotically expected. Regardless of whether our images are masked to be mostly black, white, or fully colored, the model scan images on a pixel-by-pixel basis, therefore, the output is all the same. Additionally, color filtering may be counterproductive/unnecessary as we want to avoid reliance on colors anyway and, instead, focus on learning the general shapes and compositions of *multiple* objects.

#### Approach 4: Pi camera over webcam
Switching out the webcam for the Pi camera, no object detection model, frames rate breaks to a record 120-130 FPS. Interesting. Unfortunately, the FPS remain unchanged when applied the EfficientDet model(s).

### Solution:
At best, we use the ultrasonic sensors to determine movements and maintain a ~8 FPS performance for occasional object detection when we need to identify if the objects ahead is potentially hazardous or not.
