# ABC Co. hires a programmer to develop a system that performs the following operations. Item
# attributes are item code (string), item description (string), price (double), quantity (integer), and
# item category (char). Values of item type can be ‘S’ for supermarket, ‘M’ for men section, ‘W’ for
# women section, or ‘T’ for others section. Note that item code should be unique.

def menu():
  print("1. Insert Item at the Beginning")
  print("2. Insert Item at the End")
  print("3. Insert Item at Any Position")
  print("4. Delete Item at the Beginning")
  print("5. Delete Item at the End")
  print("6. Delete Item at Any Position")
  print("7. Delete Item by Item Code")
  print("8. Delete Item by Item Category")
  print("9. Sort Item by Item Code (Ascending)")
  print("10. Sort Item by Price (Descending)")
  print("11. Search Item by Code")
  print("12. Search Item by Type")
  print("13. Search Item by Quantity (from and to quantity)")
  print("14. Update Item by Code")
  print("15. Display")
  print("16. Exit")
  print()

class Node:
  def __init__(self, ITEM_CODE, ITEM_DESCRIPTION, ITEM_PRICE, ITEM_QUANTITY, ITEM_CATEGORY):
    self.code = ITEM_CODE
    self.description = ITEM_DESCRIPTION
    self.price = ITEM_PRICE
    self.quantity = ITEM_QUANTITY
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
    if self.head == None:
      self.head = newNode
      print("New Item Added")
    else:
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

  def deleteByCode(self, itemCode):
    if self.head == None:
      print("List is Empty")
    else:
      isTrue = False
      if itemCode == self.head.code:
        self.head = self.head.next
        print("Item Deleted")
        return
      current = self.head
      previous = None
      while current:
        if itemCode == current.code:
          if previous == None:
            self.head = current.next
          else:
            previous.next = current.next
            isTrue = True
        previous = current
        current = current.next
        
      if isTrue:
        print("Item Deleted")
      else:
        print("Item Code Not Found.")

  def deleteByCategory(self, itemCategory):
    if self.head == None:
      print("List is Empty")
    else:
      isTrue = False
      if itemCategory == self.head.category:
        self.head = self.head.next
        print("Item Deleted")
        return
      current = self.head
      previous = None
      while current:
        if itemCategory == current.category:
          if previous == None:
            self.head = current.next
          else:
            previous.next = current.next
            isTrue = True
        previous = current
        current = current.next
        
      if isTrue:
        print("Item Deleted")
      else:
        print("Item Category Not Found.")

  def sortByCode(self):
    if self.head == None:
      print("List is Empty")
    else:
      flag = False
      current1 = self.head
      while current1:
        current2 = current1.next
        while current2:
          if current1.code > current2.code:
            # Swap Item Code
            tempItemCode = current1.code
            current1.code = current2.code
            current2.code = tempItemCode

            # Swap Item Description
            tempItemDescription = current1.description
            current1.description = current2.description
            current2.description = tempItemDescription

            # Swap Item Price
            tempItemPrice = current1.price
            current1.price = current2.price
            current2.price = tempItemPrice

            # Swap Item Quantity
            tempItemQuantity = current1.quantity
            current1.quantity = current2.quantity
            current2.quantity = tempItemQuantity

            # Swap Item Category
            tempItemCategory = current1.category
            current1.category = current2.category
            current2.category = tempItemCategory
            flag = True
            
          current2 = current2.next
        current1 = current1.next

      if flag:
        print("Items Sorted by Code (Ascending)")
      else:
        print("Items Already Sorted (Ascending)")

  def sortByPrice(self):
    if self.head == None:
      print("List is Empty")
    else:
      flag = False
      current1 = self.head
      while current1:
        current2 = current1.next
        while current2:
          if current1.price < current2.price:
            # Swap Item Code
            tempItemCode = current1.code
            current1.code = current2.code
            current2.code = tempItemCode

            # Swap Item Description
            tempItemDescription = current1.description
            current1.description = current2.description
            current2.description = tempItemDescription

            # Swap Item Price
            tempItemPrice = current1.price
            current1.price = current2.price
            current2.price = tempItemPrice

            # Swap Item Quantity
            tempItemQuantity = current1.quantity
            current1.quantity = current2.quantity
            current2.quantity = tempItemQuantity

            # Swap Item Category
            tempItemCategory = current1.category
            current1.category = current2.category
            current2.category = tempItemCategory
            flag = True
            
          current2 = current2.next
        current1 = current1.next

      if flag:
        print("Items Sorted by Price (Descending)")
      else:
        print("Items Already Sorted (Descending)")

  def searchItemCode(self, itemCode):
    if self.head == None:
      print("List is Empty")
    else:
      current = self.head
      while current:
        if itemCode == current.code:
          print(current.code, current.description, current.price, current.quantity, current.category)
          return
        current = current.next
      print("Item Code Not Found.")

  def searchItemCategory(self, itemCategory):
    if self.head == None:
      print("List is Empty")
    else:
      current = self.head
      while current:
        if itemCategory == current.category:
          print(current.code, current.description, current.price, current.quantity, current.category)
          return
        current = current.next
      print("Item Category Not Found.")

  def searchItemQuantity(self, itemQuantityFrom, itemQuantityTo):
    if self.head == None:
      print("List is Empty")
    else:
      flag = True
      current = self.head
      while current:
        if itemQuantityFrom <= current.quantity <= itemQuantityTo:
          print(current.code, current.description, current.price, current.quantity, current.category)
          flag = False
        current = current.next
      if flag:
        print("Item Price Range Not Found.")

  def updateItemByCode(self, itemCode):
    if self.head == None:
      print("List is Empty")
    else:
      current = self.head
      while current:
        if itemCode == current.code:
          current.description = input("New Description: ").upper()
          current.price = float(input("New Price: "))
          current.quantity = int(input("New Quantity: "))
          current.category = input("New Category: ").upper()
          return
        current = current.next
      print("Item Code Not Found.")
      
  def display(self):
    if self.head == None:
      print("List is Empty")
    else:
      lineTotal = 0
      overAllTotal = 0
      temp = self.head
      print("Item Code | Item Description | Item Price | Item Quantity")
      while temp:
        print("  ", temp.code, "\t\t\t ", temp.description, "\t\t\t  ", temp.price, "\t\t", temp.quantity)
        lineTotal += 1
        overAllTotal = float(overAllTotal) + temp.price
        temp = temp.next
      print("Total Line Items: ", lineTotal)
      print("Total Over All Items: ", overAllTotal)

  def pushIfUnique(self, itemCode):
    flag = True
    current = self.head
    while current:
      if itemCode == current.code:
        print("Item Code Already Exist.")
        flag =  False
      current = current.next
    if flag:
      itemDescription = input("Enter Item Description : ").upper()
      itemPrice = float(input("Enter Item Price : "))
      itemQuantity = int(input("Enter Item Quantity : "))
      itemCategory = input("Enter Item Category : ").upper()
      self.push(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)

  def appendIfUnique(self, itemCode):
    flag = True
    current = self.head
    while current:
      if itemCode == current.code:
        print("Item Code Already Exist.")
        flag =  False
      current = current.next
    if flag:
      itemDescription = input("Enter Item Description : ").upper()
      itemPrice = float(input("Enter Item Price : "))
      itemQuantity = int(input("Enter Item Quantity : "))
      itemCategory = input("Enter Item Category : ").upper()
      linked.append(itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)

  def insertIfUnique(self, itemCode):
    flag = True
    current = self.head
    while current:
      if itemCode == current.code:
        print("Item Code Already Exist.")
        flag =  False
      current = current.next
    if flag:
      itemDescription = input("Enter Item Description : ").upper()
      itemPrice = float(input("Enter Item Price : "))
      itemQuantity = int(input("Enter Item Quantity : "))
      itemCategory = input("Enter Item Category : ").upper()
      position = int(input("Enter Position : "))
      linked.insertAtPosition(position, itemCode, itemDescription, itemPrice, itemQuantity, itemCategory)


