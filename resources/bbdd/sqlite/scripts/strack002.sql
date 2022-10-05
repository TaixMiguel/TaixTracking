SELECT * FROM trackings
    WHERE user_id IN (SELECT id FROM users WHERE sw_allow = 1)
