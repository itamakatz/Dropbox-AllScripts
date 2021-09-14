import os 
import time
import sched
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))

PS_URL = dir_path + r"\Printrun Screenshot Monitor.ps1"

MINUTES = 5
WAIT_SEC = 60 * MINUTES

s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
	subprocess.call(['powershell', '-NoProfile', '-WindowStyle', 'Hidden', '-File', PS_URL])
	s.enter(WAIT_SEC, 1, do_something, (sc,))

s.enter(WAIT_SEC, 1, do_something, (s,))
s.run()