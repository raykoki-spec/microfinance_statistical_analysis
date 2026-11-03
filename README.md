# File: README.md

# Mombasa Microfinance Loan Statistical Analysis
This script generates statistical analysis for 150 fictional loan records of a Mombasa
microfinance institute. Plots and saves a histogram chart showing loan amounts in relation to number of loans.

## What It Does

- Creates 150 fictional loan records
- Applies logic to create full statistical summary(mean, mode, midian, minimum, maximum)
- Identifies and prints the outliers(loan_id, amount)
- Applies logic to calculate correlation between loan amount and days to repayment
- Plots a histogram of loan amounts
- Saves the histogram as PNG(msa_microfinance_analysis.png)

## Correlation Findings
A value of -0.06 indicates that there is no correlation between loan amount and days to repayment

## Setup

```bash
pip install -r requirements.txt
```

## Usage
Run the program from the project's folder

```
python msa_microfinance_analysis.py
```

## How it Works
First, fictional loan record is generated. Running a full statistical summary comes second. Next, identification of outliers alongside with correlation between loan amounts and days to repayment.

```python
loan_data = pd.DataFrame({
    "loan_id": loan_ids,
    "amount_kes": amount_kes,
    "days_to_first_repayment": days_to_first_repayment,
    "county": county
})

print(loan_data.describe())

outliers = loan_data[(loan_data["amount_kes"] < lower) | (loan_data["amount_kes"] > upper)]


corr = loan_data["amount_kes"].corr(loan_data["days_to_first_repayment"])
print(f"Correlation: {corr:.2f}")
```

## Sample Output

```
=========MOMBASA MICROFINANCE LOAN STATISTICAL ANALYSIS=========
          loan_id     amount_kes  days_to_first_repayment
count  150.000000     150.000000               150.000000
mean    75.500000  161607.333333                99.593333
std     43.445368  138501.627009                 1.043334
min      1.000000   16000.000000                96.000000
25%     38.250000   76100.000000                99.000000
50%     75.500000  124500.000000               100.000000
75%    112.750000  192525.000000               100.000000
max    150.000000  932700.000000               103.000000
----------------------------------------------------------------
```

## Stack
Python, Pandas, Numpy, Matplotlib, Scipy

