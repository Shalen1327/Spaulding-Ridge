import streamlit as st
import pandas as pd
import pyodbc
import sys 

# SQL Server connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-0F9OCUO;"  # Use your instance name if different
    "DATABASE=SR;"           # Change to your actual database name
    "Trusted_Connection=yes;" 
)

# Load data from your table
df = pd.read_sql("SELECT * FROM [Employee Data]", conn)

df["Active"] = df["Active?"] == "Y"

# Sidebar filters
st.sidebar.header("Filter Employees")
selected_role = st.sidebar.selectbox("Select Role", ["All"] + sorted(df["Role"].unique()))
selected_location = st.sidebar.selectbox("Select Location", ["All"] + sorted(df["Location"].unique()))
show_inactive = st.sidebar.checkbox("Include Inactive Employees", value=True)

# Apply filters
filtered_df = df.copy()
if selected_role != "All":
    filtered_df = filtered_df[filtered_df["Role"] == selected_role]
if selected_location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]
if not show_inactive:
    filtered_df = filtered_df[filtered_df["Active"]]

# View filtered data
st.title("Employee Dashboard")
st.dataframe(filtered_df[["Name", "Role", "Location", "Current Comp (INR)"]])

# Avg compensation
if selected_location != "All":
    avg = filtered_df["Current Comp (INR)"].mean()
    st.metric(label=f"Average Compensation in {selected_location}", value=f"₹{avg:,.0f}")

# Compensation by location
st.subheader("Average Compensation by Location")
st.bar_chart(filtered_df.groupby("Location")["Current Comp (INR)"].mean())

# Experience breakdown
st.subheader("Employees by Experience Range")
st.bar_chart(filtered_df["Years of Experience"].value_counts().sort_index())

# Variable increment
st.subheader("Simulate Compensation Increment")
increment = st.slider("Select Global % Increment", 0, 100, 10)
filtered_df["Incremented Compensation"] = filtered_df["Current Comp (INR)"] * (1 + increment / 100)
st.dataframe(filtered_df[["Name", "Current Comp (INR)", "Incremented Compensation"]])
st.success(f"Total Updated Compensation: ₹{filtered_df['Incremented Compensation'].sum():,.0f}")


# Export CSV
st.download_button("Download CSV", filtered_df.to_csv(index=False), file_name="filtered_employees.csv")


