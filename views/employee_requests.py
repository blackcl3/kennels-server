EMPLOYEES = [
    {
        "id":1,
        "name":"Tony Bourdain"
    },
    {
        "id":2,
        "name":"Bill Murray"
    }
]


def get_all_employees():
    # returns all employees
    """A dummy docstring."""
    return EMPLOYEES


def get_single_employee(id):
    """A dummy docstring."""
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
