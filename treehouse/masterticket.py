TICKET_COST = 10
SERVICE_FEE = 2

tickets_remaining = 100    

def calculate_price(num_of_tickets):
    return (TICKET_COST * num_of_tickets) + SERVICE_FEE

while tickets_remaining > 0:
    print("There are {} tickets remaining".format(tickets_remaining))
    user_name = input("What is your name?  ")
    try:
        num_tickets = int(input("How many tickets would you like, {}? ".format(user_name)))
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("That is an invalid value.  Please try again!")
        print("{}".format(err))
    else:
        price = calculate_price(num_tickets)
        print("Ok, {} the total cost for {} tickets is ${}".format(user_name, num_tickets, price))
        is_proceed = input("Would you like to go forward with the purchase?  Please enter yes/no?  ")
    
        if is_proceed.lower() == 'yes':
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you for stopping by, {}!".format(user_name))
            
print("We are all sold out of tickets!".format(user_name))