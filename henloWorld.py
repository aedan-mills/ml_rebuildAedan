

def salutations(name):
    print("This is the first step towards improving my professional self!")
    print("How are ya,", name)
name = input("Enter your name: ")
salutations(name)    

def theCount(nums):
    count = 0 
    for num in nums:
        if num <= 5:
            count+=num
    return count

userNums = input("Enter numbers separated by commas please: ")
nums = userNums.split(",")
nums = [int(i) for i in nums]
print(nums)

print("Watch This! I will add it up: ",theCount(nums))

print("Now iff'n you a fancy pants, I reckon you noticed there are no numbers above 5 counted")
print("That's because I can't count above 5, unless doing the count.")
