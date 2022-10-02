CREATE TABLE IF NOT EXISTS trackings (
	id INTEGER PRIMARY KEY,
	track_type TEXT NOT NULL,
	track_code TEXT NOT NULL,
	telegram_user_id INTEGER NOT NULL,
	track_alias TEXT,
	expiration_date TIMESTAMP,
	last_update TIMESTAMP,
	creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	audit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(track_code, telegram_user_id),
	FOREIGN KEY(telegram_user_id) REFERENCES users(id)
);