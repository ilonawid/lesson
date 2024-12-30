from PIL import Image, ImageFilter
with Image.open("screengrab5.jpg") as im:
    im.rotate(180).show()
    im_blurred = im.filter(filter=ImageFilter.BLUR)
    im_blurred.show()
    print(im.getbands())

import numpy as np
a = np.array([0, 5, 3])
print(a)
print(a.ndim)
print(a.size)