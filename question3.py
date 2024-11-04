def unpacking(order):
    for index, element in enumerate(order):
        print(f"\nCustomer {index + 1}: \n   Customer name: {element[0]} \n   Item Ordered: {element[1]} \n   Quantity: {element[2]}")

orders = [("Alice", "Laptop", 1), ("Bob", "Camera", 2)]
unpacking(orders)

