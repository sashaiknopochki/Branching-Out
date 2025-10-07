import json


def filter_users_by_name(name):
    """
    Filters users by name.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_by_age(age):
    """
    Filters users by age.
    """
    pass

def filter_by_email(email):
    """
    Filters users by email.
    """
    pass

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")