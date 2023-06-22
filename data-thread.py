import pandas as pd
import threading
import time

start = time.time()


def low_rank():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    low_rank = df.loc[df['Rank'].idxmax()]
    print(low_rank)


def high_rank():
    df = pd.read_csv('./video-game-sales.csv')
    df = df.dropna()
    low_sales = df.loc[df['Rank'].idxmin()]
    print(low_sales)


t1 = threading.Thread(target=low_rank)
t2 = threading.Thread(target=high_rank)

t1.start()
t2.start()

t1.join()
print(26 * "*")
t2.join()
end = time.time()
print(end - start)
