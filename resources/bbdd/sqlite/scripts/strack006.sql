SELECT * FROM trackings
    WHERE   last_update = null
        AND creation_time < ?
