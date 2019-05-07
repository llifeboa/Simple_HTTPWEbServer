import os, time

print(time.ctime(os.path.getmtime("./index.html")))
