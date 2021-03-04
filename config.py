
# The port to be used by the Flask server
FLASK_SERVER_PORT = 8181

# A list of IP addresses that are allowed to access the endpoint.
ALLOWED_REMOTE_IP_ADDRESSES = ['127.0.0.1', '35.155.73.2']

# A dict of camera ids and their RTSP urls.
cameras = {
    "WP6XcgtOr2": "rtsp://multipolar:t3rp999@192.168.0.102/live"
}