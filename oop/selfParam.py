from random import randint

class Train:
   class Train:
    def __init__(slf, tn):
        slf.tn = tn

    def book(slf, source, to):
        slf.source = source
        slf.to = to
        print(f"\nTicket is booked in train number: {slf.tn}, from {source} to {to}.\n")

    def getStatus(slf):
        print(f"\nTrain no: {slf.tn} is running successfully on time.\n")

    def getFare(slf):
        print(f"\nTicket fare in train no: {slf.tn} from {slf.source} to {slf.to} is {randint(222,5555)}\n")

t= Train(2)
t.book('Kathmandu','Chitwan')
t.getStatus()
