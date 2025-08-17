# Personal Finance Tracker

Cloud-based Personal Finance Tracker using Python, SQL, and AWS.

## Features
- Upload CSV of expenses to AWS S3
- ETL pipeline with Python
- Store processed data in AWS RDS (MySQL)
- SQL analytics: spending by category, monthly trends, top expenses
- Streamlit dashboard for visualization

## Tech Stack
- Python (Pandas, SQLAlchemy, Streamlit, Matplotlib, Seaborn)
- SQL (MySQL)
- AWS (S3, RDS)

## Usage
1. Set up AWS S3 bucket and upload `expenses.csv`
2. Set up AWS RDS (MySQL) and run `schema.sql` to create table
3. Update credentials in `finance_etl.py` and `app.py`
4. Run ETL script: `python finance_etl.py`
5. Run Streamlit dashboard: `streamlit run app.py`
