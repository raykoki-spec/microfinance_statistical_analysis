
"""
Mombasa Microfinance Loan-Statistical Analysis
----------------------------------------------
This script generates statistical analysis for 150 fictional loan records of a Mombasa
microfinance institute.

Plots and saves a histogram chart showing loan amounts.
Usage:
    python msa_microfinance_analysis.py

Config:
    Clip the loan amounts to a reasonable range and remove any negative values.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats

np.random.seed(42)  

loan_ids = range(1, 151)

amount_kes = np.random.lognormal(mean=np.log(130000), sigma=0.8, size=150).round(-2).astype(int)

amount_kes = np.clip(amount_kes, 1000, None).astype(int) 

days_to_first_repayment = np.random.normal(100, 1, 150).astype(int)

days_to_first_repayment = np.clip(days_to_first_repayment, 1, None).astype(int)  

county = np.random.choice(["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"], 150)

loan_data = pd.DataFrame({
    "loan_id": loan_ids,
    "amount_kes": amount_kes,
    "days_to_first_repayment": days_to_first_repayment,
    "county": county
})

print("=========MOMBASA MICROFINANCE LOAN STATISTICAL ANALYSIS=========")
print(loan_data.describe())
print("----------------------------------------------------------------")

Q1 = loan_data["amount_kes"].quantile(0.25)
Q3 = loan_data["amount_kes"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = loan_data[(loan_data["amount_kes"] < lower) | (loan_data["amount_kes"] > upper)]
print("=============OUTLIERS=============")
print(f"Number of Outliers: {len(outliers)}")
print(outliers[["loan_id", "amount_kes"]])
print("------------------------------------------------")

print("==============CORRELATION ANALYSIS==============")
corr = loan_data["amount_kes"].corr(loan_data["days_to_first_repayment"])
print(f"Correlation: {corr:.2f}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(loan_data["amount_kes"], bins=30, color='blue', edgecolor='white')
ax.axvline(loan_data["amount_kes"].mean(), color='gray', linestyle='--', linewidth=2, 
           label=f"Mean: KES {loan_data['amount_kes'].mean():.0f}")
ax.axvline(loan_data["amount_kes"].median(), color='green', linestyle='-', linewidth=2,
           label=f"Median: KES {loan_data['amount_kes'].median():.0f}")
ax.axvline(upper, color='red', linestyle=':', linewidth=2, 
           label=f"Outlier Upper Bound: KES {upper:.0f}")
ax.set_xlabel("Loan Amount (KES)")
ax.set_ylabel("Number of Loans")
ax.set_title("Distribution of Loan Amounts")
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,.0f}'))
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig("msa_microfinance_analysis.png", dpi=150)
