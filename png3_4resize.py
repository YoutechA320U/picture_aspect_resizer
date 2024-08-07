from PIL import Image, ImageDraw
import math
import sys
import pathlib

args = sys.argv

exclulists,pnglists = [],[]
exclupath = pathlib.Path(args[1]).glob('3_4_*.png')
for e in exclupath:
    exclulists.append(e.name)
pngpath = pathlib.Path(args[1]).glob('*.png')
for p in pngpath:
    pnglists.append(p.name)
for pe in  range(len(exclulists)):
    pnglists.remove(exclulists[pe])
print (args[1])
#print(exclulists)
print(pnglists)

for pr in range(len(pnglists)):
 img = Image.open(args[1]+pnglists[pr])

 width, height = img.size
 print(width, height)
 if width/height <= 3/4:
  re_height = height/1440
  if re_height > 1 :
     re_width = math.ceil(width/re_height)
  elif re_height <= 1 :
     re_height = 1440/height
     re_width = math.ceil(width*re_height)
  re_img = img.resize((re_width, 1440))
  width, height = re_img.size
  y_coordi = int((1080-width)/2)
  back_imga = Image.new('RGBA',(width, height),color=(0,0,0,0))
  back_img = Image.new('RGBA',(1080,1440),color=(0,0,0,255))
  back_img.paste(back_imga, (y_coordi, 0)) 
  back_img.paste(re_img, (y_coordi, 0)) 

 if width/height > 3/4:
  re_width = width/1080
  if re_width > 1 :
     re_height = math.ceil(height/re_width)
  elif re_width <= 1 :
     re_width = 1080/width
     re_height = math.ceil(height*re_width)
  re_img = img.resize((1080, re_height))
  width, height = re_img.size
  x_coordi = int((1440-height)/2)
  back_imga = Image.new('RGBA',(width, height),color=(0,0,0,0))
  back_img = Image.new('RGBA',(1080,1440),color=(0,0,0,255))
  back_img.paste(back_imga, (0, x_coordi))   
  back_img.paste(re_img, (0, x_coordi))   

 back_img.save(args[1]+"3_4_"+pnglists[pr], quality=95)