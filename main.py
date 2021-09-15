import psutil
import os
from dotenv import load_dotenv

load_dotenv()

battery = psutil.sensors_battery()
percent = battery.percent
duration = int(os.getenv('NOTIFICATION_DURATION'))
level = int(os.getenv('BATTERY_PERCENTAGE_LEVEL_TO_NOTIFY'))

if percent <= level:
 
    from pynotifier import Notification

    Notification(
        title="Ooops",
        description="We detected " + str(percent) + "% Battery!",
        duration=duration,
        urgency='critical',
    ).send()