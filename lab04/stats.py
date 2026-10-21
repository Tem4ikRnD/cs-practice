def parse_record(line: str) -> dict:
    flag = False
    parts = line.split(";")
    if len(parts) != 3:
<<<<<<< HEAD
        raise ValueError("Неверное количество полей")
=======
        flag = True
        raise ValueError("Неверный формат ввода")

>>>>>>> ec76ed28be29ab8f5f4734c4b2a0eaca963ddf6d
    city, temp, date = parts
    if city == "" or date == "":
        flag = True
        raise ValueError("Город или дата не указаны")
<<<<<<< HEAD
    try:
=======

    if float(temp):
>>>>>>> ec76ed28be29ab8f5f4734c4b2a0eaca963ddf6d
        temperature = float(temp)
    else:
        flag = True
        raise ValueError("Температура должна быть числом")
<<<<<<< HEAD
    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }
=======

    return city, temperature, date, flag
>>>>>>> ec76ed28be29ab8f5f4734c4b2a0eaca963ddf6d

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line == "" or parse_record(line)[3]:
            continue
<<<<<<< HEAD
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
=======
>>>>>>> ec76ed28be29ab8f5f4734c4b2a0eaca963ddf6d
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
<<<<<<< HEAD
    return min(
        averages,
        key = lambda city: (-averages[city], city)
    )
=======
    return max(averages)
>>>>>>> ec76ed28be29ab8f5f4734c4b2a0eaca963ddf6d
