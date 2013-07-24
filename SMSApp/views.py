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
        #incomingPhoneNumber = requestQueryDict['From'].replace('%2B', '')
        #incomingText = requestQueryDict['Body']

        #print 'incomingPhoneNumber: ' + incomingPhoneNumber
        #print 'incomingText: ' + requestQueryDict['Body']

        incomingPhoneNumber = '+905316326123'
        incomingText = 'YES'

        orders = models.ShirtRequest.objects(phoneNumber=incomingPhoneNumber)

        if orders.count() > 0:
            if incomingText in constants.YES_NO_ARRAY:
                print 'Over here. Calm down'
                msg = constants.SUCCESS_MESSAGE_CANCELLATION
                
                if incomingText in constants.YES_ARRAY:
                    #msg = constants.SUCCESS_MESSAGE
                    print 'Going to make the request'
                    requestMapping = helper.returnOrderMappings()
                    print type(requestMapping)
                    getResponse = helper.makeRequest('POST', 'https://www.shirts.io/api/v1/order/', 
                        requestMapping)
                    msg = helper.returnText(getResponse.json())

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
            print 'all saved'
            msg = helper.generateVerification(constants.APPLICATION_IMAGE_LINK + 
                incomingPhoneNumber + ".png")
            print 'myFinalMessage: ' + msg
    except Exception as e:
        import traceback, os.path
        top = traceback.extract_stack()[-1]
        print ', '.join([type(e).__name__, os.path.basename(top[0]), str(top[1])])
        msg = constants.ERROR_MESSAGE_SERVER + type(e).__name__

    r = Response()
    r.sms(msg)
    return r
    