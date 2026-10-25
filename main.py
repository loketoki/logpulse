from logpulse.parser import parse_file
from logpulse.database import DatabaseManager

if __name__ == "__main__":
    logs = parse_file("sample_logs/server.log")
    
    db = DatabaseManager("logs.db")


    for log in logs:
        db.insertLog(log)


    print("--- Contenuto del Database --- ")
    db.fetch_all_logs()

    db.close()


