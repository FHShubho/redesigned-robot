import os
import glob
from PIL import Image

#current directory
path = os.path.dirname(os.path.realpath(__file__))

#class names
class_label = 27

print('Reading image files...')
path_1 = path + r'\*.jpg'
img_files = glob.glob(path_1)

total = len(img_files)
total_count = 0
invalid_files = []

for files in img_files:
    try:
        f_name = os.path.basename(files)
        output = f_name[:-3]
        output = output + 'txt'
        #print(files)
        im = Image.open(files)
        #print(im.size)
        width, height = im.size

        xmin = 2
        ymin = 2
        xmax = width-2
        ymax = height-2

        x = (xmax + xmin) / (width * 2)
        y = (ymax + ymin) / (height * 2)
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height

        #print(x, " ", y, " ", w, " ", h)

        #writing to text file
        with open(path + '\\' + output, 'a+') as output_file:
            output_file.write(' '.join([str(class_label), str(x), str(y), str(w), str(h) + '\n']))
        
        total_count += 1
        print(total_count, 'generated out of', total)

    except:
            print(os.path.basename(files), 'Invalid file')
            invalid_files.append(os.path.basename(files)+'\n')

print('\nCompleted')
print(total_count, ' annotations generated successfully\n')

if len(invalid_files) > 0:
    with open(path + '\\' + 'invalid_files.txt', 'a+') as output_file:
        output_file.write(str(invalid_files))
    print(total - total_count, 'ivalid files')
    print('See invalid file list in invalid_files.txt')
