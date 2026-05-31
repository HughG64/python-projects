users = [
    {"name": "Alice", "age": 28, "active": True},
    {"name": "Bruno", "age": 17, "active": False},
    {"name": "Zara", "age": 34, "active": True},
    {"name": "Mike", "age": 15, "active": True},
    {"name": "Leah", "age": 22, "active": False},
]

adults = [user["name"] for user in users if user["age"] >= 18 and user["active"]]

# print(adults)


def summarise_users(users):
    total_users = len(users)
    active_users = 0
    total_ages = 0
    for user in users:
        if user["active"]:
            active_users += 1

        total_ages += user["age"]

    average_age = total_ages/total_users
    return f"Total users: {total_users}\nActive users: {active_users}\nAverage age: {average_age:.1f}"

print(summarise_users(users))


