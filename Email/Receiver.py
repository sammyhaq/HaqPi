import easyimap


class Receiver:
    def __init__(self, LOGIN, PASSWORD):
        self.login = LOGIN
        self.password = PASSWORD

        self.imapper = easyimap.connect('imap.gmail.com', self.login,
                                        self.password)

    #
    # Getting mail objects from the inbox. 
    #
    def getEmailAtIndex(self, i):
        return self.imapper.mail(self.imapper.listids()[i])

    #
    # Returns a list of mail objects matching the search query.
    #
    def searchInbox(subject="",
                    sender="",
                    body="",
                    attachments=""):

        returnList = []

        for mail_id in self.imapper.listids():
            mail = self.imapper.mail(mail_id)

            if (((subject == "") or (mail.title == subject)) and
                ((sender == "") or (mail.from_addr == sender)) and
                ((body == "") or (body in mail.body)) and
               ((attachments == "") or (attachment in mail.attachments))):

                returnList.append(mail)

        return returnList

    #
    # Print method.
    #
    def printEmail(mail):
        print("\n--\n")
        print(mail.from_addr)
        print(mail.to)
        print(mail.cc)
        print(mail.title)
        print(mail.body)
        print(mail.attachments)

    #
    # Getter method for parsing the mail contents and returning
    # them as dict key/value pairs.
    #
    # KEYS:
    #   'to'
    #   'from'
    #   'cc'
    #   'subject'
    #   'body'
    #   'attachments'
    #
    def parseMail(mail):
        toReturn = {}
        toReturn['to'] = mail.to
        toReturn['from'] = mail.from_addr
        toReturn['cc'] = mail.cc
        toReturn['subject'] = mail.title
        toReturn['body'] = mail.body
        toReturn['attachments'] = mail.attachments

        return toReturn
