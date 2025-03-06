import time
import schedule
import json
import os
from plyer import notification

APP_NAME = 'Gulp'
DEFAULT_INTERVAL = 10
DEFAULT_MESSAGE = 'Drink water, stay hydrated!'
CONFIG = os.path.join(os.path.dirname(__file__), 'config.json')

def notify(message):
    notification.notify(
        title='💧 Gulp',
        message=message,
        app_name=APP_NAME,
        timeout=2
    )

def load_config():
    try:
        with open(CONFIG, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {
            "interval": DEFAULT_INTERVAL, 
            "message": DEFAULT_MESSAGE,
            "is_running": False
        }
    
def check_status():
    config = load_config()
    return config.get("is_running")
    
def stop_reminder():
    config = load_config()

    is_running = config.get("is_running")
    if not is_running:
        print('Reminder is not running!')
        return
    
    print('Reminder stops!')
    config["is_running"] = False
    with open(CONFIG, "w") as config_file:
        json.dump(config, config_file, indent=4)
    
    schedule.clear()

def start_reminder():
    config = load_config()

    is_running = config.get("is_running")
    if is_running:
        print('Reminder is running!')
        return
    
    config["is_running"] = True
    with open(CONFIG, "w") as config_file:
        json.dump(config, config_file, indent=4)

    interval = config.get("interval")
    message = config.get("message")
    schedule.every(interval).seconds.do(notify, message)

    print('Reminder starts!')
    while True:
        config = load_config()
        is_running = config.get("is_running")
        if not is_running:
            schedule.clear()
            break

        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_reminder()
