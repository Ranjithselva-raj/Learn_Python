import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import logging

logging.basicConfig(filename='watchdog.log',level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if "Data_stream.txt" in event.src_path:
            logger.info("File has been modified")
            os.system("python C:\\Users\\ranje\\OneDrive\\D_Folder\\Python_Files\\txt_to_json\\txt_json.py")

observer = Observer()
event_handler = MyHandler()
observer.schedule(event_handler, path= "C:\\Users\\ranje\\OneDrive\\Desktop", recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