linked = LinkedList()

menu()

while True:
  
  choose = input("Choose an Option : ")
  print()

  # Insert Item at the Beginning
  if choose == '1':
    itemCode = input("Enter Item Code : ")
    linked.pushIfUnique(itemCode)

  # Insert Item at the End
  elif choose == '2':
    itemCode = input("Enter Item Code : ")
    linked.appendIfUnique(itemCode)

  # Insert Item at the Position
  elif choose == '3':
    itemCode = input("Enter Item Code : ")
    linked.insertIfUnique(itemCode)

  # Delete Item at the Beginning
  elif choose == '4':
    
    linked.deleteAtBeginning()

  # Delete Item at the End
  elif choose == '5':
    
    linked.deleteAtEnd()

  # Delete Item at the Position
  elif choose == '6':
    position = int(input("Enter Position : "))
    linked.deleteAtPosition(position)

  # Delete Item by Item Code
  elif choose == '7':
    itemCode = input("Delete Item by Code : ")
    linked.deleteByCode(itemCode)

  # Delete Item by Item Category
  elif choose == '8':
    itemCategory = input("Delete Item by Category : ").upper()
    linked.deleteByCategory(itemCategory)

  # Sort Item by Item Code (Ascending)
  elif choose == '9':
    
    linked.sortByCode()

  # Sort Item by Item Price (Descending)
  elif choose == '10':
    linked.sortByPrice()

  # Search Item by Code
  elif choose == '11':
    itemCode = input("Search Item by Code : ")
    linked.searchItemCode(itemCode)

  # Search Item by Category
  elif choose == '12':
    itemCategory = input("Search Item by Category : ").upper()
    linked.searchItemCategory(itemCategory)

  # Search Item by Quantity (from and to quantity)
  elif choose == '13':
    itemQuantityFrom = int(input("Enter Item Quantity From : "))
    itemQuantityTo = int(input("Enter Item Quantity To : "))
    linked.searchItemQuantity(itemQuantityFrom, itemQuantityTo)

  # Update Item by Code
  elif choose == '14':
    itemCode = input("Update Item by Code : ")
    linked.updateItemByCode(itemCode)

  # Display All Items
  elif choose == '15':
    linked.display()

  # Exit
  elif choose == '16':
    print("Program Terminated.")
    break
    
  else:
    print("Invalid Input.")
  print()