import requests
import PIL

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from SMSProject import settings


def generateShirtImage(phoneNumber, message):
	

	font = ImageFont.truetype('SMSProject/static/fonts/kberry.ttf', 30)
	img = Image.open('SMSApp/shirtimages/shirt.png')
	draw = ImageDraw.Draw(img)
	draw.text((125, 150),message,(0,0,0),font=font)
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)

	imagePath = "SMSApp/shirtimages/" + phoneNumber + ".png"

	img.save(imagePath)
	return imagePath

def generateVerification(link):
	return 'Check out: ' + link + '\nTo buy shirt type YES to decline NO'


def makeRequest(method, url, mapping):

	if method == 'GET':
		req = requests.get(url, params = mapping)
	else:
		req = requests.post(url, data = mapping)

	return req

def returnText(obj):
	#try:
	jsonObject = obj['result']
	msg = 'Order ID: ' + jsonObject['order_id']
	msg = msg + '\nDelivery Date: '+ str(jsonObject['delivery_date'])
	msg = msg + '\nNotes:'
	for w in jsonObject['warnings']:
		msg = msg + '\n' + w
	#except:
		#msg = 'ERROR'

	return msg