CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	telegram_id INTEGER NOT NULL,
	telegram_username TEXT NOT NULL,
	telegram_language_code TEXT NOT NULL,
	sw_allow BOOLEAN NOT NULL CHECK (sw_allow IN (0, 1)),
	creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	audit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(telegram_id)
);