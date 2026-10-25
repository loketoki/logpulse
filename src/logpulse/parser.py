import re
from logpulse.models import LogEntry

LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[0-9.]+" (?P<status>\d+) (?P<size>\d+)'
)

def parse_line(line: str) -> LogEntry | None:
    match = LOG_PATTERN.match(line.strip())
    if not match:
        print(f"Impossibile analizzare la riga: {repr(line.strip())}")
        return None

    data = match.groupdict()
    return LogEntry(
        ip= data["ip"],
        timestamp= data["timestamp"],
        method= data["method"],
        path= data["path"],
        status_code= int(data["status"]),
        response_size= int(data["size"])
    )

def parse_file(file_path: str):
    entries = []
    with open(file_path, 'r') as file:
        for line in file:
            entry = parse_line(line)
            if entry:
                entries.append(entry)
    return entries
