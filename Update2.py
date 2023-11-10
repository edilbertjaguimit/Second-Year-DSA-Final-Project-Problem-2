class Node:
  def __init__(self, ITEM_CODE, ITEM_DESCRIPTION, ITEM_PRICE, ITEM_QUANTITY, ITEM_CATEGORY):
    self.code = ITEM_CODE
    self.description = ITEM_DESCRIPTION
    self.price = ITEM_PRICE
    self.quantity = ITEM_PRICE
    self.category = ITEM_CATEGORY
    self.next = None

class LinkedList:
  def __init__(self,):
    self.head = None

  def push(self, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory):
    newNode = Node(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    if self.head == None:
      self.head = newNode
      print("New Item Added")
    else:
      # Check if the item code is unique
      flag = True
      current = self.head
      while current:
        if itemCode == current.code:
          print("Item Code Already Exist.")
          flag = False
          break
        current = current.next
      # self.head will become None after assigning it to newNode.next
      # print(newNode.next)
      # Add the Items
      if flag:
        newNode.next = self.head
        self.head = newNode
        print("New Item Added")
  
  def append(self, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory):
    newNode = Node(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    if self.head == None:
      self.head = newNode
      print("New Item Added")
    else:
      # Check if the item code is unique
      flag = True
      current = self.head
      while current:
        if itemCode == current.code:
          print("Item Code Already Exist.")
          flag = False
          break
        current = current.next
      # Add the Items
      if flag:
        temp = self.head
        while temp.next:
          temp = temp.next
        temp.next = newNode
        print("New Item Added")

  def insertAtPosition(self, position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory):
    newNode = Node(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    if self.head == None:
      self.head = newNode
      print("New Item Added")
    else:
      # Check if the item code is unique
      flag = True
      current = self.head
      while current:
        if itemCode == current.code:
          print("Item Code Already Exist.")
          flag = False
          break
        current = current.next
      # Add the Items
      if flag:
        if position == 0:
          self.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
          print("New Item Added")
        else:
          count = 0
          isTrue = False
          temp = self.head
          while temp:
            if count == position-1:
              newNode.next = temp.next
              temp.next = newNode
              isTrue = True
              break
            temp = temp.next
            count += 1
          if isTrue:
            print("New Item Added")
          else:
            print("Index Out of Range.")

  # Delete an ELement at the Beginning
  def deleteAtBeginning(self):
    if self.head == None:
      print("List is Empty")
    else:
      current = self.head
      self.head = self.head.next
      print("Item Deleted")
      return current

  # Delete at the End
  def deleteAtEnd(self):
    isTrue = False
    if self.head == None:
      print("List is Empty")
    else:    
      if self.head.next == None:
        self.head = None
        print("Item Deleted")
        return
      current = self.head
      while current.next != None:
        previous = current
        current = current.next
      previous.next = None
      isTrue = True
    if isTrue:
      print("Item Deleted")
      

  def deleteAtPosition(self, position):
    if self.head == None:
      print("List is Empty")
    else:
      if position == 0:
        self.head = self.head.next
        print("Item Deleted")
      else:
        count = 0
        isTrue = False
        current = self.head
        while current:
          if count == position-1:
            if current.next == None:
              break
            else:
              current.next = current.next.next
              isTrue = True
              break
          current = current.next
          count += 1
        if isTrue:
          print("Item Deleted")
        else:
          print("Index out of Range")
          
  def display(self):
    if self.head == None:
      print("List is Empty")
    else:
      temp = self.head
      while temp:
        print(temp.code, temp.description, temp.price, temp.quantity, temp.category)
        temp = temp.next
        
  def length(self):
    if self.head == None:
      print("List is Empty")
    else:
      ctr = 0
      temp = self.head
      while temp:
        temp = temp.next
        ctr += 1
      return ctr


linked = LinkedList()

while True:
  choose = input("Choose an Option : ")
    
  if choose == '1':
    itemCode = input("Enter Item Code : ")
    itemDescription = input("Enter Item Description : ")
    itemPrice = float(input("Enter Item Price : "))
    itemQuantity = int(input("Enter Item Quantity : "))
    itemCategory = input("Enter Item Category : ").upper()
    linked.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
          
  elif choose == '2':
    itemCode = input("Enter Item Code : ")
    itemDescription = input("Enter Item Description : ")
    itemPrice = float(input("Enter Item Price : "))
    itemQuantity = int(input("Enter Item Quantity : "))
    itemCategory = input("Enter Item Category : ").upper()
    linked.append(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    
  elif choose == '3':
    position = int(input("Enter Position : "))
    itemCode = input("Enter Item Code : ")
    itemDescription = input("Enter Item Description : ")
    itemPrice = float(input("Enter Item Price : "))
    itemQuantity = int(input("Enter Item Quantity : "))
    itemCategory = input("Enter Item Category : ").upper()
    linked.insertAtPosition(position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    
  elif choose == '4':
    linked.deleteAtBeginning()
    
  elif choose == '5':
    linked.deleteAtEnd()
    
  elif choose == '6':
    position = int(input("Enter Position : "))
    linked.deleteAtPosition(position)
    
  # elif choose == '7':
  # elif choose == '8':
  # elif choose == '9':
  # elif choose == '10':
  # elif choose == '11':
  # elif choose == '12':
  # elif choose == '13':
  # elif choose == '14':
  elif choose == '15':
    linked.display()
  # elif choose == '16':
  else:
    print("Invalid Input.")