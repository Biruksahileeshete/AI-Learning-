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
# ========================================
# MENU SYSTEM
# ========================================

def print_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("🔢 MATRIX CALCULATOR")
    print("=" * 50)
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Scalar Multiplication")
    print("5. Transpose Matrix")
    print("6. Determinant")
    print("7. Inverse Matrix")
    print("8. Element-wise Multiplication")
    print("9. View Matrix Statistics")
    print("10. Create Matrix")
    print("11. Display Matrix")
    print("12. Exit")
    print("=" * 50)

def get_matrix_input(calculator):
    """Get matrix input from user"""
    print("\n--- CREATE MATRIX ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    return calculator.create_matrix(rows, cols)

def main():
    """Main program loop"""
    calc = MatrixCalculator()
    
    # Create initial matrices
    print("\n🎯 Let's create two matrices first!")
    print("\n📌 MATRIX A:")
    calc.matrix_a = get_matrix_input(calc)
    calc.display_matrix(calc.matrix_a, "Matrix A")
    
    print("\n📌 MATRIX B:")
    calc.matrix_b = get_matrix_input(calc)
    calc.display_matrix(calc.matrix_b, "Matrix B")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-12): ")
        
        # 1. ADD MATRICES
        if choice == "1":
            try:
                result = calc.add_matrices(calc.matrix_a, calc.matrix_b)
                calc.display_matrix(result, "A + B")
            except ValueError as e:
                print(f"❌ Error: {e}")
                print("Matrices must have same dimensions!")
        
        # 2. SUBTRACT MATRICES
        elif choice == "2":
            try:
                result = calc.subtract_matrices(calc.matrix_a, calc.matrix_b)
                calc.display_matrix(result, "A - B")
            except ValueError as e:
                print(f"❌ Error: {e}")
                print("Matrices must have same dimensions!")
        
        # 3. MULTIPLY MATRICES
        elif choice == "3":
            try:
                result = calc.multiply_matrices(calc.matrix_a, calc.matrix_b)
                calc.display_matrix(result, "A × B")
            except ValueError as e:
                print(f"❌ Error: {e}")
                print("Columns of A must equal rows of B!")
        
        # 4. SCALAR MULTIPLICATION
        elif choice == "4":
            print("\n--- SCALAR MULTIPLICATION ---")
            scalar = float(input("Enter scalar value: "))
            matrix_choice = input("Multiply A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                result = calc.scalar_multiply(calc.matrix_a, scalar)
                calc.display_matrix(result, f"A × {scalar}")
            elif matrix_choice == "B":
                result = calc.scalar_multiply(calc.matrix_b, scalar)
                calc.display_matrix(result, f"B × {scalar}")
            else:
                print("❌ Invalid choice!")
        
        # 5. TRANSPOSE MATRIX
        elif choice == "5":
            print("\n--- TRANSPOSE ---")
            matrix_choice = input("Transpose A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                result = calc.transpose_matrix(calc.matrix_a)
                calc.display_matrix(result, "Aᵀ")
            elif matrix_choice == "B":
                result = calc.transpose_matrix(calc.matrix_b)
                calc.display_matrix(result, "Bᵀ")
            else:
                print("❌ Invalid choice!")
        
        # 6. DETERMINANT
        elif choice == "6":
            print("\n--- DETERMINANT ---")
            matrix_choice = input("Determinant of A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                det = calc.determinant(calc.matrix_a)
                if isinstance(det, str):
                    print(f"❌ {det}")
                else:
                    print(f"Det(A) = {det:.4f}")
            elif matrix_choice == "B":
                det = calc.determinant(calc.matrix_b)
                if isinstance(det, str):
                    print(f"❌ {det}")
                else:
                    print(f"Det(B) = {det:.4f}")
            else:
                print("❌ Invalid choice!")
        
        # 7. INVERSE MATRIX
        elif choice == "7":
            print("\n--- INVERSE MATRIX ---")
            matrix_choice = input("Inverse of A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                result = calc.inverse_matrix(calc.matrix_a)
                if isinstance(result, str):
                    print(f"❌ {result}")
                else:
                    calc.display_matrix(result, "A⁻¹")
            elif matrix_choice == "B":
                result = calc.inverse_matrix(calc.matrix_b)
                if isinstance(result, str):
                    print(f"❌ {result}")
                else:
                    calc.display_matrix(result, "B⁻¹")
            else:
                print("❌ Invalid choice!")
        
        # 8. ELEMENT-WISE MULTIPLICATION
        elif choice == "8":
            try:
                result = calc.element_wise_multiply(calc.matrix_a, calc.matrix_b)
                calc.display_matrix(result, "A ⊙ B (Element-wise)")
            except ValueError as e:
                print(f"❌ Error: {e}")
                print("Matrices must have same dimensions!")
        
        # 9. VIEW STATISTICS
        elif choice == "9":
            print("\n--- MATRIX STATISTICS ---")
            matrix_choice = input("Statistics for A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                stats = calc.get_statistics(calc.matrix_a)
                print(f"Shape: {calc.get_shape(calc.matrix_a)}")
                print(f"Mean: {stats['mean']:.4f}")
                print(f"Std Dev: {stats['std']:.4f}")
                print(f"Min: {stats['min']:.4f}")
                print(f"Max: {stats['max']:.4f}")
                print(f"Sum: {stats['sum']:.4f}")
            elif matrix_choice == "B":
                stats = calc.get_statistics(calc.matrix_b)
                print(f"Shape: {calc.get_shape(calc.matrix_b)}")
                print(f"Mean: {stats['mean']:.4f}")
                print(f"Std Dev: {stats['std']:.4f}")
                print(f"Min: {stats['min']:.4f}")
                print(f"Max: {stats['max']:.4f}")
                print(f"Sum: {stats['sum']:.4f}")
            else:
                print("❌ Invalid choice!")
        
        # 10. CREATE NEW MATRIX
        elif choice == "10":
            print("\n--- CREATE NEW MATRIX ---")
            matrix_name = input("Replace Matrix A or B? (A/B): ").upper()
            
            if matrix_name == "A":
                calc.matrix_a = get_matrix_input(calc)
                calc.display_matrix(calc.matrix_a, "New Matrix A")
            elif matrix_name == "B":
                calc.matrix_b = get_matrix_input(calc)
                calc.display_matrix(calc.matrix_b, "New Matrix B")
            else:
                print("❌ Invalid choice!")
        
        # 11. DISPLAY MATRIX
        elif choice == "11":
            print("\n--- DISPLAY MATRIX ---")
            matrix_choice = input("Display A or B? (A/B): ").upper()
            
            if matrix_choice == "A":
                calc.display_matrix(calc.matrix_a, "Matrix A")
            elif matrix_choice == "B":
                calc.display_matrix(calc.matrix_b, "Matrix B")
            else:
                print("❌ Invalid choice!")
        
        # 12. EXIT
        elif choice == "12":
            print("\n👋 Goodbye! Thanks for using Matrix Calculator!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-12")
        
        input("\nPress Enter to continue...")