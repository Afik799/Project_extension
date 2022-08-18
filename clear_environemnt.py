import requests

try:
    requests.get('http://0.0.0.0:5000/stop_server')
except requests.exceptions.ConnectionError:
    print("one of the servers is not responding, may be down")