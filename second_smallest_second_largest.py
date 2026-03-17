# Function to find the second smallest and second largest elements in the array
def getElements(arr, n):
    # Edge case: when the array has less than 2 elements
    if n < 2:
        print(-1, -1)  # Print -1 for both second smallest and second largest
        return

    # Initialize variables to track the smallest, second smallest, largest, and second largest elements
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    # Find the smallest and largest elements in the array
    for i in range(n):
        small = min(small, arr[i])  # Update the smallest element
        large = max(large, arr[i])  # Update the largest element

    # Find the second smallest and second largest elements
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]  # Update second smallest if a smaller element is found
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]  # Update second largest if a larger element is found

    # Output the second smallest and second largest elements
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

# Driver code
if __name__ == "__main__":
    n =int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))  # Array of elements
    
    # Call the function to find and print the second smallest and second largest elements
    getElements(arr, n)