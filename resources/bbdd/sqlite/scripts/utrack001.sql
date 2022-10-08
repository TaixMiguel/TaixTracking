UPDATE user_tracking
    SET track_alias = ?
    WHERE   id_user_fk = ?
        AND id_tracking_fk = ?
