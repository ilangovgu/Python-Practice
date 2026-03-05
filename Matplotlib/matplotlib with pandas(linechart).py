import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("av_sensor_log.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["minute"] = df["timestamp"].dt.minute
event_per_minute = df["minute"].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(event_per_minute.index,
         event_per_minute.values,
         marker="o",
         linestyle="-",
         linewidth=2)

plt.xlabel("minute(time order)")
plt.ylabel("number of events")
plt.title("sensor events vs minute")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()