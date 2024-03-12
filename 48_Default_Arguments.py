def PrintDetails(id, name='NA', price='NA'):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")


PrintDetails(name='abc', id=101)
print()
PrintDetails(price='200', id=102)  # Keyword Arguments (Don't need to remember order of passing arguments)
print()
PrintDetails(103, 'xyz', '300')  # Positional arguments
