import json

def csv_to_records(text: str) -> list[dict]:
    lines = text.splitlines()
    if not lines:
        return []
    headers = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if line == "":
            continue
        values = line.split(",")
        record = {}
        for i in range(len(headers)):
            record[headers[i]] = values[i]
        records.append(record)
    return records

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None
    for line in lines:
        line = line.split("#")[0].strip()
        if line == "":
            continue
        if line.startswith("- "):
            if current_list is not None:
                value = line[2:].strip()
                settings[current_list].append(value)
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            settings[key] = []
            current_list = key
            continue
        current_list = None
        if value == "true" or value == "yes":
            value = True
        elif value == "false" or value == "no":
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        settings[key] = value
    return settings

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        record = {}
        if row.get(key) in extra:
            record.update(extra[row[key]])
        record.update(row)
        result.append(record)
    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii = False, indent = 2, sort_keys = True)