# Class to hold the rearrangement solution
class Solution:
    # Function to rearrange first half ascending and second half descending
    def rearrangeArray(self, arr):
        # Sort the array
        arr.sort()

        n = len(arr)
        # Reverse the second half
        arr[n//2:] = reversed(arr[n//2:])

# Driver code
if __name__ == "__main__":
    arr = list(map(int,input("Enter elements separated by space:  ").split()))
    sol = Solution()
    sol.rearrangeArray(arr)
    print(arr)