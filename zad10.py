import datetime
import pytz

YEAR = 365
MONTH = 12

input1 = 'April 12, 1961 2:07 local time'
input2 = '07/21/69 2:56:15 AM UTC'

gagarin = datetime.datetime.strptime(input1, "%B %d, %Y %H:%M local time")
amstrong =  datetime.datetime.strptime(input2, "%x %X %p %Z")

roznica  = amstrong - gagarin

def timedelta_to_clocktime(delta):

    year, day = divmod(roznica.days, YEAR)
    month, day = divmod(day, MONTH)

    return {
        'year': year,
        'month': month,
        'day': day,
    }

uplynelo = timedelta_to_clocktime(roznica)

print(f'Upłyneło: {uplynelo["year"]} lat, {uplynelo["month"]} miesięcy i {uplynelo["day"]} dni')

delta = datetime.timedelta(seconds= roznica.total_seconds())

now = datetime.datetime.now()
future = now + delta

print(future.date())

birthday = datetime.datetime(1970, 1, 1, 0, 0, 0)
ile_lat = future - birthday
