import time,os,threading,subprocess,sys

def muteSound(app):#"Firefox Developer Edition"
    os.system("pacmd list-sink-inputs > soundsIndex")
    data=open('soundsIndex').read()
    indexes = data.split("    index: ")
    for index in indexes:
        if(app in index):
            i = index.split("\n")[0]
            os.system("pacmd set-sink-input-mute "+i+" true")
            return 0


firefox = subprocess.Popen(("firefox-developer-edition --display=:2 https://www.instagram.com/"+sys.argv[1]+"/live/").split(" "))
time.sleep(5)
muteSound("Firefox Developer Edition")
os.system("DISPLAY=:2 python3 recorder.py")

firefox.terminate()


