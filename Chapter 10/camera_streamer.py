
from flask import Flask, Response, render_template_string
import cv2 # OpenCV for camera capture
import time
import numpy as np

# --- Configuration ---
app = Flask(__name__)

# Initialize the Camera Capture (0 usually refers to the first connected USB camera)
print("Initializing USB Camera...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open USB camera. Please check connection and try again.")
    exit(1)

# Set resolution for efficient streaming
RESOLUTION = (640, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION[1])
print(f"Camera initialized with resolution set to {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}.")

# --- Generator Function for MJPEG Stream ---
def generate_frames():
    """Generator function that yields JPEG frames for the MJPEG stream using OpenCV."""
    try:
        while True:
            # Read a frame from the camera. 'success' is a boolean, 'frame' is the image array.
            success, frame = cap.read()
            if not success:
                continue
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame_bytes = buffer.tobytes()
            # Yield the frame in the standard MJPEG format (with boundary)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            time.sleep(0.05)
    except Exception as e:
        print(f"An error occurred during streaming: {e}")

# --- Web Server Routes ---
@app.route('/')
def index():
    """Home page that displays the video feed."""
    html_content = """
    <html>
    <head>
    <title>Raspberry Pi Surveillance Feed</title>
    <style>body { font-family: sans-serif; text-align: center; background-color: #eee; }</style>
    </head>
    <body>
    <h1>Live USB Camera Feed</h1>
    /video_feed
    <p>Accessible from any device on your local network.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/video_feed')
def video_feed():
    """The route that serves the continuous MJPEG stream."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# --- Main Program Execution ---
if __name__ == '__main__':
    try:
        print("Starting web server on http://<Your-Pi-IP-Address>:8000")
        app.run(host='0.0.0.0', port=8000, debug=False)
    except KeyboardInterrupt:
        print("\nStopping camera stream.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Crucial: Release the camera object when the script stops
        cap.release()
        print("Camera resource released.")
