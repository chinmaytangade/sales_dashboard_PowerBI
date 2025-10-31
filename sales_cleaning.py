# -----------------------------------------------
# Store Sales Dataset - Data Cleaning Project
# By Chinmay Tangade.
# -----------------------------------------------

import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("SuperStoreOrders.csv")
print("✅ Dataset loaded successfully!")
print("Initial shape:", df.shape)
print("-" * 50)

# Step 2: Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())
print("-" * 50)

# Step 3: Handle missing values
fill_cols = ['Customer Name', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'Sub-Category']
for col in fill_cols:
    if col in df.columns:
        df[col].fillna('Unknown', inplace=True)

# Numerical columns
num_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
for col in num_cols:
    if col in df.columns:
        df[col].fillna(0, inplace=True)

# Step 4: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Convert dates
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
if 'ship_date' in df.columns:
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

# Step 7: Verify data types
print("Data types after cleaning:")
print(df.dtypes)
print("-" * 50)

# Step 8: Check for duplicates and nulls again
print("Duplicates remaining:", df.duplicated().sum())
print("Missing values after cleaning:")
print(df.isnull().sum())
print("-" * 50)

# Step 9: Save cleaned dataset
df.to_csv("store_sales_cleaned.csv", index=False)
print("✅ Cleaned dataset saved successfully as 'store_sales_cleaned.csv'")
print("Final shape:", df.shape)