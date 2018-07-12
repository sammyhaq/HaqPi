import easyimap


class Receiver:
    def __init__(self, LOGIN, PASSWORD):
        self.login = LOGIN
        self.password = PASSWORD

        self.imapper = easyimap.connect('imap.gmail.com', self.login,
                                        self.password)

    def printAllEmail(self):
        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            self.printEmail(mail)

    def getEmailAtIndex(self, i):
        return self.imapper.mail(self.imapper.listids()[i])

    def getEmailsWithSubject(self, subject, partialMatch=False):
        returnList = []

        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            if (mail.title == subject):
                returnList.append(mail)

        return returnList

    def getEmailsWithSender(self, sender, partialMatch=False):
        returnList = []

        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            if (mail.title == sender):
                returnList.append(mail)

        return returnList

    def getEmailsWithBody(self, body):
        returnList = []

        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            if (body in mail.body):
                returnList.append(mail)

        return returnList

    def getEmailsWithAttachment(self, attachment):
        returnList = []

        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            if (attachment in mail.attachments):
                returnList.append(mail)

        return returnList

    def searchInbox(subject=None,
                    sender=None,
                    body=None,
                    attachments=None):

#def printEmail(mail):
#        print("\n--\n")
#        print(mail.from_addr)
#        print(mail.to)
#        print(mail.cc)
#        print(mail.title)
#        print(mail.body)
#        print(mail.attachments)
