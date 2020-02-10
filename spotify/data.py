from glob import glob
import json
import pandas as pd

def read_history():
    
    files = sorted(glob("StreamingHistory*.json"))
    streaming_history = []
    for file in files:
        with open(file) as readable:
            streaming_history.extend(json.load(readable))
    streaming_history = pd.DataFrame(streaming_history)
    streaming_history["endTime"] = pd.to_datetime(streaming_history["endTime"])
    
    return streaming_history