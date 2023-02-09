'''
273. Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= (2**31)-1
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        basic_numbers_dict = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            40: 'Forty',
        }

        if num <= 20:
            return basic_numbers_dict[num]

        for i in [30, 50, 60, 70, 80, 90]:
            basic_numbers_dict[i] = basic_numbers_dict[10+int(str(i)[0])][:-3] + 'y'
        english = []
        decimal_place = 0
        for i in range(len(str(num))-1, -1, -1):
            if decimal_place >= 2:
                if int(str(num)[i]) != 0:
                    if decimal_place == 2:
                        english.insert(0, 'Hundred')
                        idx = int(str(num)[i])
                    elif decimal_place == 3:
                        english.insert(0, 'Thousand')
                        idx = int(str(num)[i])
                    elif decimal_place == 4:
                        if 'Thousand' in english:
                            english.remove('Thousand')
                            english.pop(0)
                        english.insert(0, 'Thousand')
                        number = int((str(num)[i:i+2]))
                        if number > 20:
                            english.insert(0, basic_numbers_dict[int(str(number)[-1])])
                            idx = int(str(number)[0]) * 10
                        else:
                            idx = number
                    english.insert(0, basic_numbers_dict[idx])
            else:
                if int(str(num)[i]) != 0:
                    english.insert(0, basic_numbers_dict[int(str(num)[i]) * (10 ** decimal_place)])
            decimal_place += 1
        if 'Zero' in english:
            english.remove('Zero')
        return ' '.join(english)
    
for i in range(10000, 99999):
    print(i, Solution().numberToWords(i))