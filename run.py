#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''
import gevent.monkey
gevent.monkey.patch_all()
from datetime import datetime
import gevent
import signal
from grab_news import storage
from grab_news.spider import all_spider
from grab_news.grab import get_content
from grab_news.web_server import run_web_server
from grab_news.setting import NEWS_LENGTH





def on_hour():
    pass
 


def run_forever():
    while True:
        now =  datetime.now()
        print now
        if now.minute == 0 and now.second == 0:
            on_hour()
        gevent.sleep(1)


if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
    event_thread = gevent.spawn(run_forever)
    event_thread.join()
    
    
    
    
    
    
    