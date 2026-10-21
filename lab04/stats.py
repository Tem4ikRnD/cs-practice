def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное количество полей")
    city, temp, date = parts
    if city == "" or date == "":
        raise ValueError("Город или дата не указаны")
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")
    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        temperature = record["temperature"]
        total[city] = total.get(city, 0) + temperature
        count[city] = count.get(city, 0) + 1
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    return min(averages, key = lambda city: (-averages[city], city))