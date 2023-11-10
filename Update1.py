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
      # self.head will become None after assigning it to newNode.next
      # print(newNode.next)
      newNode.next = self.head
      self.head = newNode
      print("New Item Added")

  def append(self, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory):
    newNode = Node(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    isTrue = False
    if self.head == None:
      self.head = newNode
      print("New Item Added")
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = newNode
      isTrue = True
    if isTrue:
      print("New Item Added")

  def insertAtPosition(self, position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory):
    newNode = Node(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
    if self.head == None:
      self.head = newNode
    else:
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
      current = self.head.data
      self.head = self.head.next
      print("Item Deleted")
      return current

  # Delete at the End
  def deleteAtEnd(self):
    isTrue = False
    if self.head == None:
      print("List is Empty")
    else:    
      current = self.head
      if current.next == None:
        current = None
      while current.next.next != None:
        current = current.next
      # lastNode = current.next
      current.next = None
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

ItemCodes = []
linked = LinkedList()
while True:
  
  choose = input("Choose an Option : ")
  if int(choose) <= 3: 
    flag = True
    itemCode = input("Enter Item Code : ")
    ctr = 0
    while ctr < len(ItemCodes):
      if itemCode == ItemCodes[ctr]:
        print("Item Code Already Exist.")
        break
      else:
        flag = False
        ctr += 1
    if ctr == len(ItemCodes):
      itemDescription = input("Enter Item Description : ")
      itemPrice = float(input("Enter Item Price : "))
      itemQuantity = int(input("Enter Item Quantity : "))
      itemCategory = input("Enter Item Category : ").upper()
      ItemCodes.append(itemCode)
      
      # linked.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
      # linked.append("321", "Keyboard", 599.0, 1, "M")
      # linked.display()
      
      if choose == '1':
        linked.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
        # linked.append("321", "Keyboard", 599.0, 1, "M")
        linked.display()
      elif choose == '2':
        linked.append(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
      elif choose == '3':
        position = int(input("Enter Position : "))
        linked.insertAtPosition(position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
  else:
    if choose == '4':
      pass
    # elif choose == '5':
    # elif choose == '6':
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
    # else:
    #   print("Invalid Input.")