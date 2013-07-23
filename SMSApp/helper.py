import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def generateShirtImage(phoneNumber, message):
	
	font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", 12)
	print 'Hello'
	img = Image.open("../SMSProject/static/images/shirt.png")
	draw = ImageDraw.Draw(img)
	draw.text((125, 150),message,(0,0,0),font=font)
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)

	imagePath = "shirtimages/" + phoneNumber + ".png"

	img.save(imagePath)
	return imagePath