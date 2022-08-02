from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(trackingFolder):
            src = trackingFolder + "\\" + filename
            newDest = folderDest + "\\" + filename
            os.rename(src,newDest)

#folder principal 
trackingFolder = ""
#folder destinario
folderDest = ""

event_handler = MyHandler();

observer = Observer();

observer.schedule(event_handler, trackingFolder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join            