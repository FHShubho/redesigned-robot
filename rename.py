import glob
import os

path1 = os.path.dirname(os.path.realpath(__file__))

path = path1 + r'\*'

files = glob.glob(path)
files.sort(key=os.path.getmtime, reverse=False)

count = 1

for f in files:
    f_name = os.path.basename(f)
    if f_name == 'rename.py':
        continue
    else:
        dst = path1 + "\\" + str(count) + '. ' + f_name
        dst = dst[:-3]
        dst = dst + ".mp4"
        os.rename(f, dst)
        #print(dst)
        count += 1
    

print('Rename Completed')