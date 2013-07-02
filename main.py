#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
toodledo2grwol : Display grwol notify tasks of Toodledo

"""
import os.path
from datetime import datetime
import logging
import ConfigParser
import pynotify
from tasks import HotList


#parse config
config = ConfigParser.SafeConfigParser()
config.read(['toodledo2notify.cnf'])

pynotify.init("toodledo2notify")
logging.info('Init pynotify')

# Send Notify to Growl
notify_icon = config.get('icon', 'notify')
hotlist = HotList()
for hot_task in hotlist.retrieve():
    if not hasattr(hot_task, "duedate"):
        duedate = ""
    elif hot_task.duedate == 0:
        duedate = ""
    else:
        duedate = datetime.fromtimestamp(float(hot_task.duedate)) \
            .strftime("DueDate: %Y/%m/%d")
    n = pynotify.Notification(
        hot_task.title,
        duedate,
        os.path.abspath(notify_icon)
    )
    n.show()
    logging.info(': '.join(['notify sended', hot_task.title]))
# end
logging.info('end')
