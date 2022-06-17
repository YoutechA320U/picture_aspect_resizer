from PIL import Image, ImageDraw
import math
import pathlib
import PySimpleGUI as sg
result = sg.popup_get_folder("フォルダを選択してください")
if result is None:
   result =""
result=result+"/"
exclulists,jpglists = [],[]
exclupath = pathlib.Path(result).glob('1_1_*.jpg')
for e in exclupath:
    exclulists.append(e.name)
jpgpath = pathlib.Path(result).glob('*.jpg')
for j in jpgpath:
    jpglists.append(j.name)
for je in  range(len(exclulists)):
    jpglists.remove(exclulists[je])
print(jpglists)

for jr in range(len(jpglists)):
 img = Image.open(result+jpglists[jr])
 width, height = img.size
 print(width, height)
 if width/height <= 1/1:
  re_height = height/1080
  if re_height > 1 :
     re_width = math.ceil(width/re_height)
  elif re_height <= 1 :
     re_height = 1080/height
     re_width = math.ceil(width*re_height)
  re_img = img.resize((re_width, 1080))
  width, height = re_img.size
  y_coordi = int((1080-width)/2)
  back_img = Image.new('RGB',(1080,1080),color=(0,0,0))
  back_img.paste(re_img, (y_coordi, 0)) 
  
 if width/height > 1/1:
  re_width = width/1080
  if re_width > 1 :
     re_height = math.ceil(height/re_width)
  elif re_width <= 1 :
     re_width = 1080/width
     re_height = math.ceil(height*re_width)
  re_img = img.resize((1080, re_height))
  width, height = re_img.size
  x_coordi = int((1080-height)/2)
  back_img = Image.new('RGB',(1080,1080),color=(0,0,0))
  back_img.paste(re_img, (0, x_coordi)) 

 back_img.save(result+"1_1_"+jpglists[jr], quality=95)
if result !="/":
 sg.popup('変換が完了しました')