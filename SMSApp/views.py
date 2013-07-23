# Create your views here.
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

@twilio_view
def reply_to_sms_messages(request):
	
    print 'Printing parameters'
    
    for i in request:
        print i

    try:
        messageToSend = request['Body']
    except:
        messageToSend = 'An error occured'
    r = Response()
    r.sms(messageToSend)

    return r