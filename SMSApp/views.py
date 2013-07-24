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

        print 'incomingPhoneNumber: ' + incomingPhoneNumber
        print 'incomingText: ' + requestQueryDict['Body']

        orders = models.ShirtRequest.objects(phoneNumber=incomingPhoneNumber)

        if orders.count() > 0:
            if incomingText in constants.YES_NO_ARRAY:
                print 'Over here. Calm down'
                msg = constants.SUCCESS_MESSAGE_CANCELLATION
                
                if incomingText in constants.YES_ARRAY:
                    #msg = constants.SUCCESS_MESSAGE
                    print 'Going to make the request'
                    requestMapping = helper.returnOrderMappings()
                    print requestMapping
                    getResponse = helper.makeRequest('POST', 'https://www.shirts.io/api/v1/order/', 
                        {'api_key': '63aae231cdab277428c0c4e73ee2e9f3ccbe6c42',
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
                        'addresses[0][zipcode]':'12345'})
                    print 'JSON' + getResponse.json()
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
    except:
        msg = constants.ERROR_MESSAGE_SERVER

    r = Response()
    r.sms(msg)
    return r
    