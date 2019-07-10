import schedule
import datetime
import time

def job():
    print("I'm working...",datetime.datetime.now())

schedule.every(1).minutes.do(job)
schedule.every(10).seconds.do(job)
schedule.every(60).seconds.do(job)
#schedule.every(5*60).seconds.do(job)
#schedule.every(60*60).seconds.do(job)
#schedule.every(112*60).seconds.do(job)
#schedule.every(115*60).seconds.do(job)
#schedule.every(130).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).days.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
