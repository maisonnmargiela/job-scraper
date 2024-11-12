import schedule
import time

def schedule_job(task, timeRepeat):
    try:
        schedule.every().day.at(timeRepeat).do(task)

        while True:
            schedule.run_pending()
            time.sleep(60)
    except Exception as e:
        print(f"Error in schedule_job: {e}")
