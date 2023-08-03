def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Сравниваем корень с левым потомком
    if left < n and arr[i] < arr[left]:
        largest = left

    # Сравниваем корень с правым потомком
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если корень не самый большой, меняем с максимальным потомком
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Проходимся рекурсивно по поддереву
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение кучи (переупорядочивание массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи и упорядочиваем массив
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Пример использования:
if __name__ == "__main__":
    unsorted_array = [12, 11, 13, 5, 6, 7]
    print("Исходный массив:", unsorted_array)

    heap_sort(unsorted_array)
    print("Отсортированный массив:", unsorted_array)
