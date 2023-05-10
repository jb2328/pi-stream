pi-stream
=====================
Enables easy Pi-based web streaming

# Running Flask App with Command-Line Arguments

This document provides instructions on how to run the Flask app with command-line arguments for specifying the port number, resolution, and frame rate.

## Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3 or above)
- Flask (Python web framework)

## Steps

1. Clone the repository or download the Flask app files to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the Flask app files are located.

3. Install the required dependencies by running the following command in a venv:

`pip install flask`  

or 

`pip install -r requirements-pi.txt`

4. Run the Flask app with the desired command-line arguments using the following format:

`python app.py --port <port_number> --resolution <width> <height> --framerate <frame_rate>`

- `<port_number>`: Specify the port number to run the Flask app. If not provided, it will default to `8899`.
- `<width>` and `<height>`: Specify the resolution of the app window. If not provided, it will default to `1920x1080`.
- `<frame_rate>`: Specify the frame rate of the app. If not provided, it will default to `32`.

Note: 

* Pi Camera Module v1 resolution - `2592 × 1944` pixels
* Pi HQ Camera resolution - `4056 x 3040` pixels

**Example:**

`python app.py --port 7777 --resolution 1280 720 --framerate 60`

5. Once the Flask app is running, you will see the following output in the terminal:

`Running on http://0.0.0.0:7777/ (Press CTRL+C to quit)`

This indicates that the app is running successfully.

6. Open a web browser and navigate to `http://localhost:<port_number>/` (replace `<port_number>` with the actual port number specified in step 4). You should see the message "Hello, World!" displayed in the browser.

7. To stop the Flask app, go back to the terminal and press `CTRL+C`.

## Conclusion

By following these steps, you can easily run the Flask app with command-line arguments to customize the port number, resolution, and frame rate. Enjoy using the Flask app with your desired configurations!

Based on https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited
