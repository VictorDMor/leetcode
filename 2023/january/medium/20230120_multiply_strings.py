'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def build_number(number_dict, number, string_number):
            for i in range(len(string_number)):
                multiplier = 10**(len(string_number[i:])-1)
                number += numbers[string_number[i]] * multiplier
            return number

        numbers = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        number_1 = build_number(numbers, 0, num1)
        number_2 = build_number(numbers, 0, num2)
        return str(number_1 * number_2)