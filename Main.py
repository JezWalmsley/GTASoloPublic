# Imports
import time
import psutil

# Find PID Of GTAV

processName = "GTA5"
pid = None

for proc in psutil.process_iter():
    if processName in proc.name():
        pid = proc.pid

# If GTAV is not found

if pid is None:
    print("GTAV Process Not Found")
    print("Go into online and try again.")
    time.sleep(5)
    exit()

# SUSpend Process then resume

print("GTA Process found")

process = psutil.Process(pid)

print("Suspending...")
process.suspend()
time.sleep(9)
process.resume()
print("Should Be in a solo session")
time.sleep(2)
print("Exiting Now...")
time.sleep(3)

input()
