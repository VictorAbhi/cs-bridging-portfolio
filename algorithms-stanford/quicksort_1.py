# computing the total number of comparisons used to sort the given input file by QuickSort
# use first element as pivot

def quicksort(arr, left, right, comparison_count):
    if left >= right:
        return comparison_count
    
    # STEP 1: Choose pivot as first element
    pivot = arr[left]
    
    # STEP 2: (No need to swap since pivot is already at first position)
    
    # STEP 3: Partition
    i = left  # i marks boundary between elements < pivot and > pivot
    
    for j in range(left + 1, right + 1):  # Start from left+1 since left has pivot
        comparison_count += 1  # Count comparison
        if arr[j] < pivot:  # Note: < not <=
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # STEP 4: Put pivot in correct position
    arr[left], arr[i] = arr[i], arr[left]
    pivot_index = i
    
    # Recursively sort
    comparison_count = quicksort(arr, left, pivot_index - 1, comparison_count)
    comparison_count = quicksort(arr, pivot_index + 1, right, comparison_count)
    
    return comparison_count
def count_quick_sort_comparisons(arr):
    return quicksort(arr, 0, len(arr) - 1, 0)

if __name__ == "__main__":
    # Read input from file
    with open("quickSort.txt", "r") as file:
        arr = [int(line.strip()) for line in file.readlines()]

    # Count comparisons
    total_comparisons = count_quick_sort_comparisons(arr)

    # Print the total number of comparisons
    print("Total number of comparisons:", total_comparisons)