def maxAndMin(nums):

    # added lines of null case here
    if not nums:
        return None


    # min = nums[0]
    # max = nums[0] not bad solutions, but it would then overwrite min and max built in func
    # try this
    min_val = nums[0]
    max_val = nums[0]
    for num in nums[1:]:  # i'll add the comment here, but do the cool 1st indexing if you reference 0 index already
        if(num>=max_val):
            max_val = num
        # else if(num<=min_val):  
        # else if does not exist in python, instead try elif
        # furthermore however, rather than an else if, lets just stick to two if statements
        # this makes it so the program always checks both statements independently instead of 
        # skipping over another simply because it was also correct at the same time
        if(num<=min_val):
            min_val = num
        # if(!(nums)):   THIS IS HOPEFULLY SOMETHING IN C, I have no idea why else I thought this would work
        #   return       Decent idea though, but the check is in the wrong place if I want the earlier declarations to stick
        # adding lines above!!
           
    return (max_val,min_val)
def main():
    while True:

        userInput = input("I bet you I can do this cool thing where I give you a tuple pair of your lowest and highest values...: ")
        
        nums = userInput.split(",")

        #for num in nums:       interesting idea to type verify, but comparisons will never exist like this in python
        #   if num == str:
        #      return main()
        # TRY THIS INSTEAD  Pun intended
        try:
            nums = [int(num) for num in nums]
            break # needed to break out of the infinite loop of while true
        except ValueError:
            print("Invalid input, please use comma-separated integers.\n")
            # return main() ATTENTION!!, this WORKS! but this keeps recursively calling main, not great if user keeps getting inputs wrong
        

    print(nums)
    print("\nThese numbers above are your full list.")
    print(maxAndMin(nums))
    print("AND THESE... ARE YOUR MAX AND MIN VALS")

if __name__ == "__main__":
    main()
