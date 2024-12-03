import pandas as pd
from datetime import datetime, timedelta
import random

# Generate sample data
data = {
    "latitude": [random.uniform(8, 37) for _ in range(100)],
    "longitude": [random.uniform(68, 97) for _ in range(100)],
    "time": [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(100)],
    "weather": random.choices(["Clear", "Rainy", "Foggy", "Snowy"], k=100),
    "road_condition": random.choices(["Dry", "Wet", "Slippery"], k=100),
    "severity": random.choices([1, 2, 3, 4, 5], k=100)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("traffic_accidents.csv", index=False)
print("Sample CSV file 'traffic_accidents.csv' created successfully.")
