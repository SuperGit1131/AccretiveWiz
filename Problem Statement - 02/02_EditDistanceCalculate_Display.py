# function for user's inputs
def user_inputs():
    string_array = input("Please input array list in the format, Eg: ABC,BCD,123,56,ABE,CDE ").split(',')  # Input array, format: "ABC,BCD,123,56,ABE,CDE"

    threshold = int(input("Please input distance Threshold, Eg. 2 "))  # default=2
    return string_array, threshold


# Python program to fin minimum iteration(s) in recursive way operations to convert str1 to str2
def calDistance(str1, str2, m, n):

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:

        return calDistance(str1, str2, m-1, n-1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(calDistance(str1, str2, m, n-1),    # Insert
                   calDistance(str1, str2, m-1, n),    # Remove
                   calDistance(str1, str2, m-1, n-1)    # Replace
                   )


def compute_results():

    # calling function for user's inputs
    string_array, threshold = user_inputs()

    # Length of an array
    length = len(string_array)

    # Dict having key element and values of
    # array elements which follows distance criteria
    final_dict = {}
    # processing
    for i in range(0, length-1):

        tmp_list = []  # Dict's Value list

        for j in range(i, length-1):
            distance = calDistance(string_array[i], string_array[j+1], len(string_array[i]), len(string_array[j+1]))

            if distance <= threshold:
                tmp_list.append(string_array[j+1])

        final_dict[string_array[i]] = tmp_list

    return final_dict  # return Dict having key element and values of Array elements which follows distance criteria


# Driver Code
if __name__ == '__main__':
    final_dict = compute_results()
    print('\nConsolidated Report: ', final_dict)
