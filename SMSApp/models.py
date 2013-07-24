from mongoengine import *

# Create your models here.

class ShirtRequest(Document):
	phoneNumber = StringField()
	shirtMessage = StringField()
	shirtPicturePath = StringField()