CUSTOMERS = [
    {
        "id": 1,
        "name": "Gandalf"
    },
    {
        "id": 2,
        "name": "Charles Barkley"
    }
]


def get_all_customers():
    # returns all customers
    """A dummy docstring."""
    return CUSTOMERS


def get_single_customer(id):
    """A dummy docstring."""
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
