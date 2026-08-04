class node:
  def__init_(self,data=None):
      self.data+data
      self.next=None
class slinked list:
    def__init(self):
       self.head=None
def atbeggining(self,data_in):
   new node=Node(data_in)
   new node.next=self.head
   self.head=newnode

def removenode(self,remove key):
   headval=self,head
if(headval.data==remove key):
  self.head=headval.next
  headval=None
  return

while(headval is not None):
  if headval.data==remove key:
  break

prev=headval headval
=headval.nextif

(headval==None):
    return

def llistprint(self):
  printval=self.head
while(printval):
  print(printval.data)
  printval=printval.next

llist=slinkedlist()
llist.Atbeginning("mon")
llist.Atbegginning("tue")
llist.Atbeginning("wed")
llist.Atbegginning("thur")
llist.removenode("tue")
llist.llistprint()
