from PIL import Image
from typing import Sequence

import numpy as np


def convert(img: Image, chars: Sequence[str], char_width=2, **kwargs) -> str:
    if not (("width" in kwargs) or ("height" in kwargs)):
        raise TypeError("Neither the height nor the width of the output image is specified.")
    
    k = 256//len(chars)
    
    img = img.convert("L")
    
    size = img.size

    if "width" in kwargs:
        w = kwargs.get("width")
        size = (w, int(size[1]*(w/size[0])))
    else:
        h = kwargs.get("width")
        size = (int(size[0]*(h/size[1])), h)
        
    img = img.resize(size)
    
    img_arr = np.array(img)
    
    res = ""
    
    for y in range(size[1]):
        for x in range(size[0]):
           pix = img_arr[y, x]
           res += chars[pix//k]*char_width
        res += "\n"
        
    return res
