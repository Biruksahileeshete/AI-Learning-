# ========================================
# MATRIX CALCULATOR
# Using NumPy for Array & Matrix Operations
# ========================================

import numpy as np

class MatrixCalculator:
    """A simple matrix calculator for basic operations"""
    
    def __init__(self):
        self.matrix_a = None
        self.matrix_b = None
        self.result = None
    
    def create_matrix(self, rows, cols):
        """Create a matrix with user input"""
        print(f"\nEnter values for {rows}x{cols} matrix (row by row):")
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = float(input(f"Enter value at position ({i+1},{j+1}): "))
                row.append(value)
            matrix.append(row)
        return np.array(matrix)
    
    def display_matrix(self, matrix, name="Matrix"):
        """Display a matrix in a nice format"""
        print(f"\n{name}:")
        print("=" * 40)
        for row in matrix:
            print("|", end=" ")
            for element in row:
                print(f"{element:8.2f}", end=" ")
            print("|")
        print("=" * 40)
    
    def add_matrices(self, a, b):
        """Add two matrices"""
        return np.add(a, b)
    
    def subtract_matrices(self, a, b):
        """Subtract matrix b from matrix a"""
        return np.subtract(a, b)
    
    def multiply_matrices(self, a, b):
        """Multiply two matrices"""
        return np.dot(a, b)
    
    def scalar_multiply(self, matrix, scalar):
        """Multiply matrix by a scalar"""
        return matrix * scalar
    
    def transpose_matrix(self, matrix):
        """Find transpose of a matrix"""
        return np.transpose(matrix)
    
    def determinant(self, matrix):
        """Calculate determinant of a matrix"""
        if matrix.shape[0] != matrix.shape[1]:
            return "Not a square matrix!"
        return np.linalg.det(matrix)
    
    def inverse_matrix(self, matrix):
        """Find inverse of a matrix"""
        if matrix.shape[0] != matrix.shape[1]:
            return "Not a square matrix!"
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            return "Matrix is singular (no inverse)!"
    
    def element_wise_multiply(self, a, b):
        """Element-wise multiplication (Hadamard product)"""
        return np.multiply(a, b)
    
    def get_shape(self, matrix):
        """Get shape of matrix"""
        return matrix.shape
    
    def get_statistics(self, matrix):
        """Get statistics of matrix"""
        stats = {
            'mean': np.mean(matrix),
            'std': np.std(matrix),
            'min': np.min(matrix),
            'max': np.max(matrix),
            'sum': np.sum(matrix)
        }
        return stats