# Multi sensor range comparison
# Applyong radar specific safety margins using broadcasting

import numpy as np
radar_range=np.array([
                      [1.5,3.4,5.6],
                      [3,5,7],
                      [4.5,4.8,1.4],
                      [1.3,4.4,1.6],
                      [5,3,9],
                      [4.2,7.8,5.4],
                      [1.6,4.1,1.0],
                      [8,1,4],
                      [7.2,3.8,8.4]
                    ])
safety_margin=np.array([1,1.5,0.5])
adjusted_range=radar_range-safety_margin
print(adjusted_range)