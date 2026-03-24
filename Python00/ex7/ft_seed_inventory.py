def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    string: str = seed_type.capitalize() + " seeds:"
    if (unit == "packets"):
        print(f"{string} {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{string} {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{string} covers {quantity} square meters")
    else:
        print("Unknown unit type")
