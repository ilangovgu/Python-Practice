import numpy as np

# =========================================================
# 1. Radar detections: [x, y, relative_speed]


radar_data = np.array([
    [12,  3.2, -2],
    [-4,  3.0, -5],
    [ 6, -3.5,  1],
    [20,  0.5,  0],
    [-10, 2.8, -1]
], dtype=float)

x = radar_data[:, 0]
y = radar_data[:, 1]
relative_speed = radar_data[:, 2]

# =========================================================
# 2. Define Blind Spot Zone (Left Side)
# =========================================================

blind_spot_mask = (
    (x > -8) & (x < 2) &
    (y > 2) & (y < 4) &
    (relative_speed < 0)
)

# =========================================================
# 3. Decision
# =========================================================

if np.any(blind_spot_mask):
    print("⚠️ Blind Spot Warning: Vehicle detected in left blind zone!")
    print("Threat vehicles:")
    print(radar_data[blind_spot_mask])
else:
    print("No vehicle in blind spot.")