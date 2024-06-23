# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Split string > fist will directly add up > based on priority we will subtract the chars > if the first char is higher priority then we add the value to total>
# question is to convert roman string to number

dict_temp_roman_gt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
priority_dict = {"I":1,"V":2,"X":3,"L":4,"C":5,"D":6,"M":7}

input_str = "III"

list_str = [i for i in input_str]
length = len(list_str)

total = 0
skip_next = False
for i in range(0, length):
  if skip_next:
    skip_next = False
    continue

  if i == length-1:
    current_ele = list_str[i]
    current_value = dict_temp_roman_gt[current_ele]
    total+=current_value
    continue
    # total+=priority_dict[list_str[i]]

  current_ele = list_str[i]
  next_ele = list_str[i+1]

  current_value = dict_temp_roman_gt[current_ele]
  next_value = dict_temp_roman_gt[next_ele]

  priority_current = priority_dict[current_ele]
  priority_next = priority_dict[next_ele]

  if priority_current<priority_next:
    add_to_total = next_value-current_value
    total += add_to_total
    skip_next = True
  else:
    total += current_value

