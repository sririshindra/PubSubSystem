
import requests
from time import sleep

while True:
    r = requests.post("http://localhost:5000/publish", data={'topic': "dummy_topic", 'message': 'issue', 'action': 'show'})
    print(r.status_code, r.reason)
    sleep(0.2)
