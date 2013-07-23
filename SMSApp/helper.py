import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os.path
from SMSProject import settings

def generateShirtImage(phoneNumber, message):
	
	path = os.path.join(settings.STATIC_URL, 'fonts/kberry.ttf')

	font = ImageFont.truetype("Arial.ttf", 12)
	#print 'Hello'
	img = Image.open(settings.STATIC_URL + 'images/shirt.png')
	draw = ImageDraw.Draw(img)
	draw.text((125, 150),message,(0,0,0),font=font)
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)

	imagePath = "shirtimages/" + phoneNumber + ".png"

	img.save(imagePath)
	return imagePath