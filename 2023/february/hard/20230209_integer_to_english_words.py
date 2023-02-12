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
        def generate_english_sub_number(basic_numbers_dict, sub_num):
            if sub_num <= 20 or sub_num in [30, 40, 50, 60, 70, 80, 90]:
                return basic_numbers_dict[sub_num]
            
            str_num = str(sub_num)
            return f'{basic_numbers_dict[int(str_num[0]) * 10]} {basic_numbers_dict[int(str_num[1])]}'
        
        def check_hundred(basic_numbers_dict, str_num):
            if str_num[0] == '0':
                return f'{generate_english_sub_number(basic_numbers_dict, int(str_num[1:]))}'
            if str_num[1:] == '00':
                return f'{basic_numbers_dict[int(str_num[0])]} Hundred'
            return f'{basic_numbers_dict[int(str_num[0])]} Hundred {generate_english_sub_number(basic_numbers_dict, int(str_num[1:]))}'
        
        def check_thousand(basic_numbers_dict, str_num):
            idx = 1 if len(str_num) == 4 else 2
            if str_num[idx:] == '000':
                return f'{generate_english_sub_number(basic_numbers_dict, int(str_num[:idx]))} Thousand'
            english.append(generate_english_sub_number(basic_numbers_dict, int(str_num[:idx])))
            english.append('Thousand')
            english.append(check_hundred(basic_numbers_dict, str_num[idx:]))
            return ' '.join(english)
        
        def check_hundred_thousand(basic_numbers_dict, str_num):
            if str_num[0] == '0':
                return check_thousand(basic_numbers_dict, str_num[1:])
            if str_num[1:] == '00000':
                return f'{basic_numbers_dict[int(str_num[0])]} Hundred Thousand'
            temp_english = []
            if str_num[1:3] == '00':
                temp_english.append(f'{basic_numbers_dict[int(str_num[0])]} Hundred Thousand')
                temp_english.append(check_hundred(basic_numbers_dict, str_num[3:]))
            else:
                temp_english.append(f'{basic_numbers_dict[int(str_num[0])]} Hundred')
                temp_english.append(f'{generate_english_sub_number(basic_numbers_dict, int(str_num[1:3]))} Thousand')
                if str_num[3:] != '000':
                    temp_english.append(check_hundred(basic_numbers_dict, str_num[3:]))
            return ' '.join(temp_english)
        
        def check_million(basic_numbers_dict, str_num):
            temp_english = []
            if len(str_num) == 9:
                idx = 3
                temp_english.append(f'{check_hundred(basic_numbers_dict, str_num[:3])} Million')
            else:
                idx = 1 if len(str_num) == 7 else 2
                temp_english.append(f'{generate_english_sub_number(basic_numbers_dict, int(str_num[0:idx]))} Million')
            if str_num[idx:] == '0' * (len(str_num)-idx):
                pass
            elif str_num[idx:idx+3] == '000':
                temp_english.append(check_hundred(basic_numbers_dict, str_num[idx+3:]))
            else:
                hundred_thousand_str = check_hundred_thousand(basic_numbers_dict, str_num[idx:])
                if isinstance(hundred_thousand_str, str):
                    return ' '.join(temp_english) + ' ' + hundred_thousand_str
                temp_english += hundred_thousand_str
            return ' '.join(temp_english)
            

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
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        english = []
        str_num = str(num)
        str_num_length = len(str_num)
        if str_num_length < 3:
            return generate_english_sub_number(basic_numbers_dict, num)
        elif str_num_length == 3:
            return check_hundred(basic_numbers_dict, str_num)
        elif str_num_length > 3 and str_num_length <= 5:
            return check_thousand(basic_numbers_dict, str_num)
        elif str_num_length == 6:
            return check_hundred_thousand(basic_numbers_dict, str_num)
        elif str_num_length > 6 and str_num_length <= 9:
            return check_million(basic_numbers_dict, str_num)
        else:
            if str_num[1:4] == '000':
                if str_num[4:7] == '000':
                    if str_num[7:] == '000':
                        return f'{"One" if str_num[0] == "1" else "Two"} Billion'
                    return f'{"One" if str_num[0] == "1" else "Two"} Billion {check_hundred(basic_numbers_dict, str_num[7:])}'
                return f'{"One" if str_num[0] == "1" else "Two"} Billion {check_hundred_thousand(basic_numbers_dict, str_num[4:])}'
            return f'{"One" if str_num[0] == "1" else "Two"} Billion {check_million(basic_numbers_dict, str_num[1:])}'
i = 1100123456
print(i, Solution().numberToWords(i))