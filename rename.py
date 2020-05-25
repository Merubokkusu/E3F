import os,shutil,re

_src = "output/"
_ext = ".bmp"
for i,filename in enumerate(os.listdir(_src)):
    if filename.endswith(_ext):
        os.rename(_src+filename, 'output_2/output_' + str(i).zfill(3)+_ext)
        print(' file '+filename+' is '+str(i).zfill(3)+_ext)