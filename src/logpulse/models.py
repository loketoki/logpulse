from dataclasses import dataclass

@dataclass
class LogEntry:
    ip: str
    timestamp: str
    method: str
    path: str
    status_code: int
    response_size: int
