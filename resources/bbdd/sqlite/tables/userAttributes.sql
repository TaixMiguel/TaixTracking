CREATE TABLE IF NOT EXISTS users_attributes (
	id INTEGER PRIMARY KEY,
	id_user_fk INTEGER NOT NULL,
	attribute_key TEXT NOT NULL,
	attribute_value TEXT NOT_NULL,
	UNIQUE(id_user_fk, attribute_key),
	FOREIGN KEY(id_user_fk) REFERENCES users(id)
);