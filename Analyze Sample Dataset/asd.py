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
# ========================================
# METHOD: show_basic_info
# Displays basic dataset information
# ========================================

    def show_basic_info(self):
        """Display basic information about the dataset"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("📋 BASIC INFORMATION")
        print("=" * 60)
        
        print(f"\nDataset Shape: {self.df.shape}")
        print(f"Rows: {self.df.shape[0]}")
        print(f"Columns: {self.df.shape[1]}")
        
        print("\n📊 Column Names:")
        for col in self.df.columns:
            print(f"  - {col}")
        
        print("\n📈 Data Types:")
        print(self.df.dtypes)
        
        print("\n🔍 First 5 Rows:")
        print(self.df.head())
        
        print("\n🔍 Last 5 Rows:")
        print(self.df.tail())
# ========================================
# METHOD: show_statistics
# Calculates and displays statistical summary
# ========================================

    def show_statistics(self):
        """Display statistical summary"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("📊 STATISTICAL SUMMARY")
        print("=" * 60)
        
        # Select only numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number])
        
        print("\n📈 Descriptive Statistics:")
        print(numeric_cols.describe())
        
        print("\n📊 Individual Statistics:")
        for col in numeric_cols.columns:
            print(f"\n{col}:")
            print(f"  Mean: {self.df[col].mean():.2f}")
            print(f"  Median: {self.df[col].median():.2f}")
            print(f"  Mode: {self.df[col].mode()[0]:.2f}")
            print(f"  Std Dev: {self.df[col].std():.2f}")
            print(f"  Min: {self.df[col].min():.2f}")
            print(f"  Max: {self.df[col].max():.2f}")
            print(f"  Range: {self.df[col].max() - self.df[col].min():.2f}")
            # ========================================
# METHOD: check_missing_data
# Checks for missing values in the dataset
# ========================================

    def check_missing_data(self):
        """Check for missing values"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("🔍 MISSING DATA CHECK")
        print("=" * 60)
        
        missing = self.df.isnull().sum()
        if missing.sum() == 0:
            print("✅ No missing values found!")
        else:
            print("\n❌ Missing values found:")
            for col, count in missing.items():
                if count > 0:
                    print(f"  {col}: {count} missing values ({count/len(self.df)*100:.1f}%)")# ========================================
# METHOD: analyze_grades
# Analyzes grade data across subjects
# ========================================

    def analyze_grades(self):
        """Analyze grade data"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("🎓 GRADE ANALYSIS")
        print("=" * 60)
        
        grade_cols = ['Grade_English', 'Grade_Math', 'Grade_Science', 'Grade_History']
        
        # Calculate averages
        print("\n📊 Average Grades:")
        for col in grade_cols:
            avg = self.df[col].mean()
            print(f"  {col.replace('Grade_', '')}: {avg:.2f}")
        
        # Overall average
        self.df['Average'] = self.df[grade_cols].mean(axis=1)
        print(f"\n📈 Overall Class Average: {self.df['Average'].mean():.2f}")
        
        # Grade distribution
        print("\n📊 Grade Distribution:")
        for col in grade_cols:
            print(f"\n  {col.replace('Grade_', '')}:")
            print(f"    A (90-100): {len(self.df[self.df[col] >= 90])}")
            print(f"    B (80-89): {len(self.df[(self.df[col] >= 80) & (self.df[col] < 90)])}")
            print(f"    C (70-79): {len(self.df[(self.df[col] >= 70) & (self.df[col] < 80)])}")
            print(f"    D (60-69): {len(self.df[(self.df[col] >= 60) & (self.df[col] < 70)])}")
            print(f"    F (0-59): {len(self.df[self.df[col] < 60])}")# ========================================
# METHOD: analyze_correlations
# Finds correlations between variables
# ========================================

    def analyze_correlations(self):
        """Analyze correlations between variables"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("🔗 CORRELATION ANALYSIS")
        print("=" * 60)
        
        numeric_cols = self.df.select_dtypes(include=[np.number])
        correlation = numeric_cols.corr()
        
        print("\n📊 Correlation Matrix:")
        print(correlation)
        
        # Find strongest correlations
        print("\n💡 Strongest Correlations:")
        for i in range(len(correlation.columns)):
            for j in range(i+1, len(correlation.columns)):
                corr = correlation.iloc[i, j]
                if abs(corr) > 0.5:
                    col1 = correlation.columns[i]
                    col2 = correlation.columns[j]
                    print(f"  {col1} ↔ {col2}: {corr:.3f}")