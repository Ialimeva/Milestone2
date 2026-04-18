def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if (temp < 0 or temp > 40):
        if (temp < 0):
            raise ValueError(
                f"{temp}°C is too cold for plants (min 0°C)"
            )
        else:
            raise ValueError(
                f"{temp}°C is too hot for plants (max 40°C)"
            )
    return (temp)


def test_temperature() -> None:
    temps: list[str] = ["25", "abc", "100", "-50"]
    for t in temps:
        print(f"Input data is '{t}'")
        try:
            input_temperature(t)
            print(f"Temperature is now {t}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


def ft_raise_exception():
    print("=== Garden Temperature Checker ===")
    test_temperature()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_raise_exception()
