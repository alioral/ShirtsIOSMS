# Create your views here.
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

@twilio_view
def reply_to_sms_messages(request):
	
	for i in request:
		print i + ' ' + request[i]
    
    r = Response()
    r.sms('Thanks for the SMS message!')
    return r