from random import randint

class Train:
   class Train:
    def __init__(self, tn):
        self.tn = tn

    def book(self, source, to):
        self.source = source
        self.to = to
        print(f"\nTicket is booked in train number: {self.tn}, from {source} to {to}.\n")

    def getStatus(self):
        print(f"\nTrain no: {self.tn} is running successfully on time.\n")

    def getFare(self):
        print(f"\nTicket fare in train no: {self.tn} from {self.source} to {self.to} is {randint(222,5555)}\n")

t= Train(2)
t.book('Kathmandu','Chitwan')
t.getStatus()
t.getFare(2,'Kathmandu','Chitwan')