from O365 import Account, calendar
import datetime as dt
from pytz import timezone
import webbrowser


class todoList:
    def __init__(self):
        self.KST = timezone('Asia/Seoul')
        self.credentials = ('eaff6f02-e564-47be-b88a-9e4088cb010f', 'sL78Q~AtlVSLSOB-IdnNK3hZNhXS3KL38mRB-bvI')
        self.account = Account(self.credentials)
        self.schedule = None
        self.calendar = None

    # 인증 절차
    def auth_one(self, *, scopes=None, **kwargs): # scopes = ['Calendars.ReadWrite']
        url, state = self.account.con.get_authorization_url(requested_scopes= scopes,**kwargs)
        webbrowser.open(url)
        #token_url = input("웹페이지 주소를 복사 붙여넣기 해주세요.")
        #result = account.con.request_token(token_url, **kwargs)
        #print(result)

    def auth_two(self, _token_url, *, scopes=None, **kwargs):
        result = self.account.con.request_token(_token_url, **kwargs)
        self.schedule = self.account.schedule()
        self.calendar = self.schedule.get_default_calendar()
        return result

    def makeSchedule(self, _fileName, _deadline): # dt.datetime(정수로 연도)
        event = self.calendar.new_event()
        event.subject = _fileName
        event.location = 'Korea'
        event.start = self.KST.localize(_deadline)
        endTime = _deadline + dt.timedelta(hours=23, minutes=59, seconds=59)
        event.end = self.KST.localize(endTime)
        event.save()

'''
test = todoList()
test.auth_one(scopes=['Calendars.ReadWrite'])
test.auth_two(input(), scopes=['Calendars.ReadWrite'])
test.makeSchedule("tes.txt", dt.datetime(2022,6,10))
'''

'''

# 시간대 설정
KST = timezone('Asia/Seoul')

# 앱 아이디 , 인증서 및 암호(값)
credentials = ('eaff6f02-e564-47be-b88a-9e4088cb010f', 'sL78Q~AtlVSLSOB-IdnNK3hZNhXS3KL38mRB-bvI')

account = Account(credentials)


def test(*, scopes=None, **kwargs):
    url, state = account.con.get_authorization_url(requested_scopes= scopes,**kwargs)
    webbrowser.open(url)
    token_url = input("웹페이지 주소를 복사 붙여넣기 해주세요.")
    result = account.con.request_token(token_url, **kwargs)
    print(result)

test(scopes=['Calendars.ReadWrite'])





def makeSchedule(_fileName, _deadline):
    event = calendar.new_event()
    event.subject = _fileName
    event.location = 'Korea'
    event.start = KST.localize(dt.datetime.utcnow())
    event.recurrence.set_daily(1, end=KST.localize(_deadline))
    event.remind_before_minutes = 1440
    event.save()


schedule = account.schedule()

calendar = schedule.get_default_calendar()

# 작동 예시
makeSchedule("SW종합경진대회.hwp", dt.datetime(2022,6,3))

'''