import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os.path
from SMSProject import settings

def generateShirtImage(phoneNumber, message):
	

	font = ImageFont.truetype('SMSProject/static/fonts/kberry.ttf', 30)
	#print 'Hello'
	img = Image.open('SMSApp/shirtimages/shirt.png')
	draw = ImageDraw.Draw(img)
	draw.text((125, 150),message,(0,0,0),font=font)
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)

	imagePath = "SMSApp/shirtimages/" + phoneNumber + ".png"

	img.save(imagePath)
	return {'imagePath': imagePath, 'img': img}