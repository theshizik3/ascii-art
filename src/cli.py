from src.convert import convert
from PIL import Image

import argparse


def main():
    parser = argparse.ArgumentParser(description="ASCII converter")
    
    parser.add_argument("input", type=str, help="input image")    
    parser.add_argument("--width", type=int, default=0, help="output image width")
    parser.add_argument("--height", type=int, default=0, help="output image height")
    parser.add_argument("--charw", type=int, default=2, help="number of characters per pixel horizontally")
    parser.add_argument("--chars", type=str, default="@&#*+=;,:'_-`. ", help="output image height")
    parser.add_argument("--output", type=str, default="stdout", help="where the ascii art will be output")
    
    args = parser.parse_args()

    img = Image.open(args.input)
    
    CHARS = tuple(args.chars)
    
    res = convert(
        img=img,
        chars=CHARS,
        char_width=args.charw,
        width=args.width,
        height=args.height
    )
    
    if args.output == "stdout":
        print(res)
    else:
        with open(args.output, 'w') as f:
            f.write(res)
    