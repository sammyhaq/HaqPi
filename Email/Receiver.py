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

    def getEmailAtIndex(self, i):
            mail = self.imapper.mail(self.imapper.listids()[i])

            print("\n--\n")
            print(mail.from_addr)
            print(mail.to)
            print(mail.cc)
            print(mail.title)
            print(mail.body)
            print(mail.attachments)

            return mail
