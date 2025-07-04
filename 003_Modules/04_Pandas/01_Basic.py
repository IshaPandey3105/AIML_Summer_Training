# 📌 Pandas Theory Notes 🐼✨

# 1️⃣ What is Pandas?
# ➔ Pandas is a popular Python library used for data manipulation, analysis, and handling.
# ➔ It helps to work with structured data like tables (rows and columns) easily.

# 2️⃣ Key Data Structures in Pandas:
# ➔ Series → 1-dimensional data (like a single column).
# ➔ DataFrame → 2-dimensional data (like a full table).

# 3️⃣ Why Use Pandas?
# ➔ Easy data reading (CSV, Excel, SQL, JSON).
# ➔ Fast filtering, sorting, and grouping.
# ➔ Built-in functions for stats, cleaning, and reshaping data.

# 4️⃣ Common Pandas Functions:
# ➔ pd.read_csv() → To read data from CSV files.
# ➔ pd.DataFrame() → To create a table from a dictionary or list.
# ➔ df.head() → Shows top 5 rows.
# ➔ df.tail() → Shows last 5 rows.
# ➔ df.info() → Gives structure and data types.
# ➔ df.describe() → Statistical summary (mean, count, std).

# 5️⃣ Data Selection in Pandas:
# ➔ df['ColumnName'] → Select a single column.
# ➔ df[['Col1', 'Col2']] → Select multiple columns.
# ➔ df.loc[row_label] → Select row by label.
# ➔ df.iloc[row_index] → Select row by position.

# 6️⃣ Data Filtering:
# ➔ df[df['Column'] > value] → Filter rows based on condition.

# 7️⃣ Adding & Deleting Data:
# ➔ df['NewColumn'] = values → Add new column.
# ➔ df.drop('ColumnName', axis=1) → Delete column.
# ➔ df.drop(index, axis=0) → Delete row.

# 8️⃣ Sorting & Grouping:
# ➔ df.sort_values(by='Column', ascending=True/False)
# ➔ df.groupby('ColumnName')['AnotherColumn'].mean()

# 9️⃣ Handling Missing Values:
# ➔ df.isnull() → Check for missing values.
# ➔ df.fillna(value) → Fill missing data.
# ➔ df.dropna() → Remove missing data.

# 🔟 Saving and Loading Data:
# ➔ df.to_csv('filename.csv', index=False) → Save to CSV.
# ➔ pd.read_csv('filename.csv') → Load from CSV.

# ✅ Summary:
# ➔ Pandas = Fast, simple, powerful tool for data analysis.
# ➔ Very useful for Machine Learning, Data Science, and Reports.
