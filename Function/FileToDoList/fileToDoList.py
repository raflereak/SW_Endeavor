from O365 import Account, calendar
import datetime as dt

credentials = ('eaff6f02-e564-47be-b88a-9e4088cb010f', 'Fyd8Q~N~ROFaUxYUFaFyG7z_S-Bt2_WPMDt7ra9N')
# Fyd8Q~N~ROFaUxYUFaFyG7z_S-Bt2_WPMDt7ra9N
# the default protocol will be Microsoft Graph

account = Account(credentials)
if account.authenticate(scopes=['basic', 'Calendars.ReadWrite']):
   print('Authenticated!')


schedule = account.schedule()
calendar = schedule.get_default_calendar()
events = calendar.get_events(include_recurring=False) 
#events = calendar.get_events(query=q, include_recurring=True) 

for event in events:
    print(event)
'''

q = calendar.new_query('start').greater_equal(dt.datetime(2019, 11, 20))
q.chain('and').on_attribute('end').less_equal(dt.datetime(2019, 11, 24))

def parse_event_string(event):
    event_string = str(event)

    start_index = event_string.find('from:') + 6
    end_index = event_string.find('to:') - 1 
    start_meeting_time = event_string[start_index:end_index]

    start_obj = dt.datetime.strptime(start_meeting_time, '%H:%M:%S')
    now = dt.datetime.strptime(now, '%H:%M:%S')

    time_diff_min = ((start_obj - now).total_seconds())/60

    return time_diff_min
    '''