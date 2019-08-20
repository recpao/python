import time
import subprocess

p = subprocess.Popen(["chrome", "https://www.google.it"])
time.sleep(60)
p.kill()