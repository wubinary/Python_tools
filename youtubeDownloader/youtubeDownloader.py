import queue, time, threading, datetime, sys, os
from pytube import YouTube

class Job:    
     def __init__(self, link):    
             self.link = link    
     def do(self):
          location = os.getcwd()+'/'
          try:
               yt = YouTube(self.link).streams.first().download(location)
               print("\t[Info Done] {}".format(self.link))
          except Exception as inst:
               print(inst)
               print("\t[Info Failed] {}".format(self.link))


youtubeLinks = []
que = queue.Queue() 
def getYoutubeLink():
     global youtubeLinks
     with open ('youtubeLinks.txt','r',encoding='utf8') as f:
          for link in f:
               link = str(link).replace('\n','')
               que.put(Job(link)) 
               
getJob_lock = threading.Lock()
def doJob(*args):
     time.sleep(2)
     queue = args[0]
     while queue.qsize() > 0:  
          getJob_lock.acquire()
          job = queue.get()
          getJob_lock.release()
          job.do()
          
     
# Open three threads
thd0 = threading.Thread(target=getYoutubeLink, name='Thd0')
thd1 = threading.Thread(target=doJob, name='Thd1', args=(que,))  
thd2 = threading.Thread(target=doJob, name='Thd2', args=(que,))  
thd3 = threading.Thread(target=doJob, name='Thd3', args=(que,))  
  
# Start activity to digest queue.  
st = datetime.datetime.now()
thd0.start()
thd1.start()  
thd2.start()  
thd3.start()  
  
# Wait for all threads to terminate.  
while thd0.is_alive() or thd1.is_alive() or thd2.is_alive() or thd3.is_alive():  
     time.sleep(1)    
  
td = datetime.datetime.now() - st  
print("\t[Info] Spending time={0}!".format(td))
os.system('pause')
