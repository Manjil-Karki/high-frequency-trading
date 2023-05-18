import asyncio
from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import numpy as np
from datetime import datetime


def make_buy_request(investment_factor):
    print('Buy')
    current_timestamp = datetime.now()
    print("update content in database with current time stamp")
    

def make_sell_request(profit_factor):
    print('Sell')
    current_timestamp = datetime.now()
    print("update content in database with current time stamp")
   


def process_message(data):
    strength_threshold = 0.2
    supply = np.array(data['a'], dtype=np.float32)
    demand = np.array(data['b'], dtype=np.float32)
    if supply.shape[0] == 0:
        total_supply = 0
    else:
        total_supply = np.sum(np.prod(supply, axis=1))
    if demand.shape[0] == 0:
        total_demand = 0
    else:
        total_demand = np.sum(np.prod(demand, axis=1))
    supply_strength = total_supply/(total_supply+total_demand)
    demand_strength = total_demand/(total_demand+total_supply)
    print(supply_strength, demand_strength)
    if supply_strength > demand_strength + strength_threshold:
        make_buy_request(supply_strength - demand_strength)
    elif demand_strength > supply_strength + strength_threshold:
        make_sell_request(demand_strength - supply_strength)
    else:
        print('No Action')


async def main():
    client = await AsyncClient.create()
    df = pd.DataFrame(columns=list('eEsUuba'))
    bm = BinanceSocketManager(client)
    ts = bm.depth_socket('BNBBTC')
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            df.loc[len(df)] = res
            process_message(res)

    await client.close_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())