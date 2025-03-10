import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 200
advertising = np.random.randint(1000, 10000, n_samples)
discount = np.random.randint(5, 50, n_samples)
stores = np.random.randint(1, 20, n_samples)

# Creating a non-linear relationship with interactions
sales = (
    5000 + 2.5 * advertising - 0.0001 * advertising**2 +
    100 * discount - 0.5 * discount**2 +
    50 * stores + 0.1 * stores**2 +
    0.05 * advertising * discount +
    0.02 * advertising * stores +
    np.random.normal(0, 500, n_samples)
)

data = pd.DataFrame({
    'Advertising': advertising,
    'Discount': discount,
    'Stores': stores,
    'Sales': sales
})

data.to_csv('complex_sales_data.csv', index=False)
print("Dataset generated and saved as'complex_sales_data.csv'.")
