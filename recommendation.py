import pandas as pd
import json

def get_recommendation(sale_df, order_df, month):

    selected_cols = ['ORDERNUMBER', 'ORDERDATE']
    sale_df = sale_df[selected_cols]

    merged_df = pd.merge(sale_df, order_df, left_on='ORDERNUMBER', right_on='order_id', how='inner')
    cols_to_exclude = ['order_dow', 'order_hour_of_day', 'days_since_prior_order','order_id']
    merged_df = merged_df.drop(cols_to_exclude, axis=1)

    merged_df['ORDERDATE'] = pd.to_datetime(merged_df['ORDERDATE'])

    target_month_data = merged_df[merged_df['ORDERDATE'].dt.month == month]

    monthly_totals = target_month_data.drop(['ORDERNUMBER', 'ORDERDATE'], axis=1).sum()

    top_items = monthly_totals.nlargest(5)
    result_dict = top_items.to_dict()
    result_json = json.dumps(result_dict)

    return result_json