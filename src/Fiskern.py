# -*- coding: utf-8 -*-
import AuthBot
import time
from GlobalConfig import *
from IRCFonts import *

class Fiskern(AuthBot.AuthBot):
        
    def __init__(self, host, port, nick, ident, realname):
        super(Fiskern, self).__init__(host, port, nick, ident, realname)

    def cmd(self, command, args, channel, **kwargs):
        super(Fiskern, self).cmd(command, args, channel, **kwargs)        
        if VERBOSE: print "COMMAND FISKERN!"

        if command == "insult":
            self.msg(channel, "e du fette sprø i haue? æ ork da faen ikkje å ta mæ ti tel å lag sånnhærre tullekommandoa!", to=kwargs["from_nick"])
        elif command == "tell":
            self.private_msg(kwargs["from_nick"], "emanuel is lazy")
        elif command == "whos":
            self.msg(channel, str(self.channel[channel][args]) if args in self.channel[channel] else "Not legal key", to=kwargs['from_nick'])
        elif command == "notifyall":
            output = ""
            for key in self.channel[channel]:
                for user in self.channel[channel][key]:
                    output += user + " "
            self.msg(channel, output)
            self.msg(channel, "se tell hælvette å føll me hær!")

        elif command == "topic":
            if args:
                self.topic(channel, args)
            else:
                self.topic(channel, "Der hammermäßige IRC Bot der Computerlinguisten")

        elif command == "nick":
            self.nick(args)
            
    def listen(self, command, msg, channel, **kwargs):
        super(Fiskern, self).listen(command, msg, channel, **kwargs)
        if VERBOSE: print "LISTEN FISKERN!"
        if kwargs['from_nick'] == 'emanuel':
            self.msg(channel, "bipeti bapeti!", to="emanuel")
        if msg.find("!insult") != -1:
            self.msg(channel, "please !insult %s" % (kwargs["from_nick"]))

if __name__ == "__main__":
    HOST='irc.ifi.uio.no' #The server we want to connect to 
    PORT=6667 #The connection port which is usually 6667 
    NICK='Fiskern' #The bot's nickname 
    IDENT='Fiskern' #The bot's identity
    REALNAME='Ola Nordlenning' #REAL NAME, sort of.
    OWNER='Subfusc' #The bot owner's nick 
    
    bot = Fiskern(HOST, PORT, NICK, IDENT, REALNAME)
    bot.connect()
    bot.join("#nybrummbot")
    bot.msg("#nybrummbot", "%s e som å lig i fjorn %s på en %s!"% (bold("Ingenting"), reverse("å fesk"), underline("fin sommardag")))
    #bot.msg("#nybrummbot", "Dæsken så mye fesk det e i fjorn i dag!")
    bot.notify("Subfusc", "hør du ette eller?")
    bot.start()

    
