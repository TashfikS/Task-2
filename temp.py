import pandas as pd

csv_file_path = 'sales_data_sample.csv'
sale_df = pd.read_csv(csv_file_path, encoding='latin-1')

csv_file_path = 'orders.csv.csv'
order_df = pd.read_csv(csv_file_path, encoding='latin-1')

selected_cols = ['ORDERNUMBER', 'ORDERDATE']
sale_df = sale_df[selected_cols]

merged_df = pd.merge(sale_df, order_df, left_on='ORDERNUMBER', right_on='order_id', how='inner')
cols_to_exclude = ['order_dow', 'order_hour_of_day', 'days_since_prior_order','order_id']
merged_df = merged_df.drop(cols_to_exclude, axis=1)


features = [item for item in merged_df.columns if item not in ['ORDERNUMBER', 'ORDERDATE']]

merged_df['ORDERDATE'] = pd.to_datetime(merged_df['ORDERDATE'])

target_month = 1
target_month_data = merged_df[merged_df['ORDERDATE'].dt.month == target_month]

monthly_totals = target_month_data.drop(['ORDERNUMBER', 'ORDERDATE'], axis=1).sum()

top_items = monthly_totals.nlargest(5)

print(top_items)