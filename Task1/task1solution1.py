def calculate_price():
    """
    This function calculates the total price of a pizza order based on various factors such as the number of pizzas,
    delivery option, whether it's Tuesday, and whether the customer used the app. It performs input validation for the
    number of pizzas, delivery option, Tuesday, and app usage. The function returns the total price of the pizza order.
    """
    base_pizza_cost = 12
    delivery_cost = 2.5
    app_discount = 0.25
    tuesday_discount = 0.5

    # Input validation for the number of pizzas
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas > 0:
                break
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a valid number!")

    # Input validation for delivery option
    while True:
        delivery_option = input("Is delivery required? (y/n) ")
        if delivery_option in ["y", "n"]:
            break
        else:
            print("Please answer 'y' or 'n'.")

    # Input validation for Tuesday
    while True:
        is_tuesday = input("Is it Tuesday? (y/n) ")
        if is_tuesday in ["y", "n"]:
            break
        else:
            print("Please answer 'y' or 'n'.")

    # Input validation for app usage
    while True:
        customer_used_app = input("Did the customer use the app? (y/n) ")
        if customer_used_app in ["y", "n"]:
            break
        else:
            print("Please answer 'y' or 'n'.")

    # Calculate the total price
    total_pizza_cost = base_pizza_cost * num_pizzas

    # Apply Tuesday discount
    if is_tuesday == "y":
        total_pizza_cost -= tuesday_discount * total_pizza_cost

    # Apply delivery cost
    if delivery_option == "y" and num_pizzas < 5:
        total_pizza_cost += delivery_cost

    # Apply app discount
    if customer_used_app == "y":
        total_pizza_cost -= app_discount * total_pizza_cost

    return total_pizza_cost

# Calculate and print the total price
total_price = calculate_price()
print(f"\nTotal Price: £{total_price:.2f}")
