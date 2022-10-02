INSERT INTO users
        (telegram_id, telegram_username, telegram_language_code,
        sw_allow, creation_time, audit_time)
    VALUES
        (?,?,?,
        ?,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)
