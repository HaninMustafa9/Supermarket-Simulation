# Supermarket Simulation

## Project Overview

This project simulates a supermarket environment where customers add items to their carts, and the system processes their purchases. It manages customer queues, calculates total profit, and provides insights into the supermarket's operations. This simulation demonstrates basic object-oriented programming concepts in Python.

## Features

- **Items**: Represents products with attributes such as name, price, and barcode.
- **Customer**: Manages a cart of items and calculates the total cost.
- **Queue**: Represents a line of customers, processes transactions, and calculates total profit.
- **SuperMarket**: Manages multiple queues and tracks the overall supermarket operations.

## Classes

### Items

- **Attributes**:
  - `name` (str): Name of the item.
  - `price` (float): Price of the item.
  - `barcode` (int): Unique barcode for the item.
- **Methods**:
  - `displayItemInfo()`: Displays the item's name, price, and barcode.

### Cart (ABC)

- **Abstract Methods**:
  - `addItem()`: Adds an item to the cart.
  - `removeItem()`: Removes an item from the cart.
  - `count()`: Returns the number of items in the cart.

### Customer (ABC)

- **Attributes**:
  - `name` (str): Customer's name.
  - `queueNo` (int): Queue number the customer is in.
  - `items` (list): List of items in the cart.
  - `sum` (float): Total cost of items in the cart.
- **Methods**:
  - `addItem(item)`: Adds an item to the cart and updates the total cost.
  - `removeItem(item)`: Removes an item from the cart and updates the total cost.
  - `countItems()`: Returns the number of items in the cart.

### Queue

- **Attributes**:
  - `queueNo` (int): Queue number.
  - `customers` (list): List of customers in the queue.
  - `profit` (float): Total profit from transactions.
- **Methods**:
  - `addCustomer(customer)`: Adds a customer to the queue.
  - `removeCustomer(customer)`: Processes the customer, calculates profit, and removes them from the queue.
  - `countCustomers()`: Returns the number of customers in the queue.

### SuperMarket

- **Attributes**:
  - `queues` (list): List of queues in the supermarket.
- **Methods**:
  - `addQueue(queue)`: Adds a queue to the supermarket.

## Code Example

Here's a brief example of how to use the classes:

```python
# Creating items
milk = Items("Milk", 5)
cheese = Items("Cheese", 4)

# Creating customers
Adham = Customer("Adham", 1)
Adham.addItem(milk)
Adham.addItem(cheese)

# Creating queues
queueOne = Queue(1)
queueOne.addCustomer(Adham)

# Creating supermarket
superMarket = SuperMarket()
superMarket.addQueue(queueOne)

# Display total number of customers and total profit
totalCustomers = queueOne.countCustomers()
print(f"Total number of customers in the supermarket: {totalCustomers} ")

queueOne.removeCustomer(Adham)
totalProfit = queueOne.profit
print(f"Total Profit of the supermarket: {totalProfit} ")
```

## How to Run

1. Save the provided code in a Python file, e.g., `supermarket_simulation.py`.
2. Run the file using Python.

```bash
python supermarket_simulation.py
```

## Notes

- This simulation is a simplified model and can be extended with additional features such as handling multiple items in transactions or more complex customer interactions.
- The code uses Python's `abc` module to define abstract base classes and enforce implementation of specific methods in derived classes.
