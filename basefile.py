#imports
import ch
import random
import sys
import os
import re
import cgi
import codecs
import traceback
import time
import urllib
import datetime
import binascii
import glob
import json
import csv
import zipfile
import codecs


#bot manager for colors , font ,bg display
class bot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("000000")
        self.setFontColor("FFFF00")
        self.setFontFace("Lucida Console")
        self.setFontSize(11)
        self.enableBg()
        self.enableRecording()

#when bot enters room , print is to console , room.message is to actual chat
    def onConnect(self, room):
        room.message("Initialized in "+room.name+" , type ~help for more info.")
        room.message("Adding Flavor")
        room.message("Adding Scent")
        room.message("Adding Ai")
        
        print("Connected to "+room.name)

    def onReconnect(self, room):
        print("Reconnected")
#to set permissions if needed
    def getAccess(self, user):
        if user.name.lower() == "vxu": return 2
        else: return 0
#capturing messages to look for commands , prefix set to ~
    def onMessage(self, room, user, message):
        msgdata = message.body.split(" ",1)
        if len(msgdata) > 1:
            cmd, args = msgdata[0], msgdata[1]
        else:
            cmd, args = msgdata[0],""
        cmd=cmd.lower()
        prefix = "~"
        if len(cmd) >0:
            if cmd[0]==prefix:
                used_prefix = True
                cmd = cmd[1:]
            else:
                used_prefix= False
        else:
            return

#the "say" command
        if used_prefix and cmd=="say":
            if args:
                room.message(args)
            else:
                VariableResponse = ['Nigga you gotta type something after say.', 'You gotta type something after that.', 'Man if ya bitch ass dont use the command right...', 'So you just gonna tell me to say nothing huh. Nigga fuck ya mom.', '....', 'Bruh , are you brain dead , you type something after say']
                room.message(random.choice(VariableResponse))


#the "help" command                
        if used_prefix and cmd=="help":
                room.message("Alright so this is how it is. Nigga i'm the realest bot you'll see anywhere. Best believe I got the team building me up so I can satisfy all you niggas. I'll be programmed to actually remember some of you, a brain , memories , all that, and if I like you , then you my nigga... If not , then you can swerve. Now you can type ~toys to see some things in progress (commands). Only thing working right now is that gay ass say command. That's all for now. Now go back to beating ya meat or something.")


#the "toys" command                
        if used_prefix and cmd=="toys":
                room.message(" These gotta be followed by a ~ to be put to use , currently under construction : say,talk,save,power,rating,nigga,mynigga,thot,realtalk,maxim,DDOS,GROSS,GAY,ping,BG,profile,botnet,runtime,list,youtube,skype,facebook,pm,dickpm,block,add,snake,callofduty,gif,construct,addfunction,admin,mylevel,wos,fight,worldstar,booty,hoes,flappybird,chucknorris,ronniecoleman,arnoldshwarz,you,him,her,factoflife,whois,IP,pandemic,procrastinate,fuck,idiot,memory,life,flush,flag,fury,boondocks,...more to be added..")


#the "pm" command                
        if used_prefix and cmd=="pm" and len(args) > 0:
            try:
                name = args.split()[0].lower()
                personalm = " ".join(args.split()[1:])
                self.pm.message(ch.User(name), "# you got a message from "+user.name.capitalize()+": \""+personalm.capitalize()+"\"")
                room.message("# I sent that to "+name.capitalize()+"..")
            except:
                room.message("Damn , something # up..")
        if used_prefix and cmd=="youtube":
            try:
                search = args.split()
                import urllib.request
                with urllib.request.urlopen("http://gdata.youtube.com/feeds/api/videos?vq=%s&racy=include&orderby=relevance&max-results=1" % "+".join(search)) as url:
                    udict = url.read().decode()
                a = re.finditer('http://www.youtube.com/watch\?v=(.+?)&amp;',udict)
                matches = []
                for match in a:
                    match = str(match.group(0))
                    match = match[:42]
                    matches.append(match)
                    
                id = random.choice(matches)
                id = id[31:]
                link = "http://www.youtube.com/watch?v=%s" % id
                info = youtube.Video(id)
                info_title = "%s..." % info.get_title()[:50]
                room.message("I found: \"%s\" by %s" % (self.getAlias(user.name), info_title, info.get_auth()[:50], link), True)
            except Exception as e:
                room.message("Something fucked up")
                print(e)


