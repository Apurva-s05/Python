import array as arr
a = arr.array('d',[1.1,1.2,1.3,1.4])
while True:
    print("1.Print array")
    print("2.Add elements in array")
    print("3.Remove elements from array")
    print("4.Exit")
    choice = float(input("Enter your choice:"))
    if choice == 1:
        print("elements in array")
        for numbers in a:
            print(numbers)
    elif choice == 2:
        val = float(input("Enter the value you want to add"))
        if isinstance(val,float): 
            a.append(val)
    elif choice == 3:
        value = a.pop()
        print("Enter the index of value you want to remove",value)
        
    elif choice == 4:
        break
    else:
        print("Enter valid number")
