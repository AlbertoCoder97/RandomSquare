from PIL import Image
from PIL import ImageDraw
import random

width = 800
height = 800

i = 0
j = 0

w = width/20
h = height/20

img = Image.new('RGB', (width,height), color = 'white')
draw = ImageDraw.Draw(img)

while i < height:
    j = 0
    while j < width:
        n = random.randint(0,1)
        if n > 0:
            draw.rectangle([i,j,i+h,j+w], fill="black", outline="black", width = 1)
        else:
            draw.rectangle([i,j,i+h,j+w], fill="white", outline="black", width = 1)
        j= j + w    
    i = i + h
 
draw.line([width-1,0,width-1,height-1], fill="black") 
draw.line([0,height-1,width-1,height-1], fill="black") 
img.save('randomsquare.png')