
def build_trailer_query1(query_range):
    return 'SELECT\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Frac Job\' THEN 1 ELSE 0 END) AS \'Frac Job\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Reopen Job\' THEN 1 ELSE 0 END) AS \'Reopen Job\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Install\' THEN 1 ELSE 0 END) AS \'Install Job\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Acidizing Job\' THEN 1 ELSE 0 END) AS \'Acidizing Job\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Other Service\' THEN 1 ELSE 0 END) AS \'Other Service\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Off\' THEN 1 ELSE 0 END) AS \'Off\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Maintenance\' THEN 1 ELSE 0 END) AS \'Maintenance\',\
        SUM(CASE WHEN trailer_tracking.tr_status = \'Standby\' THEN 1 ELSE 0 END) AS \'Standby\'\
        FROM trailer_tracking WHERE track_date >= \'{0}\'\
        AND track_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_trailer_query2(query_range):
    return 'SELECT tr.tr_num AS \'index\',\
        SUM(CASE WHEN trtk.tr_status = \'Frac Job\' THEN 1 ELSE 0 END) AS \'Frac Job\',\
        SUM(CASE WHEN trtk.tr_status = \'Reopen Job\' THEN 1 ELSE 0 END) AS \'Reopen Job\',\
        SUM(CASE WHEN trtk.tr_status = \'Install\' THEN 1 ELSE 0 END) AS \'Install Job\',\
        SUM(CASE WHEN trtk.tr_status = \'Acidizing Job\' THEN 1 ELSE 0 END) AS \'Acidizing Job\',\
        SUM(CASE WHEN trtk.tr_status = \'Other Service\' THEN 1 ELSE 0 END) AS \'Other Service\',\
        SUM(CASE WHEN trtk.tr_status = \'Off\' THEN 1 ELSE 0 END) AS \'Off\',\
        SUM(CASE WHEN trtk.tr_status = \'Maintenance\' THEN 1 ELSE 0 END) AS \'Maintenance\',\
        SUM(CASE WHEN trtk.tr_status = \'Standby\' THEN 1 ELSE 0 END) AS \'Standby\'\
        FROM trailer_tracking as trtk\
        JOIN trailers AS tr ON tr.tr_id = trtk.tr_id\
        WHERE trtk.track_date >= \'{0}\' AND trtk.track_date <= \'{1}\'\
        GROUP BY tr.tr_num ORDER BY tr.tr_num;'.format(query_range['start'], query_range['end'])

def build_manpower_query1(query_range):
    return 'SELECT\
        SUM(CASE WHEN mpwr.emp_status = \'Frac Job\' THEN 1 ELSE 0 END) AS \'Frac Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Reopen Job\' THEN 1 ELSE 0 END) AS \'Reopen Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Install\' THEN 1 ELSE 0 END) AS \'Install\',\
        SUM(CASE WHEN mpwr.emp_status = \'Acidizing Job\' THEN 1 ELSE 0 END) AS \'Acidizing Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Other Service\' THEN 1 ELSE 0 END) AS \'Other Service\',\
        SUM(CASE WHEN mpwr.emp_status = \'Off\' THEN 1 ELSE 0 END) AS \'Off\',\
        SUM(CASE WHEN mpwr.emp_status = \'Unavailable\' THEN 1 ELSE 0 END) AS \'Unavailable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Standby - Billable\' THEN 1 ELSE 0 END) AS \'Standby - Billable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Standby - Non Billable\' THEN 1 ELSE 0 END) AS \'Standby - Non Billable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Training\' THEN 1 ELSE 0 END) AS \'Training\',\
        SUM(CASE WHEN mpwr.emp_status = \'Training - Field\' THEN 1 ELSE 0 END) AS \'Training - Field\',\
        SUM(CASE WHEN mpwr.emp_status = \'Mob\' THEN 1 ELSE 0 END) AS \'Mob\',\
        SUM(CASE WHEN mpwr.emp_status = \'DeMob\' THEN 1 ELSE 0 END) AS \'DeMob\',\
        SUM(CASE WHEN mpwr.emp_status = \'Office Work\' THEN 1 ELSE 0 END) AS \'Office Work\'\
        FROM mpwr_tracking as mpwr\
        WHERE mpwr.track_date >= \'{0}\' AND mpwr.track_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_manpower_query2(query_range):
    return 'SELECT emp.emp_name AS \'index\',\
        SUM(CASE WHEN mpwr.emp_status = \'Frac Job\' THEN 1 ELSE 0 END) AS \'Frac Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Reopen Job\' THEN 1 ELSE 0 END) AS \'Reopen Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Install\' THEN 1 ELSE 0 END) AS \'Install\',\
        SUM(CASE WHEN mpwr.emp_status = \'Acidizing Job\' THEN 1 ELSE 0 END) AS \'Acidizing Job\',\
        SUM(CASE WHEN mpwr.emp_status = \'Other Service\' THEN 1 ELSE 0 END) AS \'Other Service\',\
        SUM(CASE WHEN mpwr.emp_status = \'Off\' THEN 1 ELSE 0 END) AS \'Off\',\
        SUM(CASE WHEN mpwr.emp_status = \'Unavailable\' THEN 1 ELSE 0 END) AS \'Unavailable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Standby - Billable\' THEN 1 ELSE 0 END) AS \'Standby - Billable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Standby - Non Billable\' THEN 1 ELSE 0 END) AS \'Standby - Non Billable\',\
        SUM(CASE WHEN mpwr.emp_status = \'Training\' THEN 1 ELSE 0 END) AS \'Training\',\
        SUM(CASE WHEN mpwr.emp_status = \'Training - Field\' THEN 1 ELSE 0 END) AS \'Training - Field\',\
        SUM(CASE WHEN mpwr.emp_status = \'Mob\' THEN 1 ELSE 0 END) AS \'Mob\',\
        SUM(CASE WHEN mpwr.emp_status = \'DeMob\' THEN 1 ELSE 0 END) AS \'DeMob\',\
        SUM(CASE WHEN mpwr.emp_status = \'Office Work\' THEN 1 ELSE 0 END) AS \'Office Work\'\
        FROM mpwr_tracking as mpwr\
        JOIN field_emp AS emp ON mpwr.emp_id = emp.emp_id\
        WHERE mpwr.track_date >= \'{0}\' AND mpwr.track_date <= \'{1}\'\
        GROUP BY emp.emp_name ORDER BY emp.emp_name;'.format(query_range['start'], query_range['end'])

