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
            print(f"    F (0-59): {len(self.df[self.df[col] < 60])}")

    def ensure_average_exists(self):
        """Ensure the Average column exists for the dataset."""
        if self.df is None:
            return

        grade_cols = ['Grade_English', 'Grade_Math', 'Grade_Science', 'Grade_History']
        if 'Average' not in self.df.columns:
            if all(col in self.df.columns for col in grade_cols):
                self.df['Average'] = self.df[grade_cols].mean(axis=1)
            else:
                print("❌ Cannot compute Average: grade columns are missing.")

# ========================================
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
                    # ========================================
# METHOD: find_top_performers
# Identifies top performing students
# ========================================

    def find_top_performers(self, n=5):
        """Find top performing students"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print(f"🏆 TOP {n} PERFORMING STUDENTS")
        print("=" * 60)
        
        grade_cols = ['Grade_English', 'Grade_Math', 'Grade_Science', 'Grade_History']
        self.df['Average'] = self.df[grade_cols].mean(axis=1)
        
        top_students = self.df.nlargest(n, 'Average')
        
        print("\nTop Students:")
        for i, (_, row) in enumerate(top_students.iterrows(), 1):
            print(f"\n{i}. {row['Name']} (ID: {row['Student_ID']})")
            print(f"   Average: {row['Average']:.2f}")
            print(f"   English: {row['Grade_English']}")
            print(f"   Math: {row['Grade_Math']}")
            print(f"   Science: {row['Grade_Science']}")
            print(f"   History: {row['Grade_History']}")
            print(f"   Study Hours: {row['Study_Hours']}")
            print(f"   Attendance: {row['Attendance']}%")


# ========================================
# METHOD: create_visualizations
# Creates data visualizations
# ========================================

    def create_visualizations(self):
        """Create data visualizations"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        self.ensure_average_exists()
        
        print("\n📊 Creating visualizations...")
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Student Data Analysis', fontsize=16)
        
        # 1. Grade Distribution
        grade_cols = ['Grade_English', 'Grade_Math', 'Grade_Science', 'Grade_History']
        avg_grades = [self.df[col].mean() for col in grade_cols]
        axes[0, 0].bar(grade_cols, avg_grades, color=['blue', 'green', 'red', 'orange'])
        axes[0, 0].set_title('Average Grades by Subject')
        axes[0, 0].set_ylabel('Average Score')
        axes[0, 0].set_ylim(0, 100)
        
        # 2. Study Hours vs Grades
        axes[0, 1].scatter(self.df['Study_Hours'], self.df['Average'], color='purple', alpha=0.6)
        axes[0, 1].set_title('Study Hours vs Average Grade')
        axes[0, 1].set_xlabel('Study Hours')
        axes[0, 1].set_ylabel('Average Grade')
        
        # 3. Attendance vs Grades
        axes[1, 0].scatter(self.df['Attendance'], self.df['Average'], color='green', alpha=0.6)
        axes[1, 0].set_title('Attendance vs Average Grade')
        axes[1, 0].set_xlabel('Attendance %')
        axes[1, 0].set_ylabel('Average Grade')
        
        # 4. Grade Distribution Histogram
        axes[1, 1].hist(self.df['Average'], bins=10, color='orange', edgecolor='black')
        axes[1, 1].set_title('Grade Distribution')
        axes[1, 1].set_xlabel('Average Grade')
        axes[1, 1].set_ylabel('Number of Students')
        
        plt.tight_layout()
        plt.show()
        print("✅ Visualizations displayed!")


# ========================================
# METHOD: generate_report
# Generates complete analysis report
# ========================================

    def generate_report(self):
        """Generate a complete analysis report"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        print("\n" + "=" * 60)
        print("📋 COMPLETE ANALYSIS REPORT")
        print("=" * 60)
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Show all analysis
        self.show_basic_info()
        self.show_statistics()
        self.check_missing_data()
        self.analyze_grades()
        self.analyze_correlations()
        self.find_top_performers(3)
        
        # Save report to text file
        with open('analysis_report.txt', 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("STUDENT DATA ANALYSIS REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("Dataset Information:\n")
            f.write(f"  Total Students: {len(self.df)}\n")
            f.write(f"  Subjects: English, Math, Science, History\n")
            f.write(f"  Average Grade: {self.df['Average'].mean():.2f}\n")
            f.write(f"  Top Student: {self.df.nlargest(1, 'Average')['Name'].iloc[0]}\n")
        
        print("\n✅ Report saved to 'analysis_report.txt'")# ========================================
# METHOD: run_analysis
# Main program loop with menu
# ========================================

    def run_analysis(self):
        """Run complete analysis"""
        print("\n🎯 WELCOME TO DATA ANALYSIS TOOL")
        print("=" * 50)
        
        # Create or load data
        choice = input("\nLoad data from CSV or create sample? (L/S): ").upper()
        
        if choice == 'L':
            filename = input("Enter CSV filename: ")
            self.load_from_csv(filename)
        else:
            self.create_sample_data()
            self.save_to_csv('student_data.csv')
        
        if self.df is None:
            print("❌ No data available. Exiting...")
            return
        
        # Menu loop
        while True:
            print("\n" + "=" * 50)
            print("📊 DATA ANALYSIS MENU")
            print("=" * 50)
            print("1. Show Basic Info")
            print("2. Show Statistics")
            print("3. Check Missing Data")
            print("4. Analyze Grades")
            print("5. Analyze Correlations")
            print("6. Find Top Performers")
            print("7. Create Visualizations")
            print("8. Generate Full Report")
            print("9. Save Data to CSV")
            print("10. Exit")
            print("=" * 50)
            
            choice = input("\nEnter your choice (1-10): ")
            
            if choice == '1':
                self.show_basic_info()
            elif choice == '2':
                self.show_statistics()
            elif choice == '3':
                self.check_missing_data()
            elif choice == '4':
                self.analyze_grades()
            elif choice == '5':
                self.analyze_correlations()
            elif choice == '6':
                n = int(input("How many top students to show? (default 5): ") or 5)
                self.find_top_performers(n)
            elif choice == '7':
                self.ensure_average_exists()
                self.create_visualizations()
            elif choice == '8':
                self.ensure_average_exists()
                self.generate_report()
            elif choice == '9':
                filename = input("Enter filename to save: ")
                self.save_to_csv(filename)
            elif choice == '10':
                print("\n👋 Goodbye! Thanks for using Data Analysis Tool!")
                break
            else:
                print("❌ Invalid choice!")
            
            input("\nPress Enter to continue...")


# ========================================
# MAIN PROGRAM - Entry Point
# ========================================

if __name__ == "__main__":
    print("\n🎯 WELCOME TO DATA ANALYSIS TOOL")
    print("Learn to analyze datasets with Python!")
    print("=" * 50)
    
    analyzer = DataAnalyzer()
    analyzer.run_analysis()