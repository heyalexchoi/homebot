import schedule
import time

def ten_minute_job():
    print(f"{get_time()} ten minute job starting")
    ten_second_thing()

def three_day_job():
    print(f"{get_time()} three day job starting")
    ten_second_thing()

def ten_second_thing():
    print(f"ten_second_thing starting: {get_time()}")
    time.sleep(10)
    print(f"ten_second_thing ended: {get_time()}")

def get_time():
    return time.asctime(time.localtime())

if __name__ == '__main__':
    schedule.every(10).minutes.do(ten_minute_job)
    schedule.every(3).days.do(three_day_job)
    while True:
        schedule.run_pending()
        time.sleep(1)
