import psutil

battery = psutil.sensors_battery()
percent = battery.percent

if percent <= 30:
 
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=5,
        urgency='critical',
    ).send()