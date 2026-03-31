import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bakopy.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS config (
            key   TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS backups (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp   TEXT NOT NULL,
            backup_path TEXT NOT NULL,
            folders     TEXT NOT NULL,
            copied      INTEGER DEFAULT 0,
            skipped     INTEGER DEFAULT 0,
            total_size  TEXT,
            categories  TEXT,
            errors      TEXT,
            success     INTEGER DEFAULT 1,
            created_at  TEXT DEFAULT (datetime('now','localtime'))
        )
    """)
    conn.commit()
    conn.close()


def get_config(key, default=None):
    conn = get_connection()
    row = conn.execute("SELECT value FROM config WHERE key = ?", (key,)).fetchone()
    conn.close()
    return row["value"] if row else default


def set_config(key, value):
    conn = get_connection()
    conn.execute(
        "INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)", (key, value)
    )
    conn.commit()
    conn.close()


def save_backup(result, folders):
    conn = get_connection()
    conn.execute("""
        INSERT INTO backups
        (timestamp, backup_path, folders, copied, skipped, total_size, categories, errors, success)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        result.get("timestamp"),
        result.get("backup_path", ""),
        json.dumps(folders),
        result.get("copied", 0),
        result.get("skipped", 0),
        result.get("total_size", "0 B"),
        json.dumps(result.get("categories", {})),
        json.dumps(result.get("errors", [])),
        1 if result.get("success") else 0,
    ))
    conn.commit()
    conn.close()


def get_backups():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM backups ORDER BY id DESC").fetchall()
    conn.close()
    result = []
    for r in rows:
        item = dict(r)
        item["folders"] = json.loads(item["folders"])
        item["categories"] = json.loads(item["categories"])
        item["errors"] = json.loads(item["errors"])
        result.append(item)
    return result


def delete_backup_record(backup_id):
    conn = get_connection()
    conn.execute("DELETE FROM backups WHERE id = ?", (backup_id,))
    conn.commit()
    conn.close()
