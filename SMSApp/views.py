# Create your views here.
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from mongoengine import *

import models
import constants
import helper

connect('heroku_app17085708', host= constants.DB_URL)

@twilio_view
def reply_to_sms_messages(request):
    
    requestQueryDict = request.POST.copy()

    try:
        incomingPhoneNumber = requestQueryDict['From'].replace('%2B', '+')
        incomingText = requestQueryDict['Body']

        print 'incomingPhoneNumber: ' + incomingPhoneNumber
        print 'incomingText: ' + requestQueryDict['Body']

        orders = models.ShirtRequest.objects(phoneNumber='1')

        if orders.count() > 0:
            if incomingText in ["yes", "YES", "no", "NO"]:
                msg = 'Accepted or rejected to print shirt'
                
                if incomingText in ["yes", "YES"]:
                    msg = constants.SUCCESS_MESSAGE

                orders.delete()
            else:
                msg = constants.ERROR_MESSAGE_ALREADY_HAVE_SHIRT_REQUEST
        else:
            print 'In here'
            picturePath = helper.generateShirtImage(incomingPhoneNumber, 
                                                    incomingText)
            print 'picturePath: ' + picturePath
            newOrder = models.ShirtRequest(phoneNumber = incomingPhoneNumber)
            newOrder.shirtMessage = incomingText
            newOrder.shirtPicturePath = picturePath
            newOrder.save()
            msg = helper.generateVerification(incomingText)
            print 'MESSAGE: ' + msg
    except:
        msg = constants.ERROR_MESSAGE_SERVER

    r = Response()
    r.sms(msg)
    return r
    