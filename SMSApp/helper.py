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

def returnOrderMappings():
	mapping = { 'api_key': '63aae231cdab277428c0c4e73ee2e9f3ccbe6c42',
		        'test':'True', 'design':'True', 'price':'18.41', 
		        'garment[0][product_id]': '3',
		        'garment[0][color]':'White',
		        'garment[0][sizes][lrg]': '1',
		        'print[front][color_count]':'1',
		        'print[front][artwork]':'http://i488.photobucket.com/albums/rr249/STACIA_GIRL_2009/ANIMALES/koala.png',
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
		msg = msg + '\nDelivery Date: '+ str(jsonObject['delivery_date'])
		msg = msg + '\nNotes:'
		for w in jsonObject['warnings']:
			msg = msg + '\n' + w
	except:
		msg = 'ERROR'

	return msg