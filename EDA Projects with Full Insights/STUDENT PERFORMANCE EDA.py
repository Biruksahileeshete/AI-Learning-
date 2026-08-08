# ========================================
# STUDENT PERFORMANCE EDA
# Complete Exploratory Data Analysis
# ========================================

import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

class StudentEDA:
    def __init__(self):
        self.df = None
        self.output_dir = Path(__file__).resolve().parent / "visualizations"
        self.output_dir.mkdir(exist_ok=True)

    def save_figure(self, filename, fig=None):
        """Save a matplotlib figure to the visualizations folder."""
        if fig is None:
            fig = plt.gcf()
        path = self.output_dir / filename
        fig.subplots_adjust(top=0.92, bottom=0.08, left=0.06, right=0.98, hspace=0.35, wspace=0.25)
        fig.savefig(path, dpi=200, bbox_inches='tight')
        plt.close(fig)
        return path
    
    def create_dataset(self):
        """Create comprehensive student dataset"""
        np.random.seed(42)
        n = 200  # 200 students
        
        data = {
            'Student_ID': [f'S{str(i).zfill(3)}' for i in range(1, n+1)],
            'Age': np.random.randint(18, 26, n),
            'Gender': np.random.choice(['Male', 'Female'], n, p=[0.48, 0.52]),
            'Study_Hours': np.random.randint(2, 15, n),
            'Attendance': np.random.randint(60, 100, n),
            'Previous_GPA': np.round(np.random.uniform(2.0, 4.0, n), 2),
            'Sleep_Hours': np.random.randint(4, 10, n),
            'Extracurricular': np.random.choice(['Yes', 'No'], n, p=[0.7, 0.3]),
            'Part_Time_Job': np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6]),
            'Family_Income': np.random.choice(['Low', 'Medium', 'High'], n, p=[0.2, 0.5, 0.3]),
            'Grade_Math': np.random.randint(40, 100, n),
            'Grade_English': np.random.randint(50, 100, n),
            'Grade_Science': np.random.randint(45, 100, n),
        }
        
        self.df = pd.DataFrame(data)
        
        # Add calculated columns
        self.df['Average_Grade'] = self.df[['Grade_Math', 'Grade_English', 'Grade_Science']].mean(axis=1)
        self.df['Performance'] = pd.cut(self.df['Average_Grade'], 
                                        bins=[0, 60, 70, 80, 90, 100],
                                        labels=['Poor', 'Below Avg', 'Average', 'Good', 'Excellent'])
        return self.df
    
    def load_data(self, filename):
        """Load data from CSV"""
        self.df = pd.read_csv(filename)
        return self.df
    
    def data_overview(self):
        """1. Data Overview"""
        print("\n" + "="*60)
        print("📊 DATA OVERVIEW")
        print("="*60)
        
        print(f"\nTotal Students: {len(self.df)}")
        print(f"Total Features: {len(self.df.columns)}")
        print(f"\nData Types:\n{self.df.dtypes}")
        
        print("\nFirst 5 Rows:")
        print(self.df.head())
        
        print("\nDataset Info:")
        print(self.df.info())
        
        print("\nMissing Values:")
        print(self.df.isnull().sum())
    
    def descriptive_statistics(self):
        """2. Descriptive Statistics"""
        print("\n" + "="*60)
        print("📊 DESCRIPTIVE STATISTICS")
        print("="*60)
        
        numeric_cols = self.df.select_dtypes(include=[np.number])
        
        print("\nNumerical Columns Stats:")
        print(numeric_cols.describe())
        
        print("\nSkewness (data distribution shape):")
        print(numeric_cols.skew())
        
        print("\nKurtosis (data tail heaviness):")
        print(numeric_cols.kurtosis())
        
        print("\nCategorical Columns Stats:")
        for col in self.df.select_dtypes(include=['object', 'string']).columns:
            print(f"\n{col}:")
            print(f"  Unique values: {self.df[col].nunique()}")
            print(f"  Top value: {self.df[col].value_counts().index[0]} ({self.df[col].value_counts().values[0]})")
    
    def univariate_analysis(self):
        """3. Univariate Analysis (single variables)"""
        print("\n" + "="*60)
        print("📊 UNIVARIATE ANALYSIS")
        print("="*60)
        
        # Numerical variables
        num_cols = ['Age', 'Study_Hours', 'Attendance', 'Sleep_Hours', 'Average_Grade']
        
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        fig.suptitle('Univariate Analysis - Numerical Variables', fontsize=16, fontweight='bold')
        
        for i, col in enumerate(num_cols):
            row = i // 3
            col_pos = i % 3
            
            # Histogram
            axes[row, col_pos].hist(self.df[col], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
            axes[row, col_pos].axvline(self.df[col].mean(), color='red', linestyle='--', 
                                       label=f'Mean: {self.df[col].mean():.1f}')
            axes[row, col_pos].axvline(self.df[col].median(), color='green', linestyle='--', 
                                       label=f'Median: {self.df[col].median():.1f}')
            axes[row, col_pos].set_title(f'{col}', fontsize=12, fontweight='bold')
            axes[row, col_pos].set_xlabel(col)
            axes[row, col_pos].set_ylabel('Frequency')
            axes[row, col_pos].legend()
            axes[row, col_pos].grid(True, alpha=0.3)
        
        plt.tight_layout()
        self.save_figure('01_univariate_numerical.png')
        
        # Categorical variables
        cat_cols = ['Gender', 'Extracurricular', 'Part_Time_Job', 'Family_Income', 'Performance']
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Univariate Analysis - Categorical Variables', fontsize=16, fontweight='bold')
        
        for i, col in enumerate(cat_cols):
            row = i // 3
            col_pos = i % 3
            
            counts = self.df[col].value_counts()
            axes[row, col_pos].bar(counts.index, counts.values, color='lightcoral', edgecolor='black')
            axes[row, col_pos].set_title(f'{col}', fontsize=12, fontweight='bold')
            axes[row, col_pos].set_xlabel(col)
            axes[row, col_pos].set_ylabel('Count')
            axes[row, col_pos].grid(True, alpha=0.3, axis='y')
            
            # Add value labels
            for j, v in enumerate(counts.values):
                axes[row, col_pos].text(j, v + 0.5, str(v), ha='center', fontweight='bold')
        
        # Remove empty subplot
        if len(cat_cols) < 6:
            fig.delaxes(axes[1, 2])
        
        plt.tight_layout()
        self.save_figure('02_univariate_categorical.png')
        
        # Print key findings
        print("\n🔍 Key Findings from Univariate Analysis:")
        print(f"  - Average Age: {self.df['Age'].mean():.1f} years")
        print(f"  - Average Study Hours: {self.df['Study_Hours'].mean():.1f} hours/week")
        print(f"  - Average Attendance: {self.df['Attendance'].mean():.1f}%")
        print(f"  - Overall GPA: {self.df['Average_Grade'].mean():.1f}")
        print(f"  - Most students: {self.df['Performance'].value_counts().index[0]}")
        print(f"  - Gender distribution: {self.df['Gender'].value_counts().to_dict()}")
    
    def bivariate_analysis(self):
        """4. Bivariate Analysis (relationships)"""
        print("\n" + "="*60)
        print("📊 BIVARIATE ANALYSIS")
        print("="*60)
        
        # Correlation heatmap
        numeric_cols = self.df.select_dtypes(include=[np.number])
        
        fig, ax = plt.subplots(figsize=(12, 8))
        corr = numeric_cols.corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', center=0,
                    fmt='.2f', linewidths=0.5, ax=ax)
        ax.set_title('Correlation Heatmap - All Numerical Variables', fontsize=16, fontweight='bold')
        self.save_figure('03_correlation_heatmap.png', fig)
        
        # Key scatter plots
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle('Key Relationships', fontsize=16, fontweight='bold')
        
        # 1. Study Hours vs Grade
        axes[0, 0].scatter(self.df['Study_Hours'], self.df['Average_Grade'], 
                          alpha=0.6, c='blue')
        z = np.polyfit(self.df['Study_Hours'], self.df['Average_Grade'], 1)
        p = np.poly1d(z)
        axes[0, 0].plot(self.df['Study_Hours'], p(self.df['Study_Hours']), 
                       color='red', linewidth=2, label='Trend')
        axes[0, 0].set_xlabel('Study Hours', fontsize=11)
        axes[0, 0].set_ylabel('Average Grade', fontsize=11)
        axes[0, 0].set_title('Study Hours vs Grade', fontweight='bold')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].legend()
        
        # 2. Attendance vs Grade
        axes[0, 1].scatter(self.df['Attendance'], self.df['Average_Grade'], 
                          alpha=0.6, c='green')
        z = np.polyfit(self.df['Attendance'], self.df['Average_Grade'], 1)
        p = np.poly1d(z)
        axes[0, 1].plot(self.df['Attendance'], p(self.df['Attendance']), 
                       color='red', linewidth=2, label='Trend')
        axes[0, 1].set_xlabel('Attendance %', fontsize=11)
        axes[0, 1].set_ylabel('Average Grade', fontsize=11)
        axes[0, 1].set_title('Attendance vs Grade', fontweight='bold')
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].legend()
        
        # 3. Sleep vs Grade
        axes[0, 2].scatter(self.df['Sleep_Hours'], self.df['Average_Grade'], 
                          alpha=0.6, c='orange')
        axes[0, 2].set_xlabel('Sleep Hours', fontsize=11)
        axes[0, 2].set_ylabel('Average Grade', fontsize=11)
        axes[0, 2].set_title('Sleep vs Grade', fontweight='bold')
        axes[0, 2].grid(True, alpha=0.3)
        
        # 4. Boxplot - Gender vs Grade
        data = [self.df[self.df['Gender'] == 'Male']['Average_Grade'],
                self.df[self.df['Gender'] == 'Female']['Average_Grade']]
        axes[1, 0].boxplot(data, tick_labels=['Male', 'Female'], patch_artist=True)
        axes[1, 0].set_ylabel('Average Grade', fontsize=11)
        axes[1, 0].set_title('Gender vs Grade', fontweight='bold')
        axes[1, 0].grid(True, alpha=0.3, axis='y')
        
        # 5. Boxplot - Extracurricular vs Grade
        data = [self.df[self.df['Extracurricular'] == 'No']['Average_Grade'],
                self.df[self.df['Extracurricular'] == 'Yes']['Average_Grade']]
        axes[1, 1].boxplot(data, tick_labels=['No', 'Yes'], patch_artist=True)
        axes[1, 1].set_ylabel('Average Grade', fontsize=11)
        axes[1, 1].set_title('Extracurricular vs Grade', fontweight='bold')
        axes[1, 1].grid(True, alpha=0.3, axis='y')
        
        # 6. Family Income vs Grade
        income_groups = self.df.groupby('Family_Income')['Average_Grade'].mean()
        axes[1, 2].bar(income_groups.index, income_groups.values, color='purple', alpha=0.7)
        axes[1, 2].set_xlabel('Family Income', fontsize=11)
        axes[1, 2].set_ylabel('Average Grade', fontsize=11)
        axes[1, 2].set_title('Family Income vs Grade', fontweight='bold')
        axes[1, 2].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        self.save_figure('04_key_relationships.png', fig)
        
        # Print key findings
        print("\n🔍 Key Findings from Bivariate Analysis:")
        
        # Study hours correlation
        corr = self.df['Study_Hours'].corr(self.df['Average_Grade'])
        print(f"  - Study Hours vs Grade correlation: {corr:.3f} ({'Strong' if abs(corr)>0.5 else 'Moderate' if abs(corr)>0.3 else 'Weak'})")
        
        # Attendance correlation
        corr = self.df['Attendance'].corr(self.df['Average_Grade'])
        print(f"  - Attendance vs Grade correlation: {corr:.3f} ({'Strong' if abs(corr)>0.5 else 'Moderate' if abs(corr)>0.3 else 'Weak'})")
        
        # Gender difference
        male_avg = self.df[self.df['Gender'] == 'Male']['Average_Grade'].mean()
        female_avg = self.df[self.df['Gender'] == 'Female']['Average_Grade'].mean()
        print(f"  - Female students perform {'better' if female_avg > male_avg else 'worse'} ({female_avg:.1f} vs {male_avg:.1f})")
        
        # Extracurricular difference
        ex_avg = self.df[self.df['Extracurricular'] == 'Yes']['Average_Grade'].mean()
        no_ex_avg = self.df[self.df['Extracurricular'] == 'No']['Average_Grade'].mean()
        print(f"  - Students with extracurriculars: {ex_avg:.1f} vs without: {no_ex_avg:.1f}")
        
        # Income effect
        high_income = self.df[self.df['Family_Income'] == 'High']['Average_Grade'].mean()
        low_income = self.df[self.df['Family_Income'] == 'Low']['Average_Grade'].mean()
        print(f"  - High-income students: {high_income:.1f} vs Low-income: {low_income:.1f}")
    
    def multivariate_analysis(self):
        """5. Multivariate Analysis (multiple variables)"""
        print("\n" + "="*60)
        print("📊 MULTIVARIATE ANALYSIS")
        print("="*60)
        
        # Create performance segments
        self.df['Performance_Segment'] = pd.cut(self.df['Average_Grade'],
                                                bins=[0, 70, 80, 100],
                                                labels=['Needs Improvement', 'Average', 'Excellent'])
        
        # Segment analysis
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Performance Segment Analysis', fontsize=16, fontweight='bold')
        
        # 1. Study Hours by Performance
        self.df.boxplot(column='Study_Hours', by='Performance_Segment', ax=axes[0, 0])
        axes[0, 0].set_title('Study Hours by Performance')
        axes[0, 0].set_ylabel('Study Hours')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Attendance by Performance
        self.df.boxplot(column='Attendance', by='Performance_Segment', ax=axes[0, 1])
        axes[0, 1].set_title('Attendance by Performance')
        axes[0, 1].set_ylabel('Attendance %')
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Sleep Hours by Performance
        self.df.boxplot(column='Sleep_Hours', by='Performance_Segment', ax=axes[1, 0])
        axes[1, 0].set_title('Sleep Hours by Performance')
        axes[1, 0].set_ylabel('Sleep Hours')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Multiple factors comparison
        segment_stats = self.df.groupby('Performance_Segment').agg({
            'Study_Hours': 'mean',
            'Attendance': 'mean',
            'Sleep_Hours': 'mean',
            'Previous_GPA': 'mean'
        }).round(2)
        
        axes[1, 1].axis('off')
        axes[1, 1].table(cellText=segment_stats.values,
                        rowLabels=segment_stats.index,
                        colLabels=segment_stats.columns,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.15, 0.15, 0.15, 0.15])
        axes[1, 1].set_title('Segment Statistics', fontweight='bold')
        
        plt.tight_layout()
        self.save_figure('05_performance_segments.png')
        
        print("\n🔍 Key Findings from Multivariate Analysis:")
        print("\nPerformance Segment Profiles:")
        for segment in ['Needs Improvement', 'Average', 'Excellent']:
            segment_data = self.df[self.df['Performance_Segment'] == segment]
            print(f"\n  {segment}:")
            print(f"    Study Hours: {segment_data['Study_Hours'].mean():.1f}")
            print(f"    Attendance: {segment_data['Attendance'].mean():.1f}%")
            print(f"    Sleep Hours: {segment_data['Sleep_Hours'].mean():.1f}")
            print(f"    Previous GPA: {segment_data['Previous_GPA'].mean():.2f}")
            print(f"    Students: {len(segment_data)}")
    
    def outlier_detection(self):
        """6. Outlier Detection"""
        print("\n" + "="*60)
        print("📊 OUTLIER DETECTION")
        print("="*60)
        
        numeric_cols = ['Study_Hours', 'Attendance', 'Sleep_Hours', 'Average_Grade']
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Outlier Detection - Boxplots', fontsize=16, fontweight='bold')
        
        for i, col in enumerate(numeric_cols):
            row = i // 2
            col_pos = i % 2
            axes[row, col_pos].boxplot(self.df[col], patch_artist=True)
            axes[row, col_pos].set_title(col, fontweight='bold')
            axes[row, col_pos].set_ylabel(col)
            axes[row, col_pos].grid(True, alpha=0.3, axis='y')
            
            # Detect outliers using IQR
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = self.df[(self.df[col] < Q1 - 1.5*IQR) | (self.df[col] > Q3 + 1.5*IQR)]
            
            if len(outliers) > 0:
                print(f"  {col}: {len(outliers)} outliers detected")
        
        plt.tight_layout()
        self.save_figure('06_outlier_boxplots.png')
    
    def create_dashboard_report(self):
        """Create a single combined dashboard with all major chart types."""
        fig = plt.figure(figsize=(18, 12), constrained_layout=True)
        fig.suptitle('Student Performance EDA Dashboard', fontsize=20, fontweight='bold', y=0.98)

        gs = fig.add_gridspec(2, 3)

        # Histogram panel
        ax1 = fig.add_subplot(gs[0, 0])
        self.df['Average_Grade'].hist(bins=15, color='skyblue', edgecolor='black', ax=ax1)
        ax1.axvline(self.df['Average_Grade'].mean(), color='red', linestyle='--', label=f'Mean: {self.df["Average_Grade"].mean():.1f}')
        ax1.set_title('Grade Distribution')
        ax1.set_xlabel('Average Grade')
        ax1.set_ylabel('Frequency')
        ax1.legend()

        # Box plot panel
        ax2 = fig.add_subplot(gs[0, 1])
        grades_by_gender = [self.df[self.df['Gender'] == 'Male']['Average_Grade'],
                            self.df[self.df['Gender'] == 'Female']['Average_Grade']]
        ax2.boxplot(grades_by_gender, patch_artist=True, tick_labels=['Male', 'Female'])
        ax2.set_title('Average Grade by Gender')
        ax2.set_ylabel('Average Grade')

        # Scatter plot panel
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.scatter(self.df['Study_Hours'], self.df['Average_Grade'], alpha=0.6, c='blue')
        z = np.polyfit(self.df['Study_Hours'], self.df['Average_Grade'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(self.df['Study_Hours'].min(), self.df['Study_Hours'].max(), 100)
        ax3.plot(x_line, p(x_line), color='red', linewidth=2, label='Trend')
        ax3.set_title('Study Hours vs Grade')
        ax3.set_xlabel('Study Hours')
        ax3.set_ylabel('Average Grade')
        ax3.grid(True, alpha=0.3)
        ax3.legend()

        # Correlation heatmap panel
        ax4 = fig.add_subplot(gs[1, 0])
        corr = self.df.select_dtypes(include=[np.number]).corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f', linewidths=0.5, ax=ax4)
        ax4.set_title('Correlation Heatmap')

        # Bar chart panel
        ax5 = fig.add_subplot(gs[1, 1])
        income_groups = self.df.groupby('Family_Income')['Average_Grade'].mean()
        ax5.bar(income_groups.index, income_groups.values, color='purple', alpha=0.7)
        ax5.set_title('Average Grade by Family Income')
        ax5.set_xlabel('Family Income')
        ax5.set_ylabel('Average Grade')
        ax5.grid(True, alpha=0.3, axis='y')

        # Performance category panel
        ax6 = fig.add_subplot(gs[1, 2])
        performance_counts = self.df['Performance'].value_counts().sort_index()
        ax6.bar(performance_counts.index.astype(str), performance_counts.values, color='lightcoral', edgecolor='black')
        ax6.set_title('Performance Distribution')
        ax6.set_xlabel('Performance')
        ax6.set_ylabel('Students')
        ax6.grid(True, alpha=0.3, axis='y')

        fig.subplots_adjust(top=0.92, bottom=0.08, left=0.06, right=0.98, hspace=0.35, wspace=0.25)
        self.save_figure('dashboard_report.png', fig)
        print(f"\n📊 Dashboard saved to: {self.output_dir / 'dashboard_report.png'}")

    def generate_insights(self):
        """7. Generate Full Insights Report"""
        print("\n" + "="*60)
        print("📊 COMPLETE INSIGHTS REPORT")
        print("="*60)
        
        print("\n🎯 OVERALL PERFORMANCE:")
        print(f"  - Total Students: {len(self.df)}")
        print(f"  - Average Grade: {self.df['Average_Grade'].mean():.2f}")
        print(f"  - Pass Rate (>60%): {len(self.df[self.df['Average_Grade'] > 60])/len(self.df)*100:.1f}%")
        print(f"  - Excellent Students (>80%): {len(self.df[self.df['Average_Grade'] > 80])}")
        
        print("\n📚 STUDY HABITS INSIGHTS:")
        print(f"  - Average Study Hours: {self.df['Study_Hours'].mean():.1f} hrs/week")
        print(f"  - Students studying >10 hrs: {len(self.df[self.df['Study_Hours'] > 10])}")
        print(f"  - Students studying <5 hrs: {len(self.df[self.df['Study_Hours'] < 5])}")
        print(f"  - Study Hours vs Grade Correlation: {self.df['Study_Hours'].corr(self.df['Average_Grade']):.3f}")
        
        print("\n🏫 ATTENDANCE INSIGHTS:")
        print(f"  - Average Attendance: {self.df['Attendance'].mean():.1f}%")
        print(f"  - Students with >90% attendance: {len(self.df[self.df['Attendance'] > 90])}")
        print(f"  - Students with <75% attendance: {len(self.df[self.df['Attendance'] < 75])}")
        print(f"  - Attendance vs Grade Correlation: {self.df['Attendance'].corr(self.df['Average_Grade']):.3f}")
        
        print("\n👥 DEMOGRAPHIC INSIGHTS:")
        print(f"  - Gender Distribution: {self.df['Gender'].value_counts().to_dict()}")
        print(f"  - Average Grade by Gender:")
        for gender in self.df['Gender'].unique():
            avg = self.df[self.df['Gender'] == gender]['Average_Grade'].mean()
            print(f"    {gender}: {avg:.2f}")
        
        print("\n🏆 TOP PERFORMERS PROFILE:")
        top_students = self.df.nlargest(5, 'Average_Grade')
        print(f"  - Study Hours: {top_students['Study_Hours'].mean():.1f}")
        print(f"  - Attendance: {top_students['Attendance'].mean():.1f}%")
        print(f"  - Extracurricular: {top_students['Extracurricular'].value_counts().to_dict()}")
        print(f"  - Family Income: {top_students['Family_Income'].value_counts().to_dict()}")
        
        print("\n💡 KEY RECOMMENDATIONS:")
        print("  1. Increase study hours for students below average")
        print("  2. Implement attendance improvement programs")
        print("  3. Provide extra support for students from low-income families")
        print("  4. Encourage participation in extracurricular activities")
        print("  5. Promote balanced sleep schedule (7-8 hours)")
    
    def run_full_eda(self):
        """Run complete EDA pipeline"""
        print("\n" + "="*60)
        print("📊 COMPLETE EXPLORATORY DATA ANALYSIS")
        print("="*60)
        
        # Create or load data
        choice = input("Create sample data or load from CSV? (S/L): ").upper()
        if choice == 'L':
            filename = input("Enter filename: ")
            self.load_data(filename)
        else:
            self.create_dataset()
        
        if self.df is None:
            print("❌ No data available!")
            return
        
        # Run all analyses
        self.data_overview()
        self.descriptive_statistics()
        self.univariate_analysis()
        self.bivariate_analysis()
        self.multivariate_analysis()
        self.outlier_detection()
        self.generate_insights()
        self.create_dashboard_report()
        
        print(f"\n✅ EDA Complete! Full insights generated. Visualizations saved to: {self.output_dir}")


# ========================================
# RUN THE EDA
# ========================================

if __name__ == "__main__":
    eda = StudentEDA()
    eda.run_full_eda()