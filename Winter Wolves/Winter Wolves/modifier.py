from PIL import Image
img = Image.open("img.png")

data={  "pant_dark":  (3,14),
		"pant_light": (4,13),
		"skin_dark":  (0,12),
		"skin_light": (1,12),
		"shirt_dark": (0,8),
		"shirt_light":(1,8),
		"hair_dark":  (3,2),
		"hair_light": (4,2)
		}

skincolor=[(205,133,63,255),(210,180,140,255),(245,222,179,255)]#tan peru wheat
shirtcolor=[(139,69,19,255),(255,20,147,255),(255,255,0,255),(245,255,250,255),(255,0,0,255)]#saddle-brown deep-pink yellow mint-cream red 
pantcolor=[(128,0,128,255),(220,20,60,255),(25,25,112,255),(255,255,255,255),(10,10,10,255)]# purple crimson midnight-blue white black
haircolor=[(105,105,105,255),(192,192,192,255),(255,215,0,255),(128,0,0,255)]#dark grey  light grey golden maroon

color1=img.getpixel(data["hair_light"])
for key in data:
	map_area=[]
	color=img.getpixel(data[key])
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			if img.getpixel((x,y)) == color:
				map_area.append((x,y))
	data[key]=map_area
# print(data['shirt_dark'][6])
def darken(a):
	b=[a[0]-40,a[1]-40,a[2]-40,a[3]]
	for i in range(len(b)):
		if b[i]<0:
			b[i]=0
	b=tuple(b)
	return b
	
def generateimages():
	i=0
	for c1 in skincolor:
		for c2 in shirtcolor:
			for c3 in pantcolor:
				for c4 in haircolor:
					for coordinate in data['pant_dark']:
						img.putpixel(coordinate,darken(c3))
					for coordinate in data['pant_light']:
						img.putpixel(coordinate,c3)
					for coordinate in data['hair_dark']:
						img.putpixel(coordinate,darken(c4))
					for coordinate in data['hair_light']:
						img.putpixel(coordinate,c4)
					for coordinate in data['shirt_dark']:
						img.putpixel(coordinate,darken(c2))
					for coordinate in data['shirt_light']:
						img.putpixel(coordinate,c2)
					for coordinate in data['skin_dark']:
						img.putpixel(coordinate,darken(c1))
					for coordinate in data['skin_light']:
						img.putpixel(coordinate,c1)	
					img.save(str(i)+'.png')
					i+=1;

if __name__ == "__main__":
	generateimages();