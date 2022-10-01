CREATE TABLE IF NOT EXISTS trackings (
	id INTEGER PRIMARY KEY,
	track_type TEXT NOT NULL,
	track_code TEXT NOT NULL,
	telegram_user_id INTEGER NOT NULL,
	expiration_date TIMESTAMP,
	last_update TIMESTAMP,
	audit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(tracking_code, telegram_user_id)
);