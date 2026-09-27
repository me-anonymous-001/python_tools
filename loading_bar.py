from tqdm import tqdm
import time

def simulate_work(item):
    time.sleep(0.1)

# for item in tqdm(range(100), desc="Processing"):
#     simulate_work(item)

for i in tqdm(range(10), desc="Outer", position=0):
    for j in tqdm(range(100), desc="Inner", position=1):
        simulate_work(j)