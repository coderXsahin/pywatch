def parse_log_line(line):
    parts = line.strip().split(" | ", 3)
    if len(parts) != 4:
        return None
    timestamp, application, level, message = parts
    return {
        "timestamp": timestamp,
        "application": application,
        "level": level,
        "message": message
    }
def parse_log_file(file_path):
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed is not None:
                logs.append(parsed)
    return logs
