import sys
import os
from itertools import islice
import shutil
import re
import time

files = []
secondCall = True

vidFile = input("Video Path = ")
FPS = input("Video FPS = ")


if os.path.exists('output'):
    shutil.rmtree('output')
    shutil.rmtree('output_2')
    shutil.rmtree('output_3')
os.mkdir('output')
os.mkdir('output_2')
os.mkdir('output_3')

os.system('ffmpeg -i '+vidFile+' -f image2 "output/output_%06d.bmp"')
#
# FIRST CALL
#
for (path, dirnames, filenames) in os.walk('output'):
    files.extend(os.path.join(name) for name in filenames)
for file in islice(files, 2, None, 3):
    print('FIRST: '+file)
    os.replace('output/'+file,'output_2/'+file)
files.clear()
time.sleep(2)
#
# SECOND CALL
#
if secondCall == True:
    for (path, dirnames, filenames) in os.walk('output'):
        files.extend(os.path.join(name) for name in filenames)
    for file in islice(files, 2, None, 2):
        print('FIRST: '+file)
        os.replace('output/'+file,'output_2/'+file)

files.clear()
time.sleep(2)
#Number every 3rd (minus them)
for (path, dirnames, filenames) in os.walk('output_2'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    fileNumber = int(re.sub('.bmp', '', file.split("_",1)[1]))
    print(str(fileNumber) +" is now "+"{0:06}".format(fileNumber -3))

    if str("{0:06}".format(fileNumber -3)) == '-00001':
        os.replace('output_2/'+file,'output_3/'+'output_000001'+'.bmp')
    else:
        os.replace('output_2/'+file,'output_3/'+'output_'+str("{0:06}".format(fileNumber-3))+'.bmp')

files.clear()
time.sleep(2)
#Number every first files (plus them)
for (path, dirnames, filenames) in os.walk('output'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    fileNumber = int(re.sub('.bmp', '', file.split("_",1)[1]))
    print(str(fileNumber) +" is now "+"{0:06}".format(fileNumber +3))
    os.replace('output/'+file,'output_2/'+'output_'+str("{0:06}".format(fileNumber+3))+'.bmp')

files.clear()
time.sleep(2)
for (path, dirnames, filenames) in os.walk('output_2'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    os.replace('output_2/'+file,'output/'+file)
files.clear()
time.sleep(2)
for (path, dirnames, filenames) in os.walk('output_3'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    os.replace('output_3/'+file,'output/'+file)
time.sleep(2)

#d = "output"
#s = "output_2"
#files = sorted(os.listdir(d))

#highest_index = int(re.sub("[^0-9]", "", os.path.splitext(files[-1])[0]))+1

#for i,f in enumerate(sorted(os.listdir(s)),highest_index):
#    new_name = "output_{:06}.bmp".format(i)
#    shutil.copy(os.path.join(s,f),os.path.join(d,new_name))
os.system('rename.py')

os.system('ffmpeg -i "output_2/output_%03d.bmp" -r '+FPS+' video.mp4')