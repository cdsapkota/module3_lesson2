def itinerary (tuple_info):
    for index, element in enumerate(tuple_info):
        print(f"Itinerary {index + 1}: {element[0]} - From {element[1]} to {element[2]}")
        # if isinstance (element, tuple):
        #         print(f"Itinerary {index + 1}: {element[0]} - From {element[1]} to {element[2]}")
        # else:
        #     print(f"Itinerary {index + 1}: {element[0]} - From {element[1]} to {element[2]}")

test = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
itinerary(test)