# write a function checking if any two numbers in a given set of numbers sum to 17.


def adds_to_17(number_set):
    for num_1 in number_set:
        for num_2 in number_set:
            if num_1 + num_2 == 17:  # no need to check for num1!=num2 as 17 is odd
                return True
    return False


num_set = {1, 2, 3}
print(adds_to_17(num_set))