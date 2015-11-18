import re
import random
import string

class Customer():
    """Dit doet dingen."""
    uidcounter = 0
    def __init__(self,naam,telnr,mail):
        self.naam = naam
        self.telnr = telnr
        self.mail = mail
        self.uid = Customer.uidcounter
        Customer.uidcounter += 1
        self.__check_domain()
        self.password = "welkom"

    def check_telephone_number(self):
        tocheck = self.telnr
        if (type(tocheck) is str):
            tocheck = tocheck.replace('-','' )
            if (len(tocheck) == 10):
                try:
                    int(tocheck)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return False

    def __check_domain(self):
        domain = re.search("@[\w.]+", self.mail)
        self.domain = domain.group()

    def reset_password(self):
        self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    def __str__(self):
        return("Naam: %s\nE-mailadres: %s\nTelefoonnummer: %s" % (self.naam, self.mail, self.telnr))