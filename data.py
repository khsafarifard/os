import pandas as pd
import time

start = time.time()


def low_rank():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    top_sales = df.loc[df['Rank'].idxmax()]
    print(top_sales)


def high_rank():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    low_sales = df.loc[df['Rank'].idxmin()]
    print(low_sales)


high_rank()
print(26 * "*")
low_rank()
end = time.time()
print(end - start)
