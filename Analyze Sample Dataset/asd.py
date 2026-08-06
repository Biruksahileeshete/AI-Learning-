# ========================================
# DAY 3: ANALYZE SAMPLE DATASET
# Using Pandas, NumPy, and Matplotlib
# ========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# ========================================
# CLASS: DataAnalyzer
# Main class for data analysis operations
# ========================================

class DataAnalyzer:
    """Simple data analysis tool for sample datasets"""
    
    def __init__(self):
        self.data = None
        self.df = None
# ========================================
# METHOD: create_sample_data
# Generates a sample student dataset
# ========================================

    def create_sample_data(self):
        """Create a sample dataset"""
        print("\n📊 Creating sample dataset...")
        
        # Sample student data
        data = {
            'Student_ID': [f'S{str(i).zfill(3)}' for i in range(1, 21)],
            'Name': [
                'Alice', 'Bob', 'Charlie', 'Diana', 'Eve',
                'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
                'Kelly', 'Leo', 'Mia', 'Noah', 'Olivia',
                'Peter', 'Quinn', 'Rose', 'Sam', 'Tina'
            ],
            'Age': np.random.randint(18, 25, 20),
            'Grade_English': np.random.randint(50, 100, 20),
            'Grade_Math': np.random.randint(40, 100, 20),
            'Grade_Science': np.random.randint(45, 100, 20),
            'Grade_History': np.random.randint(50, 95, 20),
            'Study_Hours': np.random.randint(1, 10, 20),
            'Attendance': np.random.randint(60, 100, 20)
        }
        
        self.df = pd.DataFrame(data)
        print("✅ Dataset created successfully!")
        return self.df
# ========================================
# METHOD: load_from_csv
# Loads data from a CSV file
# ========================================

    def load_from_csv(self, filename):
        """Load data from CSV file"""
        try:
            self.df = pd.read_csv(filename)
            print(f"✅ Data loaded from {filename}")
            return self.df
        except FileNotFoundError:
            print(f"❌ File {filename} not found!")
            return None
# ========================================
# METHOD: save_to_csv
# Saves data to a CSV file
# ========================================

    def save_to_csv(self, filename):
        """Save data to CSV file"""
        if self.df is not None:
            self.df.to_csv(filename, index=False)
            print(f"✅ Data saved to {filename}")
        else:
            print("❌ No data to save!")