def double_list():
    # probem 1: given a list nums, return exactly double that, without modifying the original list
    nums = [5, 3, 8, 2, 1]
    #doubling = [nums*2 for num in nums] , this would create a list of lists, not what we want. It would replace each num with the whole list doubled (twice the list, not twice the value)
    # doubling = [nums[i]*2 for i in range(len(nums))] # this is what my c++ brain is telling me to do, but we are learning python!
    doubling = [num*2 for num in nums] # super clean, pythons list adding syntax works as [new_val for val in list], and we can just use num instead of nums[i] because we are already 
    #iterating through the list, so num is each element in the list as we go through it, and then we can just double that value and add it to the new list. this is faster than indexing 
        # key point, the variable after for is a temporary variable that holds current value of the list as it gets iterated through. makes it easy to use that val
    # food for thought: [str(num) for num in nums], -> this would create a list where all numbers are instead a string. 5 -> "5"
    #  clean = [x for x in data if x is not None] -> no missing values anymore
    print("This is the original list: ", nums)
    print("The doubled list: ", doubling)
    return doubling

def multiplicity():
    # problem 2: ["cat", "dog", "cat", "mongoose", "panda", "dog", "panda", "panda"] -> {"cat": 2, "dog": 2, "mongoose": 1, "panda": 3}

    #initially i wanted to add all elements from the list to dict as keys, then keep track of the count after for multiplicity. but this is better! not double passing through the list -> one and done

    animals = ["cat", "dog", "cat", "mongoose", "panda", "dog", "panda", "panda"]
    # this immediately tells dictionary, as we have to pair a name with a count (key -> value pairing), where keys always point to their value.
    dictionary_of_animals = {} # create an empty dictionary
    for animal in animals: # iterate over the list with animal as temp variable
        if animal in dictionary_of_animals: # if the animal already exists as a key, add one to its value
            dictionary_of_animals[animal] += 1
        else: # otherwise, create a new key and itialize its value to 1, as we have now seen it
            dictionary_of_animals[animal] = 1
    print(dictionary_of_animals)
    return dictionary_of_animals

def reverse_string():
    # problem 3: given the string "completionist" return the string in reverse order without built in functions
    # good practice on the idea of prepending, as you treat new info as the new front of the string in this case -> useful for undoing stacks or queues, or just reversing things in general
    string = "completionist"
    reversed_string = ""
    for char in string: #go through every character in the string
        reversed_string = char + reversed_string # starting with an empty string, add the current character to the front of the reversed string.
        # "completionist" -> 'c' + "" -> "o" + "c" + "" -> tsinoitelpmoc
    print("original: ", string)
    print("reversed: ", reversed_string)
    return reversed_string

def main ():
    double_list()
    multiplicity()
    reverse_string()
    print("works!") # program being fussy


if __name__ == "__main__":
    main()
    