ans="yes"
while ans=="yes":
    print("Enter 1 to find the length of the list")
    print("Enter 2 to find the index of an element")
    print("Enter 3 to add a single element to the list")
    print("Enter 4 to add multiple elements to the list")
    print("Enter 5 to add an element in between the list")
    print("Enter 6 to remove an item (at an index) from the list")
    print("Enter 7 to remove an element from the list")
    print("Enter 8 to clear the list")
    print("Enter 9 to count the occurences of an element in the list")
    print("Enter 10 to reverse the list")
    print("Enter 11 to sort the list")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        L = eval(input("Enter the elements:"))
        print("The length of the list is:", len(L))

    elif choice == 2:
        L = eval(input("Enter the elements:"))
        x = input("Enter the element to be found:")
        print("The index of the element is:", L.index(x))
    elif choice == 3:
        L = eval(input("Enter the elements:"))
        x = input("Enter the element to be added:")
        L.append(x)
        print("The new list is:", L)
    elif choice == 4:
        L = eval(input("Enter the elements:"))
        x = eval(input("Enter the elements to be added:"))
        L.extend(x)
        print("The new list is:", L)
    elif choice == 5:
        L = eval(input("Enter the elements:"))
        x = input("Enter the element to be inserted:")
        i = int(input("Enter the index at which the element should be inserted:"))
        L.insert(i, x)
        print("The new list is:", L)
    elif choice == 6:
        L = eval(input("Enter the elements:"))
        i = int(input("Enter the index of the element to be removed:"))
        L.pop(i)
        print("The new list is:", L)
    elif choice == 7:
        L = eval(input("Enter the elements:"))
        x = input("Enter the element to be removed:")
        L.remove(x)
        print("The new list is:", L)
    elif choice == 8:
        L = eval(input("Enter the elements:"))
        L.clear()
        print("The new list is:", )
    elif choice == 9:
        L = eval(input("Enter the elements:"))
        x = input("Enter the element whose occurence must be counted:")
        count = L.count(x)
        print("The number of occurences of the element is:", count)
    elif choice == 10:
        L = eval(input("Enter the elements:"))
        L.reverse()
        print("The new list is:", L)
    elif choice == 11:
        L = eval(input("Enter the elements:"))
        L.sort()
        print("The new list is:", L)
    ans = input("Do you want to continue?(yes/no)")


