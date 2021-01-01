class DataStoreException(Exception) :
    pass

class FileNotFoundException(DataStoreException):
    def __init__(self,message="File not found or present"):
        self.message = message
        super().__init__(self.message)

class FileNotAccesibleException(DataStoreException):
    def __init__(self,message="File Cannot Be Accessed"):
        self.message = message
        super().__init__(self.message)

class IOErrorOccurredException(DataStoreException):
    def __init__(self,message="IO Exception occured"):
        self.message = message
        super().__init__(self.message)
    
class  KeyLengthExceededException(DataStoreException):
    def __init__(self,message="Key should be a String, Enter a Valid Key"):
        self.message = message
        super().__init__(self.message)

class KeyLengthExceededException(DataStoreException):
 def __init__(self,message="Key must not have more than 32 characters"):
     self.message = message
     super().__init__(self.message)
    
class KeyAlreadyExists(DataStoreException):
    def __init__(self,key,message="Key already exists.Create a Key that does not exists already"):
        self.key= key
        self.message = message
        super().__init__(self.message)
    def __str(self):
        return f'{self.key}{self.message}'
    
class InvalidJsonObjectError(DataStoreException):
    def __init__(self,message="Value must be a Valid Json Data"):
        self.message = message
        super().__init__(self.message)

class DataSizeLimitException(DataStoreException):
    def __init__(self,message="Json Data should not exceed the size of 16KB"):
        self.message = message
        super().__init__(self.message)
    
class FileSizeLimitException(DataStoreException):
    def __init__(self,message="File size limit exceeded. No more Data can be stored."):
        self.message = message
        super().__init__(self.message)

class timeToLiveExceededException(DataStoreException):
    def __init__(self,message="Enter a valid value in numbers which defines time in seconds"):
        self.message = message
        super().__init__(self.message)

class EmptyFileException(DataStoreException):
    def __init__(self,message="File does not have any Data"):
        self.message = message
        super().__init__(self.message)

class KeyNotPresentException(DataStoreException):
    def __init__(self,key,message="Key does not exist.Enter a valid key"):
        self.message = message
        self.key = key
        super().__init__(self.message)

class ExpiredKeyException(DataStoreException):
    def __init__(self,key,message="Key exceeded Time-To-live. Key Cannot be accessed anymore for read and deletion"):
        self.message = message
        super().__init__(self.message)

class InvalidJsonFile(DataStoreException):
    def __init__(self,message="Needs a valid JSON file having valid JSON data"):
        self.message = message
        super().__init__(self.message)
    