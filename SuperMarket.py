import random
from abc import ABC, abstractmethod
class Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.barcode = int(random.random() * (10 ** 12)) 

    def diplayItemInfo(self):
        print(f"Item Name: {self.getName()}\t Price: {self.getPrice()}\t Barcode: {self.getBarcode()} ")


class Cart (ABC):
    @abstractmethod
    def addItem(self):
        pass
    @abstractmethod
    def removeItem(self):
        pass
    @abstractmethod
    def count(self):
        pass

class Customer(ABC):

    def __init__(self, name, queueNo):
        self.name = name
        self.queueNo = queueNo
        self.items = []
        #self.item = Items()
        self.sum = 0

    def addItem(self, item):
        self.items.append(item)
        self.sum = self.sum + item.price
 
    def removeItem(self, item):
        itemIndex = self.items.index(item)
        i = len(self.items) - 1
        while (i >= itemIndex):
            print(f"Item: {self.items[i].name}\t Barcode: {self.items[i].barcode}")
            self.items.pop(i)
            i -= 1
        
    def countItems(self):
        return len(self.items)
    

class Queue:
    def __init__(self, queueNo):
        self.queueNo = queueNo
        self.customers = []
        self.profit = 0

    def addCustomer(self, customer):
        self.customers.append(customer)
    
    def removeCustomer(self, customer):
        customerIndex = self.customers.index(customer)
        while (customerIndex != -1):
            self.profit = self.profit + self.customers[0].sum
            print(f"Customer Name: {self.customers[0].name} \t\tTotal: {self.customers[0].sum}")
            self.customers[0].removeItem(customer.items[0])

            self.customers.pop(0)
            customerIndex -= 1

    def countCustomers(self):
        return len(self.customers)
    

class SuperMarket:
    def __init__(self):
        self.queues = []

    def addQueue(self, queue):
        self.queues.append(queue)


milk = Items("Milk", 5)
cheese = Items("Cheese", 4)
cake = Items("Cake", 15)
egg = Items("Egg", 1)
salad = Items("Salad", 6)

Adham = Customer("Adham",1)
Hussein = Customer("Hussein",1)
Sherif = Customer("Sherif",1)
Saad = Customer("Saad",1)
Nour = Customer("Nour",2)
Hoda = Customer("Hoda",2)

Adham.addItem(milk)
Adham.addItem(cheese)
Adham.addItem(cake)
Adham.addItem(egg)
Adham.addItem(salad)

Hussein.addItem(milk)
Hussein.addItem(cheese)

Sherif.addItem(cake)

Saad.addItem(cake)
Saad.addItem(egg)
Saad.addItem(salad)

Nour.addItem(cake)
Nour.addItem(milk)

Hoda.addItem(milk)
Hoda.addItem(cheese)
Hoda.addItem(cake)
Hoda.addItem(cake)
Hoda.addItem(egg)
Hoda.addItem(salad)

queueOne = Queue(1)
queueTwo = Queue(2)

queueOne.addCustomer(Adham)
queueOne.addCustomer(Hussein)
queueOne.addCustomer(Sherif)
queueOne.addCustomer(Saad)

queueTwo.addCustomer(Nour)
queueTwo.addCustomer(Hoda)

superMarket = SuperMarket()
superMarket.addQueue(queueOne)
superMarket.addQueue(queueTwo)


totalCustomers = queueOne.countCustomers() + queueTwo.countCustomers()

print(f"Total number of customers in the supermarket: {totalCustomers} ")

queueOne.removeCustomer(Hussein)
totalProfit = queueOne.profit + queueTwo.profit
print(f"Total Profit of the supermarket: {totalProfit} ")

    
