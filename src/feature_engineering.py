import pandas as pd

def calculate_delay(df):
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    
    df['delay'] = (
        df['order_delivered_customer_date'] - 
        df['order_estimated_delivery_date']
    ).dt.days
    
    
    return df


def apply_sla(df):
    df['apply_SLA'] = df['delay'] <= 0
    return df