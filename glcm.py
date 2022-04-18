import numpy as np
from skimage import io, color, img_as_ubyte, feature
import cv2
from flask import Flask, request, Response
import jsonpickle

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
    rgbImg = io.imread(
        'https://ichef.bbci.co.uk/news/976/cpsprodpb/7614/production/_105482203__105172250_gettyimages-857294664.jpg')
    grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

    # cv2.imshow("test img", grayImg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    properties = ['energy', 'contrast', 'homogeneity', 'correlation']

    glcm = feature.graycomatrix(grayImg,
                                distances=[1],
                                angles=[0],
                                symmetric=True,
                                normed=True)

    feats = np.hstack([feature.graycoprops(glcm, prop).ravel()
                       for prop in properties])

    entropy = -np.sum(glcm*np.log2(glcm + (glcm == 0)))

    result = {"energy": feats[0].tolist(), "contrast": feats[1].tolist(),
              "homogenity": feats[2].tolist(), "correlation": feats[3].tolist(), "entropy": entropy.tolist()}

    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(result)
    print(response_pickled)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run()
