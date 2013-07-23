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

    msg = 'Hello, World'
    path = helper.generateShirtImage('5316326123', msg)

    r = Response()
    r.sms(path)
    return r
    '''
    requestQueryDict = request.POST.copy()

    try:
        incomingPhoneNumber = requestQueryDict['From'].replace('%2B', '+')
        incomingText = requestQueryDict['Body']

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
            msg = 'Going to create a tshirt image'
            newOrder = models.ShirtRequest(phoneNumber = incomingPhoneNumber)
            newOrder.save()
    except:
        msg = constants.ERROR_MESSAGE_SERVER

    r = Response()
    r.sms(msg)
    return r
    '''


    '''
    print 'Printing parameters'

    for i in request:
        print i

    requestQueryDict = request.POST.copy()

    try:
        messageToSend = requestQueryDict['Body']
    except:
        messageToSend = 'An error occured'

    r = Response()
    r.sms(messageToSend)

    return r
    '''