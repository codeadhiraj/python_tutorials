import numpy as np
import pandas as pd

# NumPy: Creating an array and performing operations
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("NumPy Array:")
print(arr)

# Basic NumPy Operations
print("\nSum of all elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))
print("Transpose of array:\n", arr.T)

# Pandas: Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Basic Pandas Operations
print("\nAverage Salary:", df["Salary"].mean())
print("People above 28 years old:\n", df[df["Age"] > 28])
