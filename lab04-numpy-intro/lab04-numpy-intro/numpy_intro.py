import numpy as np

def main():
    # 1. Create a 1D NumPy array
    arr = np.array([1, 2, 3, 4, 5])
    print("1D NumPy Array:")
    print(arr)

    # 2. Create a 2D NumPy array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D NumPy Matrix:")
    print(matrix)

    # 3. Create a 3x3 matrix of zeros
    zeros_matrix = np.zeros((3, 3))
    print("\n3x3 Matrix of Zeros:")
    print(zeros_matrix)

    # 4. Create a 3x3 matrix of ones
    ones_matrix = np.ones((3, 3))
    print("\n3x3 Matrix of Ones:")
    print(ones_matrix)

    # 5. Array addition and subtraction
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    sum_array = arr1 + arr2
    print("\nArray Addition:")
    print(sum_array)

    diff_array = arr1 - arr2
    print("\nArray Subtraction:")
    print(diff_array)

    # 6. Element-wise multiplication
    product_array = arr1 * arr2
    print("\nElement-wise Multiplication:")
    print(product_array)

    # 7. Matrix multiplication (dot product)
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix_product = np.dot(matrix1, matrix2)
    print("\nMatrix Dot Product (Multiplication):")
    print(matrix_product)

    # 8. Element-wise square
    square_array = np.square(arr1)
    print("\nElement-wise Square:")
    print(square_array)

    # 9. Element-wise square root
    sqrt_array = np.sqrt(arr1)
    print("\nElement-wise Square Root:")
    print(sqrt_array)

    # 10. Element-wise exponentiation
    exp_array = np.exp(arr1)
    print("\nElement-wise Exponentiation (e^x):")
    print(exp_array)

if __name__ == "__main__":
    main()