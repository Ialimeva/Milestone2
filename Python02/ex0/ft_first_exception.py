def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temps: list[str] = ["25", "abc"]
    for t in temps:
        print(f"Input data is '{t}'")
        try:
            input_temperature(t)
            print(f"Temperature is now {t}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===")
    test_temperature()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
