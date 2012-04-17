from models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from xml.dom.minidom import Document
import random

@csrf_exempt
def home(request):
    entries = Ujinga.objects.all()
    selection = random.randint(0, len(entries)-1)
    #select joke
    ujinga = entries[selection]
    
    if request.method == 'POST':
        Id = request.POST.get('Id',None)
        Message = request.POST.get('Message',None)
        SessionState = request.POST.get('SessionState',None)
        CustomerState = request.POST.get('CustomerState', None)
        response = createXml(Id=Id, Message=ujinga.content, SessionState=SessionState, CustomerState=CustomerState)
        return HttpResponse(response, content_type='text/xml')
    else:
        return HttpResponse(ujinga.content)

def createXml(**kwargs):
    doc = Document()

    # Create the <base> base element   
    baseElement = doc.createElement("mt")
    baseElement.setAttribute("id",kwargs['Id'])
    doc.appendChild(baseElement)

    # Create the <Message> base element   
    messageElement = doc.createElement("msg")
    messageText = doc.createTextNode(kwargs['Message'])
    messageElement.appendChild(messageText)
    baseElement.appendChild(messageElement)

    # Create the <SessionState> base element   
    sessionStateElement = doc.createElement("sessionstate")
#    sessionStateText = doc.createTextNode(kwargs['SessionState'])
#    sessionStateElement.appendChild(sessionStateText)
    baseElement.appendChild(sessionStateElement)


    # Create the <CustomerState> base element   
    customerStateElement = doc.createElement("customerstate")
#    customerStateText = doc.createTextNode(kwargs['CustomerState'])
#    customerStateElement.appendChild(customerStateText)
    baseElement.appendChild(customerStateElement)

    # Print our newly created XML                                                                                           
    return doc.toxml()

