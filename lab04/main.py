import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

records = read_valid(lines)
averages = average_by_city(records)
valid_count = len(records)
empty_count = sum(1 for line in lines if line == "")
skipped_count = len(lines) - valid_count - empty_count

print(valid_count)
print(skipped_count)
if records:
    city = warmest_city(records)
    print(f"{averages[city]:.1f}")
else:
    print("0.0")