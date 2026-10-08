

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line == "":
            continue
    return records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for record in records:
        city = record[city]
        temperature = record[temperature]

        total[city] = total.get(city, 0) + temperature
        count[city] = count.get(city, 0) + 1

    averages = {}

    for city in total:
        averages[city] = round(total[city] / count[city], 1)

    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    return max(averages)