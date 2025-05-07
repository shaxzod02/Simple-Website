def min_diff(numbers):
    numbers = sorted(numbers)  # Asl ro'yxat o'zgarmaydi

    result = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        result = min(result, numbers[i] - numbers[i - 1])
    
    return result

def min_diff(numbers):
    numbers = sorted(numbers)  # Asl ro'yxat o'zgarmaydi

    result = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        result = min(result, numbers[i] - numbers[i - 1])
    
    return result
