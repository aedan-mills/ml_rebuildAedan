def theLargest(nums):
    # baseline = 0, this was how I did it initially, not TERRIBLE, but only works if
    # all numbers given are positive. Try this:
    baseline = nums[0]
    # now the list starts with the actual first element, and then
    # we can save time by starting the comparison on the elements after
    for num in nums[1:]:
        if(num > baseline):
            baseline = num
    return baseline


def main():
    user = input("Provide a list of comma-separated numbers you want to see the largest of: ")
    userNums = user.split(",")
    userNums = [int(num) for num in userNums]
    print (userNums)

    print("Now here, my friend is the largest: ", theLargest(userNums))


if __name__ == "__main__":
    main()