#the wall of shame command                
        if used_prefix and cmd=="wos" and user.name in open('Creator.txt') or used_prefix and cmd=="wos" and user.name() in open('OG.txt'):
                temp = open('temp.txt','w')
                temp.write(args)
                room.message("Is the message properly formatted?  EX; USERNAME: Their post :TIMESTAMP (Type ~y or ~n)")
               
        if used_prefix and cmd=="y"and user.name in open('Creator.txt') or used_prefix and cmd=="y" and user.name() in open('OG.txt'):
            tempVerified = open('temp.txt', 'r')
            testval = tempVerified.read()
            f = open('wallofshame.txt','a')
            f.write(testval)
            f.write(", ")
            f.write("\n")
            room.message("( " + testval + " ) " " has been added to the wall of shame")
        if used_prefix and cmd=="n" and user.name in open('Creator.txt') or used_prefix and cmd=="n" and user.name() in open('OG.txt'):
            room.message("Do it right next time.")
            
        if used_prefix and cmd=="wos" and user.name not in open('Creator.txt') or used_prefix and cmd=="wos" and user.name() not in open('OG.txt'):
                room.message("You don't have permission to do that . You gotta be an OG or Creator , to prevent bullshit spam and dumbass posts on this wall. ")          


#the power command
        if used_prefix and cmd=="power" and user.name.lower() in open('Creator.txt').read() and args not in open('OG.txt').read():
            p = open('OG.txt','a')
            p.write("\n")
            p.write(args)
            room.message("The Creator just made "+args+" an OG")
        
        if used_prefix and cmd=="power" and user.name.lower() in open('Creator.txt').read() and args in open('OG.txt').read(): 
            room.message("Nigga,"+args+" is already an OG")
        
        if used_prefix and cmd=="power" and user.lower() in open('OG.txt').read() and args not in open('RealNiggas.txt').read():
            j = open('RealNiggas.txt','a')
            p.write("\n")
            p.write(args)
            room.message("OG, you just made "+args+" a real nigga")
        
        if used_prefix and cmd=="power" and user.name.lower() in open('OG.txt').read() and args in open('RealNiggas.txt').read(): 
            room.message("Nigga,"+args+" is already a Real Nigga")    
        
        if used_prefix and cmd=="power" and user.name.lower() in open('RealNiggas.txt').read():    
            room.message("You have to be an OG , or Creator to do that... find one or something.")
        
        if used_prefix and cmd=="power" and user.name.lower() not in open('OG.txt').read() and user.name.lower() not in open('RealNiggas.txt').read() and user.name.lower() not in open('Creator.txt').read():
            room.message("You've got to be an OG or Creator to level anyone up , and you're not even at Real nigga yet. You're at Nig. WTF.")
#the mylevel command            
        if used_prefix and cmd=="mylevel" and user.name.lower() not in open('OG.txt').read() and user.name.lower() not in open('RealNiggas.txt').read() and user.name.lower() not in open('Creator.txt').read():
            room.message("Your level is ---> nig <--- . That means you're still ass , and you don't have as many permissions. Basic ass nigga..")
        if used_prefix and cmd=="mylevel" and user.name.lower() in open('OG.txt').read():
            room.message("Your level is ---> OG. <--- Beyond a Real nigga. Top of the hood at least. You're not a Creator but nigga you have hella rights.")
        if used_prefix and cmd=="mylevel" and user.name.lower() in open('RealNiggas.txt').read():
            room.message("Your level is ---> Real Nigga. <---  Beyond a nig.  So you made it from the bottom , but you still have work to do. Permissions limited.")
        if used_prefix and cmd=="mylevel" and user.name.lower() in open('Creator.txt').read() and user.name!="vxu":
            room.message("Your level is ---> Creator <--- . You are a developer. All permissions enabled including lethal class commands. You can assign OG's and assign Real Niggas. You are not the one who brought me to life tho.")
        if used_prefix and cmd=="mylevel" and user.name.lower() in open('Creator.txt').read() and user.name=="vxu": 
            room.message("LOL ur Dad, you know your level.")

        






                   
rooms = ["cloudromance"]

if __name__ == "__main__":
    bot.easy_start(rooms, "iterminal", "terminal")