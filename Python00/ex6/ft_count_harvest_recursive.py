def ft_count_harvest_recursive(days: int | None = None) -> None:
    input_value: int | None = None
    if (days is None):
        days = int(input("Days until harvest: "))
        input_value = days
    if (days > 0):
        ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")
        if (days == input_value):
            print("Harvest time!")
