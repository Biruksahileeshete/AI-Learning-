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
                    print(f"  {col}: {count} missing values ({count/len(self.df)*100:.1f}%)")


# ========================================
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


# ========================================
# METHOD: ensure_average_exists
# Ensures Average column exists
# ========================================

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
# Creates 8 enhanced data visualizations
# ========================================

    def create_visualizations(self):
        """Create multiple data visualizations"""
        if self.df is None:
            print("❌ No data loaded!")
            return
        
        self.ensure_average_exists()
        
        print("\n📊 Creating enhanced visualizations...")
        
        # ========================================
        # VISUALIZATION 1: Subject Performance
        # Bar chart showing average grades by subject
        # ========================================
        
        print("\n1️⃣ Creating Subject Performance Chart...")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        
        grade_cols = ['Grade_English', 'Grade_Math', 'Grade_Science', 'Grade_History']
        avg_grades = [self.df[col].mean() for col in grade_cols]
        subject_labels = ['English', 'Math', 'Science', 'History']
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
        
        bars = ax1.bar(subject_labels, avg_grades, color=colors, edgecolor='black', linewidth=1.5)
        ax1.set_title('📊 Average Grades by Subject', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Average Score', fontsize=12)
        ax1.set_ylim(0, 100)
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bar, value in zip(bars, avg_grades):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 2: Grade Distribution
        # Histogram showing grade distribution
        # ========================================
        
        print("\n2️⃣ Creating Grade Distribution Chart...")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        
        ax2.hist(self.df['Average'], bins=10, color='#45B7D1', edgecolor='black', alpha=0.7)
        ax2.set_title('📈 Grade Distribution', fontsize=16, fontweight='bold')
        ax2.set_xlabel('Average Grade', fontsize=12)
        ax2.set_ylabel('Number of Students', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add vertical line for average
        mean_grade = self.df['Average'].mean()
        ax2.axvline(mean_grade, color='red', linestyle='--', linewidth=2, 
                   label=f'Mean: {mean_grade:.2f}')
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 3: Study Hours vs Grades
        # Scatter plot with trend line
        # ========================================
        
        print("\n3️⃣ Creating Study Hours Analysis...")
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        
        # Scatter plot
        scatter = ax3.scatter(self.df['Study_Hours'], self.df['Average'], 
                            c=self.df['Average'], cmap='viridis', s=100, alpha=0.7)
        
        # Add trend line
        z = np.polyfit(self.df['Study_Hours'], self.df['Average'], 1)
        p = np.poly1d(z)
        ax3.plot(self.df['Study_Hours'], p(self.df['Study_Hours']), 
                color='red', linestyle='--', linewidth=2, label='Trend Line')
        
        ax3.set_title('📚 Study Hours vs Average Grade', fontsize=16, fontweight='bold')
        ax3.set_xlabel('Study Hours per Week', fontsize=12)
        ax3.set_ylabel('Average Grade', fontsize=12)
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Grade Score', fontsize=10)
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 4: Attendance vs Grades
        # Scatter plot with trend line
        # ========================================
        
        print("\n4️⃣ Creating Attendance Analysis...")
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        
        # Scatter plot
        scatter = ax4.scatter(self.df['Attendance'], self.df['Average'], 
                            c=self.df['Average'], cmap='plasma', s=100, alpha=0.7)
        
        # Add trend line
        z = np.polyfit(self.df['Attendance'], self.df['Average'], 1)
        p = np.poly1d(z)
        ax4.plot(self.df['Attendance'], p(self.df['Attendance']), 
                color='red', linestyle='--', linewidth=2, label='Trend Line')
        
        ax4.set_title('🎯 Attendance vs Average Grade', fontsize=16, fontweight='bold')
        ax4.set_xlabel('Attendance %', fontsize=12)
        ax4.set_ylabel('Average Grade', fontsize=12)
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Grade Score', fontsize=10)
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 5: Box Plot
        # Shows distribution of all subjects
        # ========================================
        
        print("\n5️⃣ Creating Box Plot Analysis...")
        fig5, ax5 = plt.subplots(figsize=(10, 6))
        
        data = [self.df['Grade_English'], self.df['Grade_Math'], 
                self.df['Grade_Science'], self.df['Grade_History']]
        box = ax5.boxplot(data, patch_artist=True)
        
        # Set x-axis labels manually for compatibility with older Matplotlib versions
        ax5.set_xticks([1, 2, 3, 4])
        ax5.set_xticklabels(['English', 'Math', 'Science', 'History'])
        
        # Color boxes
        for patch, color in zip(box['boxes'], ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']):
            patch.set_facecolor(color)
        
        ax5.set_title('📦 Subject Grade Distribution', fontsize=16, fontweight='bold')
        ax5.set_ylabel('Grades', fontsize=12)
        ax5.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 6: Pie Chart
        # Shows grade distribution categories
        # ========================================
        
        print("\n6️⃣ Creating Grade Category Distribution...")
        fig6, ax6 = plt.subplots(figsize=(8, 8))
        
        # Categorize grades
        grades = self.df['Average']
        categories = {
            'Excellent (90-100)': len(grades[grades >= 90]),
            'Good (80-89)': len(grades[(grades >= 80) & (grades < 90)]),
            'Average (70-79)': len(grades[(grades >= 70) & (grades < 80)]),
            'Below Average (60-69)': len(grades[(grades >= 60) & (grades < 70)]),
            'Poor (0-59)': len(grades[grades < 60])
        }
        
        labels = list(categories.keys())
        sizes = list(categories.values())
        colors = ['#2ECC71', '#F1C40F', '#E67E22', '#E74C3C', '#C0392B']
        explode = (0.1, 0, 0, 0, 0)  # Explode the first slice
        
        wedges, texts, autotexts = ax6.pie(sizes, labels=labels, colors=colors, 
                                           autopct='%1.1f%%', explode=explode,
                                           shadow=True, startangle=90)
        
        ax6.set_title('🎯 Grade Category Distribution', fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 7: Correlation Heatmap
        # Shows relationships between variables
        # ========================================
        
        print("\n7️⃣ Creating Correlation Heatmap...")
        fig7, ax7 = plt.subplots(figsize=(10, 8))
        
        # Calculate correlation matrix
        numeric_cols = self.df.select_dtypes(include=[np.number])
        corr = numeric_cols.corr()
        
        # Create heatmap
        im = ax7.imshow(corr, cmap='coolwarm', aspect='auto', interpolation='nearest')
        
        # Add labels
        ax7.set_xticks(range(len(corr.columns)))
        ax7.set_yticks(range(len(corr.columns)))
        ax7.set_xticklabels(corr.columns, rotation=45, ha='right')
        ax7.set_yticklabels(corr.columns)
        
        # Add values in cells
        for i in range(len(corr.columns)):
            for j in range(len(corr.columns)):
                text = ax7.text(j, i, f'{corr.iloc[i, j]:.2f}',
                               ha='center', va='center', color='black' if abs(corr.iloc[i, j]) < 0.5 else 'white',
                               fontsize=8)
        
        ax7.set_title('🔗 Correlation Heatmap', fontsize=16, fontweight='bold')
        
        # Add colorbar
        cbar = plt.colorbar(im)
        cbar.set_label('Correlation Coefficient', fontsize=10)
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # VISUALIZATION 8: Age Distribution
        # Shows age range of students
        # ========================================
        
        print("\n8️⃣ Creating Age Distribution Chart...")
        fig8, ax8 = plt.subplots(figsize=(10, 6))
        
        age_counts = self.df['Age'].value_counts().sort_index()
        
        bars = ax8.bar(age_counts.index, age_counts.values, color='#9B59B6', 
                      edgecolor='black', linewidth=1.5, alpha=0.7)
        
        ax8.set_title('👥 Student Age Distribution', fontsize=16, fontweight='bold')
        ax8.set_xlabel('Age', fontsize=12)
        ax8.set_ylabel('Number of Students', fontsize=12)
        ax8.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bar, value in zip(bars, age_counts.values):
            height = bar.get_height()
            ax8.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{value}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # ========================================
        # SUMMARY
        # ========================================
        
        print("\n" + "=" * 60)
        print("📊 VISUALIZATION COMPLETE!")
        print("=" * 60)
        print("\nCreated 8 visualizations:")
        print("  1. 📊 Subject Performance - Bar Chart")
        print("  2. 📈 Grade Distribution - Histogram")
        print("  3. 📚 Study Hours vs Grades - Scatter Plot")
        print("  4. 🎯 Attendance vs Grades - Scatter Plot")
        print("  5. 📦 Subject Grade Distribution - Box Plot")
        print("  6. 🎯 Grade Category Distribution - Pie Chart")
        print("  7. 🔗 Correlation Heatmap")
        print("  8. 👥 Age Distribution - Bar Chart")
        print("=" * 60)
        print("✅ All visualizations displayed successfully!")


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
        
        print("\n✅ Report saved to 'analysis_report.txt'")


# ========================================
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