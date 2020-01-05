import os
import threading
import getpass
import datetime
import json
import re
import nuke
import time

CURRENT_USER = getpass.getuser()
LOG_DIR = "/Users/path/to/your/logs"
TIMER = 60
IDLE_TIME = 300


class Timelog():

    def start_thread(self):

        Timelog.thread = threading.Timer( TIMER, self.write_json)
        Timelog.thread.setDaemon(True)
        Timelog.thread.start()

    def get_json(self):
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        json_dir = "%s/%s/%s" % (LOG_DIR, CURRENT_USER, date)
        if not os.path.exists(json_dir):
            os.makedirs(json_dir)

        self.json_path = "%s/log.json" % json_dir
        if not os.path.exists(self.json_path):
            data = {}
        else:
            _file = open(self.json_path, "r")
            data = json.load(_file)

        return data

    def write_json(self):

        self.script_path = nuke.root()['name'].value()

        regex = re.search( r"projects/(\w+)/shots/(\w+)", self.script_path)
        if regex:
            shot = "%s_%s" % (regex.group(1), regex.group(2))
        else:
            print "Invalid Path"
            self.start_thread()
            return

        if self.idle_time() > IDLE_TIME:
            print "Script is idle"
            self.start_thread()
            return


        data = self.get_json()

        if data.has_key(shot):
            data[shot] += TIMER
        else:
            data[shot] = TIMER

        _file = open(self.json_path, "w")
        json.dump(data, _file)
        print data
        self.start_thread()

    def idle_time(self):

        now = time.time()
        autosave_path = "%s.autosave" % self.script_path

        if os.path.isfile( autosave_path):
            modification_time = int(os.stat( autosave_path).st_mtime)
            _idle_time = now - modification_time

        elif nuke.modified():
            if not os.path.isfile(autosave_path):
                _idle_time = 0

        elif not nuke.modified():
            modification_time = int(os.stat( self.script_path).st_mtime)
            _idle_time = now - modification_time

        print _idle_time
        return _idle_time
