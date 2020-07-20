# importing external libs/pkgs
from smallest_largest_integer import largest, smallest
import unittest


# Unit Testing Class
class UnitTesting(unittest.TestCase):

    def test_data(self):
        print("Test-Case:1 - To Check Largest with unique Values")
        self.assertAlmostEqual(largest([1, 2, 3], 3), 3)
        print("Test-Case:1 Passed")

        print("Test-Case:2 - To Check Largest with repetitive Values")
        self.assertAlmostEqual(largest([1, 2, 2], 3), 2)
        print("Test-Case:2 Passed")

        print("Test-Case:3 - To Check Smallest with repetitive Values")
        self.assertAlmostEqual(smallest([3, 6, 7, 0, 0], 5), 0)
        print("Test-Case:3 Passed")


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    # driver code
    while True:

        operation = (input("\nWhich operation to be executed?\n" + "Choice-'A' for SmallestLargestInteger Program\nChoice-'T' for Testing of SmallestLargestInteger program\nChoice-'E' for Exit\n")).lower()

        if operation == 'a':
            try:
                integer_array = []  # empty Arrayspython
                arr_len = input('Enter the length of an Array: ')
                print('Enter numbers in array: ')

                for i in range(int(arr_len)):
                    num = input("number: ")
                    integer_array.append(int(num))
                print('User Array: ', integer_array)

                n = len(integer_array)
                print('Largest number: ', largest(integer_array, n))
                print('Smallest number: ', smallest(integer_array, n))

            # Catch exception if inut is not number
            except Exception:
                print('Please enter values in Numeric format')

        elif operation == 't':
            unit_t = UnitTesting()
            unit_t.test_data()

        elif operation == 'e':
            print('Program ended, have a great time ahead..')
            break

        else:
            print('Please provide Correct Choice - (A/a or B/b or C/c)')
