import numpy as np
from skimage import io, color, img_as_ubyte, feature

rgbImg = io.imread(
    'https://images.unsplash.com/photo-1607690424560-35d967d6ad7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZWdnfGVufDB8fDB8fA%3D%3D&w=1000&q=80')
grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

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

print('glcm: ', feats)
