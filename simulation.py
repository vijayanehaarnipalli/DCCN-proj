import random
import time
import pandas as pd

def simulate_transfer(topology, src, dst, csv_file="results.csv"):
    start_time = time.time()
    path = topology.shortest_path(src, dst)
    hops = len(path) - 1
    delay = random.uniform(10, 100) * hops   # ms
    throughput = round(random.uniform(50, 100) / hops, 2)  # Mbps
    packet_loss = round(random.uniform(0, 2) * hops, 2)    # %
    duration = time.time() - start_time

    data = {
        "src": src,
        "dst": dst,
        "path": "→".join(path),
        "delay_ms": delay,
        "throughput_mbps": throughput,
        "packet_loss_pct": packet_loss,
        "sim_time": round(duration, 3)
    }

    df = pd.DataFrame([data])
    df.to_csv(csv_file, mode="a", header=not pd.io.common.file_exists(csv_file), index=False)

    return data
