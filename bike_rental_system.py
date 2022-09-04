# bike_stock = 100

# should_continue = True


# def display():
#     print("Total available stock:- {}".format(bike_stock))


# def bike_request(bikes_quantity):
#     print("We have currently {} bikes available to rent.".format(bike_stock))
#     print("Total price {}".format(bike_stock * 100))
#     print("Total available stock {}\n\n".format(bike_stock - bikes_quantity))
#     if bikes_quantity <= bike_stock:

#         rent = bikes_quantity * 100
#         remaining_bikes = bike_stock - bikes_quantity
#         print(
#             "You have rented {} no of bikes. Collectively rent of it is: {}\nThe remaining bikes in stock: {}\n\n".format(
#                 bikes_quantity, rent, remaining_bikes
#             )
#         )
#     else:
#         print("You have enter invalid range of rented cars.")


# def quit():
#     exit(0)


# while should_continue:
#     command = int(
#         input(
#             "1  Display available stocks\n2  Request a bike for rent (100 Rs-1qty)\n3  Exit\n\t"
#         )
#     )
#     if command == 1:
#         display()

#     elif command == 2:
#         no_of_bikes = int(input("Enter the Qty would you like to rent:- "))
#         bike_request(bikes_quantity=no_of_bikes)

#     elif command == 3:
#         quit()


# 🥗🥗🥗🥗🥗🥗🥗🥗🥗 Now converting the above logic using classes and methods. 🥗🥗🥗🥗🥗🥗🥗🥗🥗🥗


class Bike:
    bike_stock = 100

    def __init__(self):
        pass

    def display(slf):
        print("Total available stock:- {}".format(slf.bike_stock))

    def bike_request(slf, bikes_quantity):
        print("We have currently {} bikes available to rent.".format(slf.bike_stock))
        print("Total price {}".format(slf.bike_stock * 100))
        print("Total available stock {}\n\n".format(slf.bike_stock - bikes_quantity))
        if bikes_quantity <= slf.bike_stock and slf.bike_stock > 0:

            rent = bikes_quantity * 100
            remaining_bikes = slf.bike_stock - bikes_quantity
            print(
                "You have rented {} no of bikes. Collectively rent of it is: {}\nThe remaining bikes in stock: {}\n\n".format(
                    bikes_quantity, rent, remaining_bikes
                )
            )
        else:
            print("You have enter invalid range of rented cars.")

    def quit(slf):
        exit(0)


should_continue = True

bike_object = Bike()
while should_continue:
    command = int(
        input(
            "1  Display available stocks\n2  Request a bike for rent (100 Rs-1qty)\n3  Exit\n\t"
        )
    )
    if command == 1:
        bike_object.display()

    elif command == 2:

        print(
            "We have currently {} bikes available to rent.".format(
                bike_object.bike_stock
            )
        )
        no_of_bikes = int(input("Enter the Qty would you like to rent:- "))
        bike_object.bike_request(bikes_quantity=no_of_bikes)
        bike_object.bike_stock -= no_of_bikes

    elif command == 3:
        bike_object.quit()
    else:
        pass
