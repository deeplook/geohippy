"""
Various bits to be loaded in the Geohippy "dashboard".
"""

from multiprocessing import Process
import time

from ipywidgets import Button
import redis

from workers import start_redis


def redis_running():
    try:
        r = redis.Redis()
        r.info()
        return True
    except:
        return False


def style(button, state=True):
    if state:
        button.button_style = "success"
        button.icon = "check"
        button.tooltip = "Click to stop..."
    else:
        button.button_style = "danger"
        button.icon = "exclamation-triangle"
        button.tooltip = "Click to start..."


def click_redis(bt):
    """Start/stop redis server.
    """
    if redis_running():
        try:
            r = redis.Redis()
            r.shutdown()
        except:
            pass
    else:
        p = Process(target=start_redis, args=('bob',))
        p.start()
        time.sleep(2)
    style(bt, state=redis_running())


def make_redis_button():
    redis_bt = Button(description="Redis Server")
    redis_bt.on_click(click_redis)
    style(redis_bt, state=redis_running())
    return redis_bt
