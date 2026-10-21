from pathlib import Path
from logstats import count_levels, top_errors, format_report

def main():
    filename = input().strip()
    script_dir = Path(__file__).resolve().parent
    log_path = Path(filename)
    if not log_path.is_absolute():
        log_path = Path.cwd() / log_path
    
    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)
    total = sum(counts.values())

    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)
    
    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    report_path = script_dir / "report.txt"
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

if __name__ == "__main__":
    main()