# Create your views here.
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from django.shortcuts import HttpResponse, render
from mongoengine import *

import models
import constants
import helper


connect('heroku_app17085708', host= constants.DB_URL)

@twilio_view
def reply_to_sms_messages(request):
    
    requestQueryDict = request.POST.copy()

    try:
        incomingPhoneNumber = requestQueryDict['From'].replace('%2B', '')
        incomingText = requestQueryDict['Body']

        orders = models.ShirtRequest.objects(phoneNumber=incomingPhoneNumber)

        if orders.count() > 0:

            if incomingText in constants.YES_NO_ARRAY:

                msg = constants.SUCCESS_MESSAGE_CANCELLATION
                
                if incomingText in constants.YES_ARRAY:
                    artWorkURL = str(orders.first()['shirtPicturePath'])
                    requestMapping = helper.returnOrderMappings(artWorkURL)

                    getResponse = helper.makeRequest('POST', 'https://www.shirts.io/api/v1/order/', 
                        requestMapping)

                    msg = helper.returnText(getResponse.json())

                orders.delete()
            else:
                msg = constants.ERROR_MESSAGE_ALREADY_HAVE_SHIRT_REQUEST
        else:
            picturePath = helper.generateShirtImage(incomingPhoneNumber, 
                                                    incomingText)

            pictureLink = constants.APPLICATION_IMAGE_LINK + incomingPhoneNumber + ".png"
            newOrder = models.ShirtRequest(phoneNumber = incomingPhoneNumber)
            newOrder.shirtMessage = incomingText
            newOrder.shirtPicturePath = pictureLink
            newOrder.save()

            msg = helper.generateVerification(pictureLink)
    except Exception as e:
        msg = constants.ERROR_MESSAGE_SERVER 

    r = Response()
    r.sms(msg)
    return r
    