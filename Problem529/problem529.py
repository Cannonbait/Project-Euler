substr_10 = {}

def sum_10(str_num):
	sum = 0
	for num in str_num:
		sum += int(num)
	return sum

def is_substr_10(num):
  if num in substr_10:
    return substr_10[num]
  start = 0
  end = 1
  str_num = str(num)
  len_num = len(str_num)
  while end <= len_num:
    sum = sum_10(str_num[start:end])
    #print("Start: %d, End: %d, Sum: %d" % (start, end, sum))
    if sum < 10:
      end += 1
    elif sum > 10:
      substr_10[num] = False
      return False
    elif end == len_num:
      substr_10[num] = True
      return True
    elif str_num[end] == '0':
      end += 1
    else: 
      val = is_substr_10(int(str_num[end:]))
      substr_10[num] = val
      return val

def count_num_substr_10(exponent):
  count = 0
  for i in range (1, 10**exponent):
    if is_substr_10(i):
      count += 1
  return count
print(count_num_substr_10(2))
#print(count_num_substr_10(5))
#print(is_substr_10(190))