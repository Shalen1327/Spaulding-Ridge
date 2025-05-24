# Employee Compensation Dashboard

This is a Streamlit-powered dashboard that connects to a Microsoft SQL Server database and allows users to:
- Filter employees by role, location, and active status
- View compensation statistics and bar charts
- Simulate salary increments using a slider
- Download filtered employee data to CSV

---

##  Requirements

- Windows 10 or 11
- Python 3.9+
- Microsoft SQL Server (Express or Standard)
- SQL Server Management Studio (SSMS)
- ODBC Driver for SQL Server (v17 or above)

---

##  Project Structure


---

##  Step-by-Step Installation

### 1. Install SQL Server and SSMS

- [Download SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [Download SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)

### 2. Restore the `.bak` File

1. Open **SQL Server Management Studio**
2. Connect to `localhost\SQLEXPRESS` (or your instance name)
3. Right-click `Databases` → `Restore Database`
4. Choose **Device** → Browse → Select `SR.bak`
5. Restore it and name your database: `SR`

---

##  3. Set Up Python Environment

### Install required packages:

```bash
pip install streamlit pandas pyodbc openpyxl
Note - If you don’t have Python, download it from: https://www.python.org/downloads/
make sure that the following section in correctly configured 
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"  # or your instance name
    "DATABASE=EmployeeDB;"           # your restored database name
    "Trusted_Connection=yes;"        # for Windows Authentication
)

Ensure the table name matches just in case - df = pd.read_sql("SELECT * FROM [Employee Data]", conn)
open the terminal ensure the file loacation and use this command to run
streamlit run app.py


