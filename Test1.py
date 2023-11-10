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
      print("New Item Added")
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
index = 0
ItemCodes = []
print(len(ItemCodes))
# print(ItemCodes)
while True:
  length = len(ItemCodes)
  choose = input("Choose an Option : ")
  if int(choose) <= 3: 
    flag = True
    itemCode = input("Enter Item Code : ")
    ctr = 0
    while ctr < length:
      if itemCode == ItemCodes[ctr]:
        print("Item Code Already Exist.")
        break
      else:
        flag = False
        ctr += 1
    if ctr == length:
      itemDescription = input("Enter Item Description : ")
      itemPrice = float(input("Enter Item Price : "))
      itemQuantity = int(input("Enter Item Quantity : "))
      itemCategory = input("Enter Item Category : ").upper()
      # ItemCodes.append(itemCode)
      
      if choose == '1':
        linked.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)

        # ItemCodes Container
        ItemCodes.insert(0, itemCode)
        # if length == 0:
        #   ItemCodes[0] = itemCode
        # else:
        #   i = index+1
        #   while i > 0 and i < index:
        #     ItemCodes[i] = ItemCodes[i-1]
        #     i -= 1
          
      elif choose == '2':
        linked.append(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
        # ItemCodes Container
        ItemCodes.append(itemCode)
        # ItemCodes[length] = itemCode
        
      elif choose == '3':
        position = int(input("Enter Position : "))
        linked.insertAtPosition(position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)
        
        # ItemCodes Container
        ItemCodes.insert(position, itemCode)
        # i = length
        # print(length)
        # while i > position:
        #   ItemCodes[i] = ItemCodes[i-1]
        #   print(i)
        #   i -= 1
        # ItemCodes[position] = itemCode
        # print(ItemCodes)
  else:
    if choose == '4':
      linked.deleteAtBeginning()
      ItemCodes.pop(0)
    elif choose == '5':
      linked.deleteAtEnd()
      ItemCodes.pop(length-1)
    elif choose == '6':
      position = int(input("Enter Position : "))
      linked.deleteAtPosition(position)
      if position < length:
        ItemCodes.pop(position)
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
  index += 1