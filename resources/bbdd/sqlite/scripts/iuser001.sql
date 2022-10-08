INSERT INTO users
        (sw_allow, creation_time, audit_time)
    VALUES
        (?,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)
