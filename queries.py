
TRAILERS_QUERY1 = 'SELECT\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Frac Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Reopen Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Install\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Acidizing Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Other Service\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Off\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Maintenance\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trailer_tracking.tr_status = \'Standby\' THEN 1 ELSE 0 END)\
    FROM trailer_tracking WHERE track_date >= \'2019-06-01\';'

#TYPE 2 POSSIBLE PANDAS DF
TRAILERS_QUERY2 = 'SELECT tr.tr_num,\
    SUM(CASE WHEN trtk.tr_status = \'Frac Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Reopen Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Install\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Acidizing Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Other Service\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Off\' THEN 1 ELSE 0 END) AS \'Days Off\',\
    SUM(CASE WHEN trtk.tr_status = \'Maintenance\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN trtk.tr_status = \'Standby\' THEN 1 ELSE 0 END)\
    FROM trailer_tracking as trtk\
    JOIN trailers AS tr ON tr.tr_id = trtk.tr_id\
    GROUP BY tr.tr_num ORDER BY tr.tr_num;'

MANPOWER_QUERY1 = 'SELECT\
    SUM(CASE WHEN mpwr.emp_status = \'Frac Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Reopen Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Install\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Acidizing Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Other Service\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Off\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Unavailable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Standby - Billable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Standby - Non Billable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Training\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Training - Field\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Mob\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'DeMob\' THEN 1 ELSE 0 END)\
    FROM mpwr_tracking as mpwr;'

#TYPE 2 POSSIBLE PANDAS DF
MANPOWER_QUERY2 = 'SELECT\
    SUM(CASE WHEN mpwr.emp_status = \'Frac Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Reopen Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Install\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Acidizing Job\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Other Service\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Off\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Unavailable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Standby - Billable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Standby - Non Billable\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Training\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Training - Field\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Mob\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'DeMob\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN mpwr.emp_status = \'Office Work\' THEN 1 ELSE 0 END)\
    FROM mpwr_tracking as mpwr\
    JOIN field_emp AS emp ON mpwr.emp_id = emp.emp_id\
    GROUP BY emp.emp_name ORDER BY emp.emp_name;'

OPS_INCIDENTS_QUERY1 = 'SELECT\
    SUM(CASE WHEN severity = \'Light\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Serious\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Major\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Catastrophic\' THEN 1 ELSE 0 END)\
    FROM ops_inc_tracking\
    WHERE kobold_resp = \'Yes\';'

#TYPE 2 POSSIBLE PANDAS DF
OPS_INCIDENTS_QUERY2 = 'SELECT\
    DATENAME(month, inc_date),\
    SUM(CASE WHEN severity = \'Light\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Serious\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Major\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN severity = \'Catastrophic\' THEN 1 ELSE 0 END)\
    FROM ops_inc_tracking\
    WHERE kobold_resp = \'Yes\'\
    GROUP BY DATENAME(month, inc_date)\
    ORDER BY CASE DATENAME(month, inc_date)\
        WHEN \'January\' THEN 0\
        WHEN \'February\' THEN 1\
        WHEN \'March\' THEN 2\
        WHEN \'April\' THEN 3\
        WHEN \'May\' THEN 4\
        WHEN \'June\' THEN 5\
        WHEN \'July\' THEN 6\
        WHEN \'August\' THEN 7\
        WHEN \'September\' THEN 8\
        WHEN \'October\' THEN 9\
        WHEN \'November\' THEN 10\
        WHEN \'December\' THEN 11\
        END;'

OPS_INCIDENTS_QUERY3 = 'SELECT\
    SUM(CASE WHEN inc_type = \'Kobold Tool - General\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Kobold Tool - Cycling\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Element Issue\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Guide Sub\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Kobold Sleeve - General\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Kobold Sleeve - Closing\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Kobold Sleeve - Opening\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Kobold Sleeve - Leaking\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'3rd Party Gauge\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Wellbore\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Environment\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Coil\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Frac\' THEN 1 ELSE 0 END),\
    SUM(CASE WHEN inc_type = \'Other\' THEN 1 ELSE 0 END)\
    FROM ops_inc_tracking\
    WHERE kobold_resp = \'Yes\';'