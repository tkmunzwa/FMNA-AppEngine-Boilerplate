from django.db import models
from xml.dom.minidom import Document

class FmnaSms(models.Model):
    '''
    Abstract class to for FMNA SMS message
    '''
    upstream_id = models.TextField('Message ID')
    message  = models.TextField('Message', blank=False, null=False)
    session_state = models.TextField('Session State', blank=True, null=True)
    customer_state = models.TextField('Session State', blank=True, null=True)

    class Meta:
        abstract = True
        app_label = 'api'

class FmnaRequestSms(FmnaSms):
    @staticmethod
    def getFromPost(request):
        """
        @request: django.HttpRequest
        @return: FmnaRequestSms
        """
        requestSms = FmnaRequestSms()
        requestSms.upstream_id = request.POST.get('Id', None)
        requestSms.message = request.POST.get('Message', None)
        requestSms.customer_state = request.POST.get('CustomerState', None)
        requestSms.session_state = request.POST.get('SessionState', None)
        if requestSms.upstream_id is None:
            raise Exception("Message ID not found")
        return requestSms

    def generateResponseSms(self):
        response = FmnaResponseSms()
        response.response_to = self.upstream_id
        response.upstream_id = self.upstream_id
        response.customer_state = self.customer_state
        response.session_state = self.session_state
        return response
    pass

class FmnaResponseSms(FmnaSms):
    response_to = models.TextField('In Response to', blank=True, null=True)

    def getXML(self):
        """
        @return: string
        """
        
        import pprint
        pprint.pprint(self)
        doc = Document()
        mt = doc.createElement('mt');
        mt.setAttribute('id', self.upstream_id)
        msg = doc.createElement('msg');
        textNode = doc.createTextNode(self.message)
        msg.appendChild(textNode)
        mt.appendChild(msg)
        if self.session_state is not None:
            sessionNode = doc.createElement('sessionstate');
            textNode = doc.createTextNode( (self.session_state))
            sessionNode.appendChild(textNode)
            mt.appendChild(sessionNode)
        if self.customer_state is not None:
            customerNode = doc.createElement('customerstate')
            textNode = doc.createTextNode(self.customer_state)
            customerNode.appendChild(textNode)
            mt.appendChild(customerNode)
        doc.appendChild(mt)
        return doc.toxml()
    

