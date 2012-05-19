from django.http import HttpResponse
from models import FmnaRequestSms, FmnaResponseSms

def index(request):
    pass

def api_process_incoming(request):
    requestSms = FmnaRequestSms.getFromPost(request)
    responseSms = requestSms.generateResponseSms()
    responseSms.message = "I heard your '%s'" % requestSms.message
    response = HttpResponse()
    response.write(responseSms.getXML())
    return response
