from datetime import datetime
import parsedatetime


def get_date(date):
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(date)
    
    return datetime(*time_struct[:6]).date()