def build_ops_incidents_query1(query_range):
    return 'SELECT\
        SUM(CASE WHEN severity = \'Light\' THEN 1 ELSE 0 END) AS \'Light\',\
        SUM(CASE WHEN severity = \'Serious\' THEN 1 ELSE 0 END) AS \'Serious\',\
        SUM(CASE WHEN severity = \'Major\' THEN 1 ELSE 0 END) AS \'Major\',\
        SUM(CASE WHEN severity = \'Catastrophic\' THEN 1 ELSE 0 END) AS \'Catastrophic\'\
        FROM ops_inc_tracking\
        WHERE kobold_resp = \'Yes\'\
        AND inc_date >= \'{0}\'\
        AND inc_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_ops_incidents_query2(query_range):
    return 'SELECT\
        DATENAME(month, inc_date) AS \'index\',\
        SUM(CASE WHEN severity = \'Light\' THEN 1 ELSE 0 END) AS \'Light\',\
        SUM(CASE WHEN severity = \'Serious\' THEN 1 ELSE 0 END) AS \'Serious\',\
        SUM(CASE WHEN severity = \'Major\' THEN 1 ELSE 0 END) AS \'Major\',\
        SUM(CASE WHEN severity = \'Catastrophic\' THEN 1 ELSE 0 END) AS \'Catastrophic\'\
        FROM ops_inc_tracking\
        WHERE kobold_resp = \'Yes\'\
        AND inc_date >= \'{0}\'\
        AND inc_date <= \'{1}\'\
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
            END;'.format(query_range['start'], query_range['end'])

