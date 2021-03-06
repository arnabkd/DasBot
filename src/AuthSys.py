#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Skrevet av Sindre Wetjen
from User import User

class AuthSys:

    def __init__(self, secret):
        self.secret = secret
        self.userlist = {}
        self.domainlist = {}

    def add(self, nick, email, level = 0):
        if len(self.userlist.keys()) == 0:
            level = 100
        try:
            self.userlist[nick] = User(nick, email, self.secret, level)
        except:
            return "I got an error in registering. Please try again"
        
    def login(self, nick, passwd, domain):
        if (nick in self.userlist) and self.userlist[nick].login(passwd, domain, self.secret):
            self.domainlist[domain] = self.userlist[nick]
            return True
        return False

    def online(self, domain):
        return domain in self.domainlist
    
    def level(self, domain):
        if domain in self.domainlist:
           return self.domainlist[domain].get_level()

    def list_users(self):
        return str(self.userlist.keys())

    def logout(self, domain):
        if domain in self.domainlist:
            self.domainlist[domain].logout()
            del self.domainlist[domain]
