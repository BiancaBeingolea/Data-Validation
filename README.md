# Superstore Automated Data Validation Pipeline

An automated data quality assurance pipeline built with **Python**, **Pandas**, and **GitHub Actions**. 

This repository demonstrates how to integrate automated data validation into a CI/CD workflow to test datasets and block invalid data before it reaches production.

You can read the accompanying blog here: 

---

## Repository Structure

```text
Data-Validation/
├── .github/
│   └── workflows/
│       └── data_validation.yml   # GitHub Actions CI/CD configuration
├── data/
│   └── Sample - Superstore - Orders.csv  # Target dataset
├── requirements.txt              # Dependencies (pandas)
├── validate_data.py              # Data quality check suite
└── README.md                     # Project documentation
