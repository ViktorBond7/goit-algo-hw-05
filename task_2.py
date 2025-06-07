from typing import List, Tuple, Optional

def binary_search_upper_bound(arr: List[float], target: float) -> Tuple[int, Optional[float]]:
    left = 0
    right = len(arr) - 1
    iterations = 0
    result = None  # Тут збережемо верхню межу

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value >= target:
            result = mid_value  # Потенційна верхня межа
            right = mid - 1     # Продовжуємо шукати менший >= target
        else:
            left = mid + 1

    return (iterations, result)


if __name__ == '__main__':
    arr = [0.5, 1.2, 2.4, 3.6, 4.0, 5.1]
    target = 3.0

    print(binary_search_upper_bound(arr, target))
