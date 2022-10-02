UPDATE trackings
    SET
        expiration_date = ?,
        audit_time = CURRENT_TIMESTAMP
    WHERE
        id = ?
