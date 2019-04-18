# Self-Driving-AI
A trial at creating a automated self driving bot for GRID Autosport

We started by Capturing the original frames from the game itself:
## Image Capture
![Image Capture](Captures/1_caputure_edit_0.gif)


***

Furthermore, from the extracted image we had to find the edges, so we implemented edge detection in the retrieved frame as well.
## Edge Detection
![Edge Detection](Captures/2_edge_detection.gif)


***

We do not need all the frame so in order to remove the sky and unnecessary parts, we took out only the below half in shape of a trapezium like in this image.
## Region of Interest
![Edge Detection](Captures/3_region_of_interest.gif)
