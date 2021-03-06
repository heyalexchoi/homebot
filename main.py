from time import sleep
from os import system
from urllib.request import urlopen
import logging
import schedule
from gpiozero import LED

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('homebot.main.log')
fh.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

def ten_minute_job():
    logger.debug(f"{get_time()} ten minute job starting")
    # ten_second_thing()

def one_day_job():
    logger.debug(f"{get_time()} one day job starting")
    # ten_second_thing()

def three_day_job():
    logger.debug(f"{get_time()} three day job starting")
    # ten_second_thing()

def ten_second_thing():
    logger.debug(f"internet looks like it works: {test_internet()}")
    logger.debug(f"ten_second_thing starting: {get_time()}")
    time.sleep(10)
    logger.debug(f"ten_second_thing ended: {get_time()}")

def get_time():
    return time.asctime(time.localtime())

def test_internet():
    try:
        urlopen('http://www.google.com')
    except:
        return False
    return True

# pumping from tank on the ground to a vessel sitting on a chair - filled up 7 oz of water in about 35 seconds
# with 14 plants drinking say... 2 ozs of water at a time... that's 28 ozs a go. try 140 seconds.
power = LED(4) # use LED's simple on-off API - pin GPIO4 - https://gpiozero.readthedocs.io/en/stable/recipes.html
def turn_on_for_n_seconds(seconds):
    power.on()
    sleep(seconds)
    power.off()

def water_plants():
    logger.debug('watering plants...')
    turn_on_for_n_seconds(60)
    logger.debug('finished watering plants')

if __name__ == '__main__':
    logger.debug('starting main...')
    schedule.every(10).minutes.do(ten_minute_job)
    schedule.every(1).days.do(one_day_job)
    schedule.every(3).days.do(three_day_job)
    schedule.every(2).days.do(water_plants)
    while True:
        schedule.run_pending()
        time.sleep(1)
