class CloudStorageException(Exception):
    def __str__(self):
        return f"code: {self.code} message: {self.message}"


class CloudStorageInsufficient(CloudStorageException):
    def __init__(self, message="The cloud storage limit was reached.", code=507):
        self.message = message
        self.code = code


class FileNotFound(CloudStorageException):
    def __init__(self, message="File not found", code=404):
        self.message = message
        self.code = code


class ServerDown(CloudStorageException):
    def __init__(self, message="We are under maintenance.", code=503):
        self.message = message
        self.code = code

class TooManyReqeust(CloudStorageException):
    def __init__(self, message="Too many request. The server can't follow.", code=429):
        self.message = message
        self.code = code

class BadFileType(CloudStorageException):
    def __init__(self, message="File type not supported", code=400):
        self.message = message
        self.code = code

class FileNameInvalid(CloudStorageException):
    def __init__(self, message="Invalid file name. Must only contain alphanumeric and underscore.", code=400):
        self.message = message
        self.code = code

class FileTooLarge(CloudStorageException):
    def __init__(self, message="File is too large. Must not exceed 2000 Mb", code=413):
        self.message = message
        self.code = code

class InvalidInput(CloudStorageException):
    def __init__(self, message="Invalid input", code=400):
        self.message = message
        self.code = code