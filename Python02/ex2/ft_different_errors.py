def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        4 / 0
    elif (operation_number == 2):
        open("test.txt")
    elif (operation_number == 3):
        "hello" + 42
    else:
        return


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundErro: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_different_errors()
