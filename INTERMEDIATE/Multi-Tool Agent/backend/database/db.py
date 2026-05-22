import sqlite3
import json
from datetime import datetime
from pathlib import Path

class Database:
    def __init__(self, db_path='./database/agent_data.db'):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                results TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                category TEXT,
                metadata TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipient TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                status TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input_text TEXT NOT NULL,
                analysis_result TEXT,
                model_used TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def save_search(self, query, results):
        """Save search query and results"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO searches (query, results) VALUES (?, ?)',
            (query, json.dumps(results))
        )
        conn.commit()
        search_id = cursor.lastrowid
        conn.close()
        return search_id

    def save_data(self, title, content, category='general', metadata=None):
        """Save arbitrary data"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO saved_data (title, content, category, metadata) VALUES (?, ?, ?, ?)',
            (title, content, category, json.dumps(metadata) if metadata else None)
        )
        conn.commit()
        data_id = cursor.lastrowid
        conn.close()
        return data_id

    def get_all_data(self, category=None, limit=100):
        """Retrieve saved data"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if category:
            cursor.execute(
                'SELECT * FROM saved_data WHERE category = ? ORDER BY timestamp DESC LIMIT ?',
                (category, limit)
            )
        else:
            cursor.execute(
                'SELECT * FROM saved_data ORDER BY timestamp DESC LIMIT ?',
                (limit,)
            )

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def save_email_log(self, recipient, subject, body, status):
        """Log sent emails"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO emails (recipient, subject, body, status) VALUES (?, ?, ?, ?)',
            (recipient, subject, body, status)
        )
        conn.commit()
        email_id = cursor.lastrowid
        conn.close()
        return email_id

    def save_analysis(self, input_text, analysis_result, model_used):
        """Save AI analysis results"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO analysis (input_text, analysis_result, model_used) VALUES (?, ?, ?)',
            (input_text, analysis_result, model_used)
        )
        conn.commit()
        analysis_id = cursor.lastrowid
        conn.close()
        return analysis_id

    def get_recent_searches(self, limit=10):
        """Get recent search history"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM searches ORDER BY timestamp DESC LIMIT ?',
            (limit,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
