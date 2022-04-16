from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
from skimage import color, img_as_ubyte, feature

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # glcm
    grayImg = img_as_ubyte(color.rgb2gray(img))

    distances = [1, 2, 3]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
    properties = ['energy', 'homogeneity']

    glcm = feature.graycomatrix(grayImg,
                                distances=distances,
                                angles=angles,
                                symmetric=True,
                                normed=True)

    feats = np.hstack([feature.graycoprops(glcm, prop).ravel()
                       for prop in properties])

    # build a response dict to send back to client
    response = {'glcm ': feats.tolist()}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    print(response_pickled)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run()
