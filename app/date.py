from datetime import datetime
import parsedatetime
import dateparser

# retrieve date text and convert it into date type
# parsedatetime library doesn't work with numerical dates, it works only for relative dates
# more info can be found here: https://dateparser.readthedocs.io/en/latest/

def get_date(date):

    if "-" in date or "/" in date:                      # if these characters exist in the string
        return dateparser.parse(date).date()            # the date provided is numerical and use the 'dateparser' library
    else:
        cal = parsedatetime.Calendar()                  # if the date provided is relative
        time_struct, parse_status = cal.parse(date)     # then use the 'parsedatetime' library
        
        return datetime(*time_struct[:6]).date()