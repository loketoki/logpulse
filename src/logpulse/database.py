import sqlite3
from logpulse.models import LogEntry


class DatabaseManager:
    def __init__(self, db_path: str = "logs.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS logs (
            ip TEXT,
            timestamp TEXT,
            method TEXT,
            path TEXT,
            status_code INTEGER,
            response_size INTEGER
            )
        """

        self.cursor.execute(query)
        self.conn.commit()


    def insertLog(self, log: LogEntry):
        query = """
    INSERT INTO logs(ip, timestamp, method, path, status_code, response_size) VALUES (?,?,?,?,?,?)
    """
        self.cursor.execute(
            query,
            (
                log.ip,
                log.timestamp,
                log.method,
                log.path,
                log.status_code,
                log.response_size,
            ),
        )
        self.conn.commit()


    def fetch_all_logs(self):
        self.cursor.execute("SELECT * FROM logs")
        rows = self.cursor.fetchall()
        i = 0
        for row in rows:
            i += 1
            print(
                f"[{i}] IP: {row['ip']}, Timestamp: {row['timestamp']}, "
                f"Method: {row['method']}, Path: {row['path']}, "
                f"Status: {row['status_code']}, Size: {row['response_size']} bytes"
            )

    def close(self):
        self.conn.close()
