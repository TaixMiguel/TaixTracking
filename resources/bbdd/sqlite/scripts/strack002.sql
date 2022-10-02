SELECT * FROM trackings
    WHERE telegram_user_id IN (SELECT telegram_id FROM users WHERE sw_allow = 1)
