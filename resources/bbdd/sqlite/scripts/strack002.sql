SELECT * FROM trackings
    WHERE id IN (
        SELECT DISTINCT(id_tracking_fk) FROM user_tracking WHERE id_user_fk IN (
            SELECT id FROM users WHERE sw_allow = 1))
