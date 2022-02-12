#Requirements for this script: imageio and ffmpeg!
import sys
import os
from itertools import islice
import shutil
import re
import time
import imageio #use pip to install Imageio and Imageio-ffmpeg
print("::::::::::  ::::::::  ::::::::::")
print(":+:        :+:    :+: :+:")
print("+:+               +:+ +:+")
print("+#++:++#       +#++:  :#::+::#")
print("+#+               +#+ +#+")
print("#+#        #+#    #+# #+#")
print("##########  ########  ###")
print("WELCOME!!! Get ready to mess some videos!")
files = []
secondCall = True
vidFile = input("Enter Video Path : ")
#check if video file exists
while not os.path.exists(vidFile):
    print("No such file in the directory!")
    vidFile = input("Enter Video Path : ")
read=imageio.get_reader(vidFile)
FPS = str(int(read.get_meta_data()['fps'])) #Original FPS will be output FPS
print("Loading...")
#Delete old stuff if exists
if os.path.exists('output'):
    shutil.rmtree('output')
    shutil.rmtree('output_2')
    shutil.rmtree('output_3')
os.mkdir('output')
os.mkdir('output_2')
os.mkdir('output_3')
#Start the fun!
os.system(f'ffmpeg -i '+vidFile+' -f image2 "output/output_%06d.bmp"')
#
# FIRST CALL
#
print("Step 1: Extracting frames!")
for (path, dirnames, filenames) in os.walk('output'):
    files.extend(os.path.join(name) for name in filenames)
for file in islice(files, 2, None, 3):
    print('FIRST: '+file)
    os.replace('output/'+file,'output_2/'+file)
files.clear()
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
#Number every 3rd frame (minus them)
print("Step 2: Rearranging the frames!")
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
#Number every first files (plus them)
for (path, dirnames, filenames) in os.walk('output'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    fileNumber = int(re.sub('.bmp', '', file.split("_",1)[1]))
    print(str(fileNumber) +" is now "+"{0:06}".format(fileNumber +3))
    os.replace('output/'+file,'output_2/'+'output_'+str("{0:06}".format(fileNumber+3))+'.bmp')
files.clear()
for (path, dirnames, filenames) in os.walk('output_2'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    os.replace('output_2/'+file,'output/'+file)
files.clear()
for (path, dirnames, filenames) in os.walk('output_3'):
    files.extend(os.path.join(name) for name in filenames)
for file in files:
    os.replace('output_3/'+file,'output/'+file)
#Extraction done
#os.system('rename.py') no longer needed
_src = "output/"
_ext = ".bmp"
for i,filename in enumerate(os.listdir(_src)):
    if filename.endswith(_ext):
        os.rename(_src+filename, 'output_2/output_' + str(i).zfill(3)+_ext)
        print(' file '+filename+' is '+str(i).zfill(3)+_ext)
print("Step 3: Converting the video!")
if os.path.exists("video.mp4"):
    os.remove("video.mp4") #remove old video.mp4 file if exists
os.system(f'ffmpeg -i "output_2/output_%03d.bmp" -r '+FPS+' video.mp4')
#the output video is corrupted so have to convert it using imageio
reader=imageio.get_reader("video.mp4")
outfile=vidFile[:-4]+"_E3F_output_video.mp4"
writer= imageio.get_writer(outfile, fps=float(FPS))
for frames in reader:
        print(frames)
        writer.append_data(frames)
writer.close()
os.remove("video.mp4")
#Delete these folders to save space!
shutil.rmtree('output')
shutil.rmtree('output_2')
shutil.rmtree('output_3')
#Done message
print(":::::::::   ::::::::  ::::    ::: ::::::::::   :::")
print(":+:    :+: :+:    :+: :+:+:   :+: :+:          :+:")
print("+:+    +:+ +:+    +:+ :+:+:+  +:+ +:+          +:+")
print("+#+    +:+ +#+    +:+ +#+ +:+ +#+ +#++:++#     +#+")
print("+#+    +#+ +#+    +#+ +#+  +#+#+# +#+          +#+")
print("#+#    #+# #+#    #+# #+#   #+#+# #+#  ")
print("#########   ########  ###    #### ##########   ###")
print("Your video is baked - "+outfile)
print("Rerun to use it again!")
time.sleep(2)
#Modified by Akascape 
#Orignal script by Merubokkusu
