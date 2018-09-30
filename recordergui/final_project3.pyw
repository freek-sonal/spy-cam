import time
import ctypes
import cv2
from datetime import datetime as dt
user32 = ctypes.windll.user32
time.sleep (1.0)

while 1:
      
      
      OpenDesktop = user32.OpenDesktopW
      SwitchDesktop = user32.SwitchDesktop
      DESKTOP_SWITCHDESKTOP = 0x0100
      
      hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
      result = SwitchDesktop (hDesktop)
      
      
      if result:
        #print("Unlocked")
        
        try : 
         cap.release()
         out.release()
         cv2.destroyAllWindows()
         print("Unlocked")
         break
        except :
            print("Unlocked")
            
        #break
      else:
          print(result)
          print(time.asctime (), "still locked")
          
          cap = cv2.VideoCapture(0)
          fourcc = cv2.VideoWriter_fourcc(*'MJPG')
          name=[str(dt.now().year),str(dt.now().month),str(dt.now().day),
                str(dt.now().hour),
                str(dt.now().minute),
                str(dt.now().second)]
          name=(('-'.join(name))+'.avi')
          #print(name)
          out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))
          while(True):
             hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
             result1 = SwitchDesktop (hDesktop)
             ret, frame = cap.read()
             #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             out.write(frame)
             cv2.imshow('frame',frame)
             if result1==1:
                break
      
      
'''      
cap.release()
out.release()
cv2.destroyAllWindows() 
     
   '''       

      #time.sleep (2)