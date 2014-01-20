#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''
#矿工帐号
WORKER_NAME = 'ezioruan.ezio_worker'
#矿工密码
WORKER_PASSWORD = 'worker'   



#挖矿命令
MINERD_CMD = "./minerd -a scrypt -r 1 -t 4 -s 6 -o http://127.0.0.1:8332 -O %s:%s" % (WORKER_NAME,WORKER_PASSWORD)

#代理命令
PROXY_CMD = "python mining_proxy.py -pa scrypt -o coinotron.com -p 3334"
