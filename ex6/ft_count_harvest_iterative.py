def ft_count_harvest_iterative() -> None:
    count = int(input("Days until harvest: "))
    for day in range(1, count + 1):
        print("Day", day)
    print("Harvest time!")
