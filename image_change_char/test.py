#import library and module
from PIL import Image
import argparse

#process imput command-line parm
parser = argparse.ArgumentParser()
parser.add_argument('files')
parser.add_argument('-o', '--output', action='store_true')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#get para
args = parser.parse_args()
IMG = args.files
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

#fun for 260 gray mapped 70 character
def map_char(r, g, b, alpha=255):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(r*0.2126 + 0.7152*g + b*0.0722)
    unit = (float(alpha+1) + 1) / length
    return ascii_char[int(gray/unit)]

#main
if __name__ == '__main__':
    image = Image.open(IMG)
    image = image.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += map_char(*image.getpixel((j,i)))
        txt += '\n'
    print txt

#put finished image to file and output
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
          







