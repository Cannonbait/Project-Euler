import math

hash_num10 = {}

def seed_hash_num10():
  for i in range(0, 10):
    hash_num10[i] = set()

def sum_10(str_num):
  sum = 0
  for num in str_num:
    sum += int(num)
  return sum

def complete_sub(num):
  return set(range(0, len(str(num)))) == hash_num10[num]

def substring_10(num):
  str_num = str(num)
  if num in hash_num10:
    return complete_sub(num)
  prenum = int(str_num[:-1])
  index = len(str_num)
  sum = 0
  while sum < 10 and index > 0:
    index -= 1
    sum += int(str_num[index])
  if sum == 10:
    num_set = set(range(index, len(str_num)))
    num_set = num_set.union(hash_num10[prenum])
    hash_num10[num] = num_set
    return complete_sub(num)
  else:
    hash_num10[num] = hash_num10[prenum]
    return False

def count_num_substr_10(exponent):
  count = 0
  for i in range (1, 10**exponent):
    if substring_10(i):
      count += 1
  return count

seed_hash_num10()
print(count_num_substr_10(6))
#print(hash_num10)
#print(count_num_substr_10(5))
#print(is_substr_10(190))