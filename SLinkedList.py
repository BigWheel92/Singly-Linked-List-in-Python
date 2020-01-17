#Node class implementation for Singly Linked List
class SNode:

    def __init__(self):
       self.data=None
       self.next=None

    def setData(self, data):
        self.data=data

    def setNext(self, next):
        self.next=next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


#Singly Linked List Implementation
class SLinkedList:

    def __init__(self):
        self.head=self.tail=None

    def insertAtHead(self, data):
        temp = SNode()
        temp.setData(data)

        if self.head==None:
            temp.setNext(None)
            self.head=self.tail=temp

        else:
            temp.setNext(self.head)
            self.head=temp


    def insertAtEnd(self, data):
        temp=SNode()
        temp.setData(data)

        if self.tail==None:
            temp.setNext(None)
            self.head=self.tail=temp

        else:
            self.tail.setNext(temp)
            self.tail=temp


    def print(self):
        curr=self.head

        while curr!=None:
            print(curr.getData())
            curr=curr.getNext()


    def deleteFromHead(self):
        if self.head==None:
            return

        if self.head is self.tail:
            self.head=self.tail=None
            return

        self.head=self.head.getNext()


    def deleteFromTail(self):
        if self.tail==None:
            return

        if self.head is self.tail:
            self.head=self.tail=None
            return

        curr=self.head

        while curr.getNext() is not self.tail:
            curr=curr.getNext()

        curr.setNext(None)
        self.tail=curr




