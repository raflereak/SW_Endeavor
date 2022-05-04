from O365 import Account, MSGraphProtocol


Client_ID = "raflereak@outlook.kr"
Client_PW = ""

credentials = (Client_ID, Client_PW)

protocol = MSGraphProtocol() 
#protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')




schedule = account.schedule()
calendar = schedule.get_default_calendar()
events = calendar.get_events(include_recurring=False) 
#events = calendar.get_events(query=q, include_recurring=True) 

for event in events:
    print(event)


q = calendar.new_query('start').greater_equal(dt.datetime(2019, 11, 20))
q.chain('and').on_attribute('end').less_equal(dt.datetime(2019, 11, 24))

def parse_event_string(event):
    event_string = str(event)

    start_index = event_string.find('from:') + 6
    end_index = event_string.find('to:') - 1 
    start_meeting_time = event_string[start_index:end_index]

    start_obj = datetime.datetime.strptime(start_meeting_time, '%H:%M:%S')
    now = datetime.datetime.strptime(now, '%H:%M:%S')

    time_diff_min = ((start_obj - now).total_seconds())/60

    return time_diff_min