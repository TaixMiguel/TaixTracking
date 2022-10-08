CREATE TABLE IF NOT EXISTS trackings (
	id INTEGER PRIMARY KEY,
	track_type TEXT NOT NULL,
	track_code TEXT NOT NULL,
	expiration_date TIMESTAMP,
	last_update TIMESTAMP,
	creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	audit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(track_type, track_code)
);