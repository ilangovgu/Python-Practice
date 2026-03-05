import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv("av_sensor_log.csv")

# Aggregation
counts = df.groupby(["vehicle_id", "event"]).size().unstack(fill_value=0)
ax = counts.plot(kind="bar", stacked=True, figsize=(12, 6))

plt.xlabel("Vehicle_id")
plt.ylabel("Event Count")
plt.title("Bar chart - Vehicle Events")
plt.legend(title="Event")
plt.tight_layout()

plt.show() 