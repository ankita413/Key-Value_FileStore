 # pylint: disable=no-member
import threading
from threading import Lock
import time
import os  #os contains functions for interacting with os
import json
from Exceptions import *

class dataStore:
    def __init__(self,filePath = None):
        self.filePath = filePath
        self._lock = Lock()
        if self.filePath:
            if not os.access(self.filePath, os.F_OK): raise FileNotFoundException
            elif not os.access(self.filePath, os.R_OK): raise FileNotAccesibleException
            try:
                with open(self.filePath): pass
            except IOError : raise IOErrorOccurredException
        else:
            self.filePath = os.getcwd() + '\\dataStore.json'

        with open(self.filePath,'a+') : pass
        self.filePath = os.stat(self.filePath).st_size

        @staticmethod
        def checkKeyLength(self): 
            if len(self.key)>32 : raise KeyLengthExceededException

        def createData(self,key,value,timeToLive = None):
            self.key = key
            self.value = value
            self.timeToLive = timeToLive
            self.value_size = self.value.__sizeof__()
            self.checkKeyLength

            try : json.loads(self.value)
            except json.JSONDecodeError: raise InvalidJsonObjectError
            with self._lock:
                self.fileSize = os.stat(self.filePath).st_size
                if self.value_size > (1024*16):
                    raise DataSizeLimitException
                elif (self.value_size + self.fileSize)/1024 >  (1024*1024):
                    raise FileSizeLimitException

                if self.timeToLive:
                    try:self.timeToLive = int(self.timeToLive)
                    except: raise timeToLiveExceededException
                   
                    if type(self.timeToLive) is not int : pass
                    self.time = int(time())
                else : self.time = None
        with open(self.filePath,'r+') as self.dataStorPtr :
            self.data = {self.key : (self.value,self.timeToLive,self.time)}

            if self.fileSize is 0:
                self.dataStorPtr.write(json.dumps(self.data,indent=4))
            else: 
                try: self.data_Store= json.load(self.dataStorPtr)
                except json.JSONDecodeError: raise InvalidJsonFile

                if self.key in self.data_Store : raise KeyAlreadyExists(self.key)
                else: 
                    try: self.data_Store.update(self.data)
                    except AttributeError : raise InvalidJsonFile

                    self.dataStorPtr.seek(0)
                    json.dump(self.data_Store,self.dataStorPtr)

    def readData(self,key):
        with self._lock:
            self.fileSize = os.stat(self.filePath).st_size
            self.key = key = key
            self.checkKeyLength
            if self.fileSize is 0 : raise EmptyFileException
            with open(self.filePath,'r') as self.dataStorPtr:
                try:self.data_Store = json.load(self.dataStorPtr)
                except json.JSONDecodeError: raise InvalidJsonFile
                if self.key not in self.data_Store: raise KeyNotPresentException(self.key)
                else: 
                    self.data = self.data_Store[self.key]
                    try:self.ValidTTL = (int(time()) - self.data[2] < self.data[1])
                    except: raise InvalidJsonFile
                    if self.ValidTTL :  return json.dumps(self.data[0])
                    else: raise ExpiredKeyException(self.key)

    def deleteData(self,key):
        with self._lock:
            self.fileSize = os.stat(self.filePath).st_size
            self.key = key
            self.checkKeyLength
            if self.fileSize is 0 : raise EmptyFileException
            with open(self.filePath,'r+') as self.dataStorPtr :
                try: self.data_Store = json.load(self.dataStorPtr)
                except json.JSONDecodeError: raise InvalidJsonFile

            if self.key not in self.data_Store : raise KeyNotPresentException(self.key)
            else:
                self.data = self.data_Store[self.key]
                try: self.ValidTTL = (int (time()) - self.data[2])< self.data[1]
                except: raise InvalidJsonFile
                if self.ValidTTL:  
                    del self.data_Store[self.key]
                    os.remove(self.filePath)
                else:
                    raise ExpiredKeyException(self.key)
            with open(self.filePath,'w') as self.dataStorPtr :
                json.dump(self.data_Store,self.dataStorPtr)
