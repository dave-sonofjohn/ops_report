
TRAILERS_QUERY1 = 'SELECT\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Frac Job\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Reopen Job\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Install\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Acidizing Job\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Other Service\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Off\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Maintenance\' THEN 1 ELSE 0 END),\
            SUM(CASE WHEN trailer_tracking.tr_status = \'Standby\' THEN 1 ELSE 0 END)\
            FROM trailer_tracking WHERE track_date >= \'2019-06-01\''