import os, sys
from PIL import Image
filelist= [file for file in os.listdir() if file.endswith('.png')]
atlas_dict = {'logos.png':{}}
h,w = 6,6
width, height = 200,200  # size of element
total_width = width * w
max_height = height * h
result = Image.new('RGBA', (total_width, max_height))  # common canvas
y_offset = 0
x_offset = 0
for file in filelist:	
    im = Image.open(file)
    result.paste(im, (x_offset, y_offset))
    atlas_dict['logos.png'][file[:-4]]=[x_offset,y_offset,width, height]
    x_offset += width

    if x_offset == total_width:
    	x_offset = 0
    	y_offset += height
atlas = open('logos.atlas', 'w')
atlas.write(str(atlas_dict))
atlas.close()
#result.show()
