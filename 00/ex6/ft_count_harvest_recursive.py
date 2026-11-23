def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(current: int = 1) -> None:
        if current > days:
            print("Harvest time!")
            return
        print("Day ", current)
        helper(current + 1)

    helper()
