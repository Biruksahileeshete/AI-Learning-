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