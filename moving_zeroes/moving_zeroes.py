'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    old_length = len(arr)

    # remove zero values and append zerped array to end
    arr = [v for v in arr if v != 0]
    new_length = len(arr)
    zero_length = old_length - new_length

    arr = arr + [0] * zero_length
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")