def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    being_sorted = to_be_sorted[:]
    iterations = 0
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
                digit = int(digit)
            except IndexError:
                digit = 0

            digits[digit].append(number)

            being_sorted = []
            iterations += 1
        for numeral in digits:
            being_sorted.extend(numeral)
        print(being_sorted)
        print("---------------------------------------")
    print("Process completed in {0} iterations.".format(iterations))
    return being_sorted


# unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
# print(unsorted_list)
# print("--------------------------------------")
# radix_sort(unsorted_list)



