import random
import timeit
import csv

# --- Алгоритми --- #
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Налаштування тестів --- #
sizes = [1000, 5000, 10000]
algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Timsort (Python)": sorted
}

results = []

for n in sizes:
    data = [random.randint(0, 100000) for _ in range(n)]
    row = [n]
    for name, func in algorithms.items():
        t = timeit.timeit(lambda: func(data), number=3)
        row.append(round(t, 5))
    results.append(row)

# --- Вивід у форматі Markdown --- #
table_md = "\n## Результати тестування\n\n"
table_md += "| Розмір масиву | Insertion Sort | Merge Sort | Timsort (Python) |\n"
table_md += "|---------------|----------------|------------|------------------|\n"
for row in results:
    table_md += f"| {row[0]} | {row[1]} сек | {row[2]} сек | {row[3]} сек |\n"

print(table_md)

# --- Збереження у CSV --- #
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Array Size", "Insertion Sort (sec)", "Merge Sort (sec)", "Timsort (sec)"])
    writer.writerows(results)

# --- Формування README.md --- #
readme_content = f"""# Порівняння алгоритмів сортування: Insertion Sort, Merge Sort та Timsort

## Теоретичний аналіз

| Алгоритм            | Найгірший випадок | Середній випадок | Найкращий випадок | Особливості |
|----------------------|------------------|------------------|-------------------|-------------|
| Insertion Sort       | O(n²)            | O(n²)            | O(n)              | Ефективний на малих та майже відсортованих масивах |
| Merge Sort           | O(n log n)       | O(n log n)       | O(n log n)        | Стабільний, але потребує додаткової пам’яті |
| Timsort (Python)     | O(n log n)       | O(n log n)       | O(n)              | Адаптивний: поєднання Merge Sort та Insertion Sort |

{table_md}

## Висновки

1. **Insertion Sort** — дуже повільний на великих наборах даних, але швидкий на маленьких або майже відсортованих.
2. **Merge Sort** — стабільно швидкий, але не використовує локально відсортовані ділянки.
3. **Timsort (Python)** — найефективніший завдяки адаптивності: комбінує переваги Merge Sort і Insertion Sort.

✅ Отримані результати підтверджують теоретичний аналіз: **Timsort значно ефективніший** і саме тому використовується у Python у `sorted()` та `.sort()`.
"""

with open("readme.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("\n✅ Результати збережено у results.csv та readme.md")

