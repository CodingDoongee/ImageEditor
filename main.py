import numpy as np
from PIL import Image


def FilterOneColor(color):
    img_name = 'my_img.png'
    im = Image.open(img_name)

    pix = np.array(im)

    for i in range(pix.shape[0]):
        for j in range(pix.shape[1]):
            if (pix[i][j] == color).all():
                continue
            else:
                pix[i][j] = [0, 0, 0, 0]
    img = Image.fromarray(pix, 'RGBA')
    img.save('my_img2.png')


Color = [0, 188, 212, 255]
FilterOneColor(Color)
