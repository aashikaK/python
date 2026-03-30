from random import randint

class Train:

    def book(self,trainNo,source,to):
        print(f"Ticket is booked in train number: {trainNo}, from {source} to {to}.")

    def getStatus(self, trainNo):
        self.trainNo=trainNo
        print(f"Train no: {self.trainNo} is running successfully  on time.")

    def getFare(self, trainNo, source, to):
        self.source=source
        print(f"Ticket fare in train no: {trainNo} from {self.source} to {to} is {randint(222,5555)}")

t= Train()
t.book(2,'Kathmandu','Chitwan')
t.getStatus(2)
t.getFare(2,'Kathmandu','Chitwan')