def build_ops_incidents_query3(query_range):
    return 'SELECT\
        SUM(CASE WHEN inc_type = \'Kobold Tool - General\' THEN 1 ELSE 0 END) AS \'Kobold Tool - General\',\
        SUM(CASE WHEN inc_type = \'Kobold Tool - Cycling\' THEN 1 ELSE 0 END) AS \'Kobold Tool - Cycling\',\
        SUM(CASE WHEN inc_type = \'Element Issue\' THEN 1 ELSE 0 END) AS \'Element Issue\',\
        SUM(CASE WHEN inc_type = \'Guide Sub\' THEN 1 ELSE 0 END) AS \'Guide Sub\',\
        SUM(CASE WHEN inc_type = \'Kobold Sleeve - General\' THEN 1 ELSE 0 END) AS \'Kobold Sleeve - General\',\
        SUM(CASE WHEN inc_type = \'Kobold Sleeve - Closing\' THEN 1 ELSE 0 END) AS \'Kobold Sleeve - Closing\',\
        SUM(CASE WHEN inc_type = \'Kobold Sleeve - Opening\' THEN 1 ELSE 0 END) AS \'Kobold Sleeve - Opening\',\
        SUM(CASE WHEN inc_type = \'Kobold Sleeve - Leaking\' THEN 1 ELSE 0 END) AS \'Kobold Sleeve - Leaking\',\
        SUM(CASE WHEN inc_type = \'3rd Party Gauge\' THEN 1 ELSE 0 END) AS \'3rd Party Gauge\',\
        SUM(CASE WHEN inc_type = \'Wellbore\' THEN 1 ELSE 0 END) AS \'Wellbore\',\
        SUM(CASE WHEN inc_type = \'Environment\' THEN 1 ELSE 0 END) AS \'Environment\',\
        SUM(CASE WHEN inc_type = \'Coil\' THEN 1 ELSE 0 END) AS \'Coil\',\
        SUM(CASE WHEN inc_type = \'Frac\' THEN 1 ELSE 0 END) AS \'Frac\',\
        SUM(CASE WHEN inc_type = \'Other\' THEN 1 ELSE 0 END) AS \'Other\'\
        FROM ops_inc_tracking\
        WHERE kobold_resp = \'Yes\'\
        AND inc_date >= \'{0}\'\
        AND inc_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_header_query(query_range):
    return 'SELECT\
        SUM(CASE WHEN fjs_id IS NOT NULL THEN 1 ELSE 0 END) AS \'Total Frac Jobs\',\
        SUM(CASE WHEN num_trips > 1 THEN 1 ELSE 0 END) AS \'Total Kobold Tool Runs\',\
        SUM(time_inhole) AS \'Time In Hole (hrs)\',\
        SUM(unacc_time) AS \'NPT (hrs)\',\
        SUM(tmd) * 2 AS \'In Hole Distance Travelled (m)\',\
        SUM(tot_frac_tons) AS \'Total Tons Fracked\',\
        SUM(num_stages) AS \'Total Stages Fracked\'\
        FROM fj_summ_2019\
        WHERE frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_num_trips_query(query_range):
    return 'SELECT\
        SUM(CASE WHEN num_trips = 1 THEN 1 ELSE 0 END) AS \'1 Trip\',\
        SUM(CASE WHEN num_trips = 2 THEN 1 ELSE 0 END) AS \'2 Trips\',\
        SUM(CASE WHEN num_trips = 3 THEN 1 ELSE 0 END) AS \'3 Trips\',\
        SUM(CASE WHEN num_trips > 3 THEN 1 ELSE 0 END) AS \'> 3 Trips\'\
        FROM fj_summ_2019\
        WHERE frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_stages_brkdwn_query(query_range):
    return 'SELECT\
        SUM(num_stages) AS \'Stages Fracked\',\
        SUM(tot_so) AS \'Stages SO\',\
        SUM(tot_cut) AS \'Stages Cut\',\
        SUM(tot_abdn) AS \'Stages Abandonned\',\
        SUM(tot_leak) AS \'Stages Leaking\',\
        SUM(tot_popt) AS \'Number of Pop Thrus\',\
        SUM(tot_misloc) AS \'Number of Mislocates\'\
        FROM fj_summ_2019\
        WHERE frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_job_depth_query(query_range):
    return 'SELECT\
        SUM(CASE WHEN tmd <= 1000 THEN 1 ELSE 0 END) AS \'<1000 m\',\
        SUM(CASE WHEN tmd > 1000 AND  tmd <= 2000 THEN 1 ELSE 0 END) AS \'1000-2000 m\',\
        SUM(CASE WHEN tmd > 2000 AND tmd <= 3000 THEN 1 ELSE 0 END) AS \'2000-3000 m\',\
        SUM(CASE WHEN tmd > 3000 AND tmd <= 4000 THEN 1 ELSE 0 END) AS \'3000-4000 m\',\
        SUM(CASE WHEN tmd > 4000 THEN 1 ELSE 0 END) AS \'>4000 m\'\
        FROM fj_summ_2019\
        WHERE frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\';'.format(query_range['start'], query_range['end'])

def build_job_formation_query(query_range):
    return 'SELECT\
        DISTINCT(job_form) AS \'index\',\
        SUM(CASE WHEN fjs_id IS NOT NULL THEN 1 ELSE 0 END) AS \'Job Count\'\
        FROM fj_summ_2019\
        WHERE job_form IS NOT NULL\
        AND frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\'\
        GROUP BY job_form;'.format(query_range['start'], query_range['end'])

def build_stage_time_query(query_range):
    return 'SELECT\
        DISTINCT(cl.client_name) AS \'index\',\
        CAST((ROUND(AVG(fjs.avg_frac_time), 2)) AS DECIMAL(5,2)) AS \'Avg Frac Time (min)\',\
        CAST((ROUND(AVG(fjs.avg_btwn_time), 2)) AS DECIMAL(5,2)) AS \'Avg Btwn Stage Time (min)\'\
        FROM fj_summ_2019 AS fjs\
        LEFT JOIN clients AS cl ON fjs.client_id = cl.client_id\
        WHERE fjs.client_id IS NOT NULL\
        AND frac_date >= \'{0}\'\
        AND frac_date <= \'{1}\'\
        GROUP BY cl.client_name;'.format(query_range['start'], query_range['end'])