from __future__ import print_function
import requests
import json
import cv2
from skimage import io, color, img_as_ubyte, feature

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = io.imread('https://images.unsplash.com/photo-1607690424560-35d967d6ad7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZWdnfGVufDB8fDB8fA%3D%3D&w=1000&q=80')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)
# decode response
print(json.loads(response.text))