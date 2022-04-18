import requests
import json
import cv2
from skimage import io

addr = 'http://localhost:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = io.imread(
    'https://ichef.bbci.co.uk/news/976/cpsprodpb/7614/production/_105482203__105172250_gettyimages-857294664.jpg')
    
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)

# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)

# decode response
data = json.loads(response.text)
print(data['energy'])
