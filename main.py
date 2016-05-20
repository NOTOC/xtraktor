#!/usr/bin/env python
# -*- coding: utf-8 -*-

## imports
import os
import sys
from datetime import datetime
## globals
LOG_PATH = SCRIPT_PATH+"log.log"  

## functions
def writelog(logMsg):
    FDEVNULL  = open(LOG_PATH, 'a+')
    timenow = datetime.now()
    msg = str(timenow)+" - "+str(logMsg)+"\n"
    FDEVNULL.write(msg)
    FDEVNULL.close()
    
class KPPoziv(object):
    """ Class desc """
    #varijable klase
    #...
    
    def __init__(self, data):
        """data je kratke_Poruke.grouped_by_call polje poruka"""
        self.loadKratkePoruke(data)
        
    def loadKratkePoruke(self,kratke_Poruke):
        self.listaKPoruka = kratke_Poruke
        self.initvars()
        self.createSekvenca()
        self.userCallDuration() #ako je sekvenca  180-200-ACK-BYE  od 200OK do zadnje poruke
        self.checkCall()  #regex na sekvenci
    
    

if __name__ == "__main__":
    from excel import Excel
    """  Main """
    



















