def top_delayed_states(df):
    return (
        df.groupby('customer_state')['delay']
        .mean()
        .sort_values(ascending=False)
    )



def most_delayed_products(df):
    return (
        df.groupby('product_category_name')['delay']
        .mean()
        .sort_values(ascending=False)
    )


def delay_by_state_product(df):
    return (
        df.groupby(['customer_state', 'product_category_name'])['delay']
        .mean()
        .reset_index()
    )