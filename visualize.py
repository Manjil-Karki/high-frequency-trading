from datetime import datetime, time
from binance.client import Client
import pandas as pd


def get_starting_point(start_time):
    # Todo

    #convert time to timestamp
    #from database query records after given timestamp
    #corresponding data
    pass

def visualize_trading_history(df, trade_df):
    # todo
    #use matplotlib and other tools to visualize the performance
    pass

if __name__ == "__main__":
    current_date = datetime.now().date()
    midnight_time = time(0, 0, 0)
    # mid night timestamp
    start_time = datetime.combine(current_date, midnight_time)
    client = Client()
    df = get_starting_point(start_time=start_time)
    trades = client.get_historical_klines('BNBBTC',interval = '1m', start_str= start_time, end_str=datetime.now())
    trade_df = pd.DateFrame(trades)
    visualize_trading_history(df, trade_df)
