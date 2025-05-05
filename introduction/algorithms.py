def count_even1(numbers, version=1):
    if version == 1:
        result = 0
        for x in numbers:
          if x % 2 == 0:
            result += 1
        return result
    elif version == 2:
       return sum(x % 2 == 0 for x in numbers)
    
def max_diff(numbers, version=1):
   if version == 1:
      result = 0
      for x in numbers:
         for y in numbers:
            result = max(result, abs(x - y))
      return result
   elif version == 2:
      sorted_1 = sorted(numbers)
      return sorted_1[-1] - sorted_1[0]
   elif version == 3:
      #I personally like this one
      return max(numbers) - min(numbers)  

def middle(numbers):
   return numbers[len(numbers) // 2]

def calc_sum(numbers):
   result = 0
   for x in numbers:
      result += x
   return result

def has_sum(numbers, x):
   for a in numbers:
      for b in numbers:
         if a+b == x:
            return True
   return False              
    
    

