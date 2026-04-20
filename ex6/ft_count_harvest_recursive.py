def ft_count_harvest_recursive() -> None:
    count = int(input("Days until harvest: "))

    def helper(current: int, count: int) -> None:
        if current > count:
            print("Harvest time!")
        else:
            print(f"Day {current}")
            helper(current + 1, count)

    helper(1, count)
