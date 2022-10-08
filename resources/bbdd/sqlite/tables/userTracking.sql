CREATE TABLE IF NOT EXISTS user_tracking (
	id INTEGER PRIMARY KEY,
	id_user_fk INTEGER NOT NULL,
	id_tracking_fk INTEGER NOT NULL,
	track_alias TEXT,
	UNIQUE(id_user_fk, id_tracking_fk),
	FOREIGN KEY(id_user_fk) REFERENCES users(id),
	FOREIGN KEY(id_tracking_fk) REFERENCES trackings(id)
);