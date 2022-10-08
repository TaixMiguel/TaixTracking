UPDATE trackings
    SET
        track_alias = ?,
        audit_time = CURRENT_TIMESTAMP
    WHERE
        id = ?
