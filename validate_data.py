# validate_data.py
import sys
import pandas as pd

def run_validations():
    print("Loading Superstore Orders dataset for Pandas validation...")
    
    # Load the dataset
    file_path = "data/Sample - Superstore - Orders.csv"
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"\ERROR: File '{file_path}' not found.")
        sys.exit(1)

    errors = []

    # Check required columns exist
    required_cols = {
        "Row ID", "Order ID", "Order Date", "Customer ID", 
        "Segment", "Category", "Sales", "Quantity", "Discount", "Profit"
    }
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        errors.append(f"Missing required columns: {missing_cols}")

    # Check primary key is unique
    if "Row ID" in df.columns and df["Row ID"].duplicated().any():
        duplicate_count = df["Row ID"].duplicated().sum()
        errors.append(f"Found {duplicate_count} duplicate 'Row ID' values.")

    # Range and boundary checks
    if "Sales" in df.columns and (df["Sales"] <= 0).any():
        errors.append("Found non-positive values in 'Sales' column.")

    if "Quantity" in df.columns and (df["Quantity"] < 1).any():
        errors.append("Found 'Quantity' values less than 1.")

    if "Discount" in df.columns and not df["Discount"].between(0.0, 1.0).all():
        errors.append("Found 'Discount' values outside the valid range [0.0, 1.0].")

    # Check allowed categorical values
    valid_segments = {"Consumer", "Corporate", "Home Office"}
    if "Segment" in df.columns:
        invalid_segments = set(df["Segment"].unique()) - valid_segments
        if invalid_segments:
            errors.append(f"Found invalid values in 'Segment': {invalid_segments}")

    valid_categories = {"Furniture", "Office Supplies", "Technology"}
    if "Category" in df.columns:
        invalid_categories = set(df["Category"].unique()) - valid_categories
        if invalid_categories:
            errors.append(f"Found invalid values in 'Category': {invalid_categories}")

    # Evaluate and output results
    if errors:
        print("\nDATA VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)  # Exit code 1 flags a failure in GitHub Actions
    else:
        print("\nALL SUPERSTORE DATA CHECKS PASSED SUCCESSFULLY!")
        sys.exit(0)  # Exit code 0 signals success

if __name__ == "__main__":
    run_validations()