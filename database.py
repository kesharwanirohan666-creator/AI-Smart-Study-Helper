import sqlite3

def init_db():
    """Initializes the database and creates the notes table if it doesn't exist."""
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_note(title, content):
    """Adds a new study note to the database."""
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

def get_all_notes():
    """Retrieves all notes from the database."""
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, content, created_at FROM notes ORDER BY created_at DESC')
    notes = cursor.fetchall()
    conn.close()
    return notes
