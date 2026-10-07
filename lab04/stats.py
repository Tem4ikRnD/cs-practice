# import sys

# lines = sys.stdin.read().splitlines()
# total = {}
# count = {}
# for line in lines:
#     city, temp, date = line.split(";")
#     total[city] = total.get(city, 0) + float(temp)
#     count[city] = count.get(city, 0) + 1
# best = ""
# for city in total:
#     if best == "" or total[city] / count[city] > total[best] / count[best]:
#         best = city
# print(len(lines))
# print(0)
# print(total[best] / count[best])


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
            record = parse_record(line)
            records.append(record)
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

    return max(averages, key=lambda city: (averages[city], -ord(city[0])))