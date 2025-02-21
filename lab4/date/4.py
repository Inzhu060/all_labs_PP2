from datetime import datetime

d1 = datetime(2025, 2, 21, 3, 49, 0)
d2 = datetime(2025, 2, 21, 3, 12, 25)
difference = d1 - d2
print(difference.seconds)