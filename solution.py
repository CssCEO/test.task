def can_jump(nums):
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jump)
        if max_reachable >= len(nums) - 1:
            return True
    return False
def parse_input(input_str):
    try:
        cleaned = input_str.replace(',', ' ')
        nums = list(map(int, cleaned.strip().split()))
        if not nums:
            raise ValueError("Список чисел пуст.")
        return nums
    except ValueError:
        print("Ошибка: введите целые числа, разделённые пробелами или запятыми.")
        return None
while True:
    user_input = input("Введите список чисел (через пробел или запятую): ")
    nums = parse_input(user_input)
    if nums is not None:
        result = can_jump(nums)
        print("Результат:", result)
        break
