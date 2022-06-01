from O365 import Account, calendar
import datetime as dt
from pytz import timezone
import webbrowser

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

