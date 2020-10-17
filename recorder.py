import pyautogui as pg
import time,datetime
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract,os,time
#print(pg.position())
def chekEND():
    while True:
        data=pytesseract.image_to_string(pg.screenshot(), lang='rus')
        if ("Видеотрансляция завершена" in data):
            print("evrika")
            break
        time.sleep(1)
        print("no")
def waitDownlouad():
    while True:
        data=''.join(os.listdir("./tmp"))
        if("part" not in data):
            os.system("ffmpeg -i ./tmp/*.webm -c:v copy -c:a copy ./saves/record-"+datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")+".webm")
            os.system("rm -rf ./tmp/*")
            return 0
        
def startRecording():
    pg.leftClick(1846,90,duration=0.5)
    pg.leftClick(679,183,duration=0.5)
def stopRecording():
    pg.leftClick(679,183,duration=0.5)
    time.sleep(5)
    pg.leftClick(1137,650,duration=0.5)
def pageScale():
    pg.leftClick(1900,86,duration=0.5)
    pg.leftClick(1852,301,duration=0.5)
    pg.leftClick(1852,301,duration=0.5)
    pg.leftClick(1852,301,duration=0.5)

if("В ПРЯМОМ ЭФИРЕ" in pytesseract.image_to_string(pg.screenshot(region=(1145,260,160,30)), lang='rus')):
    #pageScale()
    startRecording()
    chekEND()
    stopRecording()
    waitDownlouad()
else:print("Сейчас нет прямого эфира!!!")
