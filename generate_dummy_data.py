import pandas as pd
import numpy as np

# Create 500 rows of dummy audit data
data = {
    "Transaction_ID": range(1001, 1501),
    "Account_Code": np.random.choice(['4010', '4020', '5010', '6010', '7010'], 500),
    "Description": np.random.choice(['Office Supplies', 'Consulting Fees', 'Software License', 'Travel', 'Payroll'], 500),
    "Debit": np.round(np.random.uniform(10, 5000, 500), 2),
    "Credit": np.round(np.random.uniform(10, 5000, 500), 2),
    "Date": pd.date_range(start='2025-01-01', periods=500, freq='D')
}

df = pd.DataFrame(data)
df.to_csv("mock_general_ledger.csv", index=False)
print("Mock ledger created successfully.")