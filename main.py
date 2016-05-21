#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''                     # primjer klase
class KPPoziv(object): 
    """ Class desc """
    #varijable klase
    #...
    
    def __init__(self, data): # u init se predaju podatci koje predajemo klasi kod inicijalizacije
        """data je kratke_Poruke.grouped_by_call polje poruka"""
        self.loadKratkePoruke(data)
        
    def loadKratkePoruke(self,kratke_Poruke):
        self.listaKPoruka = kratke_Poruke
        self.initvars()
        self.createSekvenca()
        self.userCallDuration() #ako je sekvenca  180-200-ACK-BYE  od 200OK do zadnje poruke
        self.checkCall()  #regex na sekvenci
        '''
        
## imports
import os
import sys
from datetime import datetime
from input import getUserInput
from scrapercalz import openMECH
## globals
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = ABS_PATH+"/"
LOG_PATH = SCRIPT_PATH+"log.log"  

#########################  definitions  #########################
def writelog(logMsg):
    FDEVNULL  = open(LOG_PATH, 'a+')
    timenow = datetime.now()
    msg = str(timenow)+" - "+str(logMsg)+"\n"
    FDEVNULL.write(msg)
    FDEVNULL.close()
    
class Xtraktor(object): 
    """ Class desc """
    #varijable klase
    #...
    
    def __init__(self):
        """ pokrece glavnu xtraktor logiku """
        self.getInput()
        self.callMechanize()
    
    def getInput(self):
        self.websiteurl = getUserInput() #from input
    
    def callMechanize(self):
        mechreturn = openMECH(self.websiteurl)
        print mechreturn
        
        
#########################  PROGRAM STARTING  #########################
if __name__ == "__main__":
    """  Main """
    
    xtraktor = Xtraktor() # kreirali smo objekt xtraktor klase Xtraktor. xtraktor je napravljen po klasi Xtraktor
    



















