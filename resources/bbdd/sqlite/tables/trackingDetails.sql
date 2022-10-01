CREATE TABLE IF NOT EXISTS tracking_details (
	id INTEGER PRIMARY KEY,
	id_trackings_fk INTEGER NOT NULL,
	detail_head TEXT NOT NULL,
	detail_text TEXT NOT NULL,
	detail_time TIMESTAMP NOT NULL,
	audit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(detail_head, detail_text, detail_time),
	FOREIGN KEY(id_trackings_fk) REFERENCES trackings(id)
);