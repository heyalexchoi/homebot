import schedule
import time

def ten_minute_job():
    print(f"{time.asctime(time.localtime())} ten minute job")

def three_day_job():
    print(f"{time.asctime(time.localtime())} three days job")


if __name__ == '__main__':
    schedule.every(10).minutes.do(ten_minute_job)
    schedule.every(3).days.do(three_day_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
