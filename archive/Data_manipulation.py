import pandas as pd
df = pd.read_excel('OrderHistory.xlsx')
# Sorting in the excel by column values
df = df.sort_values('Order ID',ascending=True)
print(df.head(10))

agg_dict = {
    'Sales Amount' : 'sum',
    'Order Type'   : ','.join,
}
# groupy functions in excel sheet
manipulated_df = df.groupby('Order ID').agg(agg_dict)

manipulated_df.to_excel('simplified_order_history.xlsx')

print(manipulated_df[manipulated_df['Order Type'].str.contains(',')])