from random import randint

class Train:

    def book(self,trainNo,source,to):
        print(f"Ticket is booked in train number: {self.trainNo}, from {self.source} to {self.to}.")

    def getStatus(self, trainNo):
        print(f"Train no: {self.trainNo} is running successfully  on time.")

    def getFare(self, trainNo, source, to):
        print(f"Ticket fare in train no: {self.trainNo} from {self.source} to {self.to} is {randInt(222,5555)}")

t= Train()
t.book(2,'Kathmandu','Chitwan')
t.getStatus(2)
t.getFare(2,'Kathmandu','Chitwan')