# Student Performance EDA

This project performs an Exploratory Data Analysis (EDA) on a synthetic student performance dataset to uncover patterns, trends, and relationships between student behavior and academic outcomes.

## Overview

The analysis explores how factors such as study hours, attendance, sleep, previous GPA, family income, gender, and extracurricular activities relate to students' average grades and overall performance.

The project is implemented in Python using pandas, NumPy, seaborn, and matplotlib.

## Project Goals

- Understand the shape and quality of the dataset
- Identify trends in student performance
- Analyze relationships between academic and lifestyle factors
- Detect outliers and unusual patterns
- Generate clear visual summaries and reports
- Produce actionable insights for student improvement strategies

## Dataset

The project creates a sample student dataset with fields such as:

- Student_ID
- Age
- Gender
- Study_Hours
- Attendance
- Previous_GPA
- Sleep_Hours
- Extracurricular
- Part_Time_Job
- Family_Income
- Grade_Math
- Grade_English
- Grade_Science
- Average_Grade
- Performance

## Analysis Included

The script covers the following stages of EDA:

1. Data overview
2. Descriptive statistics
3. Univariate analysis
4. Bivariate analysis
5. Multivariate analysis
6. Outlier detection
7. Insight generation
8. Dashboard creation

## Visual Outputs

The project saves charts and reports in the `visualizations/` folder, including:

- Univariate numerical distribution plots
- Categorical variable bar charts
- Correlation heatmap
- Study hours vs grade plots
- Attendance vs grade plots
- Gender and extracurricular comparisons
- Performance segmentation charts
- Outlier detection boxplots
- Final dashboard report

## File Structure

```text
EDA Projects with Full Insights/
├── Readme.md
├── STUDENT PERFORMANCE EDA.py
├── visualizations/
│   ├── 01_univariate_numerical.png
│   ├── 02_univariate_categorical.png
│   ├── 03_correlation_heatmap.png
│   ├── 04_key_relationships.png
│   ├── 05_performance_segments.png
│   ├── 06_outlier_boxplots.png
│   ├── dashboard_report.png
└── ...
```

## Requirements

Install the required libraries before running the script:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

Open the project folder and run:

```bash
python "STUDENT PERFORMANCE EDA.py"
```

When prompted, choose one of the following:

- `S` to create a sample student dataset
- `L` to load an existing CSV file

## Example Insights from the Project

- Students with higher study hours tend to have better grades
- Attendance strongly correlates with academic performance
- Sleep and previous GPA also affect overall achievement
- Family income and extracurricular participation show noticeable differences in performance
- Students in high-performing groups typically display stronger study habits and attendance patterns

## Key Takeaway

This project demonstrates how exploratory data analysis can be used to convert raw educational data into meaningful insights that support better academic planning, student support, and data-driven decision-making.

## License

This project is intended for educational and learning purposes.
