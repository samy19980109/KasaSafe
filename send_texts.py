from twilio.rest import Client
class send_texts:
    
    def __init__(self, destNumber, emergContact = None):
        # Account SID and Token are hidden for privacy
        self.accountSID = '*****************************'
        self.accounTOKEN = '*****************************'

        self.tw = Client(self.accountSID, self.accounTOKEN)
        self.twNumber = '+12898143339'
        self.destNumber = str(destNumber)
        self.emergContact = str(emergContact)


    def send_text(self):
        message = self.tw.messages.create(
            body = 'Hey! You seem a bit drowsy, Please wake up!', 
            from_ = self.twNumber, 
            to = self.destNumber
        )
        message = self.tw.messages.create(
            body = 'You are the emergery contact of ' + self.destNumber + ' Please make sure they drive safe !', 
            from_ = self.twNumber, 
            to = self.emergContact
        )

        



