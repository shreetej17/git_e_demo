users = {
    "admin": "admin123",
    "user": "1234"
}

def login_user(username, password):
    if username in users:
        if users[username] == password:
            print("Login successful")
            return username
        else:
            print("Wrong password")
    return None


def create_order(user, amount):
    if user == None:
        print("Invalid user")

    if amount > 10000:
        print("High value order")

    if amount > 10000:
        print("High value order")   # duplicate code smell

    discount = calculate_discount(amount)
    final_amount = amount - discount

    print("Order placed for", user, "amount", final_amount)


def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.2
    else:
        return amount * 0.2   # duplicated logic
