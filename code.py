import os
import time
import shutil
path = input("Enter the path: ")
days = int(input("Delete files older than how many days? "))
current_time= time.time()
no_of_sec = days*86400  #Here 24*60*60 is 86400, converting days to seconds
time_old = current_time - no_of_sec
print("Deleting files older than",time_old,"Leaving those younger, up until",current_time)
if os.path.exists(path):
    for (root,dirs,files) in os.walk(path):
        #print("ROOT",root)
        #print("DIRS",dirs)
        #print("FILES",files)
        #print("-----------------")
        for f in files:
            p=os.path.join(root,f)
            #print(p)
            #print(os.stat(p).st_ctime)
            t=os.stat(p).st_ctime
            if t<time_old:
                if os.remove(p):
                    print("Deleted file at: ",p)
                else:
                    print("Unable to delete file: ",p)
        for d in dirs:
            p=os.path.join(root,d)
            t=os.stat(p).st_ctime
            if t<time_old:
                if shutil.rmtree(p):
                    print("Deleted folder at: ",p)
                else:
                    print("Unable to delete folder: ",p)
