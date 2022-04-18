import requests
import json
import cv2
from skimage import io

addr = 'https://babahaha-glcm.herokuapp.com'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = io.imread(
    'https://media.istockphoto.com/photos/egg-isolated-on-black-picture-id118361301?k=20&m=118361301&s=612x612&w=0&h=Z1d5d_Q_76KyRv4earP_XDyc4Nnz7The9CRvHlnE_FA=')
    
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)

# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)

# decode response
data = json.loads(response.text)
print(data)
