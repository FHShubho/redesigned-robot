import glob
import os
from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))
path = path + r'\*.png'
files = glob.glob(path)

for f in files:
    #print(f)
    png = Image.open(f)
    png = png.convert('RGB')
    output = f[:-4]
    output = output + '.pdf'
    png.save(output, optimize = False)

print('Conversion finished')

