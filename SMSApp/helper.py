import requests
import PIL
import time

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

	print 'Method: ' + method
	print 'URL: ' + url
	print 'Mapping: ' + str(mapping)

	if method == 'GET':
		req = requests.get(url, params = mapping)
	else:
		req = requests.post(url, data = mapping)

	print 'REQ: ' + req.text
	return req

def returnOrderMappings(artwork):
	mapping = {'api_key': '63aae231cdab277428c0c4e73ee2e9f3ccbe6c42',
		       'test':'True', 'design':'True', 'price':'18.41', 
		       'garment[0][product_id]': '3',
		       'garment[0][color]':'White',
		       'garment[0][sizes][lrg]': '1',
		       'print[front][color_count]':'1',
		       'print[front][artwork]':artwork,
		       'print[front][proof]':'http://www.stanford.edu/~jay/koalas/Koala450j.jpg',
		       'addresses[0][name]':'John Doe',
		       'addresses[0][address]':'123 Hope Ln.',
		       'addresses[0][city]':'Las Vegas',
		       'addresses[0][state]':'Nevada',
		       'addresses[0][zipcode]':'12345'}
	return mapping

def returnText(obj):
	try:
		jsonObject = obj['result']
		msg = 'Order ID: ' + jsonObject['order_id']
		#msg = msg + '\nDelivery Date: '+ str(jsonObject['delivery_date'])
		msg = msg + '\nDelivery Date: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(jsonObject['delivery_date']))
		msg = msg + '\nNotes:'
		lastNoteIndex = len(jsonObject['warnings']) - 1
		msg += jsonObject['warnings'][lastNoteIndex]
	except:
		msg = 'ERROR'

	return msg