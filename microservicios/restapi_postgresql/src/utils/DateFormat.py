import datetime
class DateFormat:
    @classmethod
    def date2ymd(self, date):
        return datetime.datetime.strftime(date, '%Y-%m-%d')