from file import File
from error import CloudStorageInsufficient, InvalidInput, FileTooLarge, FileNotFound, ServerDown, TooManyReqeust, BadFileType, FileNameInvalid


class CloudStorageServer:
    def __init__(self, storage_limit, request_limit):
        self.storage_limit = storage_limit
        self.request_limit = request_limit
        self.current_storage = 0
        self.file_max_size = 2000
        self.current_requests = 0
        self.is_server_down = False
        self.files = []

    def upload_file(self):
        try:
            
            new_file = self.config_file()
            if self.is_server_down:
                raise ServerDown("Server is down. Please try again later.")

            if self.current_storage + new_file.size > self.storage_limit:
                raise CloudStorageInsufficient("Not enough storage space.")

            if self.current_requests >= self.request_limit:
                raise TooManyReqeust("Too many requests. Server is going down.")

            self.files.append(new_file)
            self.current_storage += new_file.size
            self.current_requests += 1

            print(f"File '{new_file.name}' uploaded successfully.")
        except CloudStorageInsufficient as e:
            print(f"Error: {e.__str__}")
        except TooManyReqeust as e:
            print(f"Error: {e.__str__}")
            self.is_server_down = True
        except ServerDown as e:
            print(f"Error: {e.__str__}")

    def delete_file(self):
        name = input("Enter file name to delete: ")
        try:
            if self.is_server_down:
                raise ServerDown("Server is down. Please try again later.")

            file_to_delete = next((file for file in self.files if file.name == name), None)
            if not file_to_delete:
                raise FileNotFound(f"File '{name}' not found.")

            self.files.remove(file_to_delete)
            self.current_storage -= file_to_delete.size
            self.current_requests += 1

            print(f"File '{name}' deleted successfully.")
        except FileNotFound as e:
            print(f"Error: {e.__str__}")
        except ServerDown as e:
            print(f"Error: {e.__str__}")

    def download_file(self):
        name = input("Enter file name to download: ")
        try:
            if self.is_server_down:
                raise ServerDown("Server is down. Please try again later.")

            file_to_download = next((file for file in self.files if file.name == name), None)
            if not file_to_download:
                raise FileNotFound(f"File '{name}' not found.")

            self.current_requests += 1

            print(f"File '{name}' downloaded successfully.")

            return file_to_download
        except FileNotFound as e:
            print(f"Error: {e.__str__}")
        except ServerDown as e:
            print(f"Error: {e.__str__}")

def config_file(self):
        name = input("Enter file name: ")

        if not all(char.isalnum() or char == '_' for char in name):
            raise FileNameInvalid(f"Invalid characters in file name: {name}")

        while True:
            try:
                size = int(input("Enter file size: "))
                if size <= 0:
                    raise InvalidInput("Invalid input. Size must be greater than 0.")
                elif size > self.file_max_size:
                    raise FileTooLarge(f"File size exceeds maximum allowed size: {self.file_max_size}")
                break
            except InvalidInput:
                print("Invalid input. Please enter a valid number.")
            except FileTooLarge:
                print("File size exceeds maximum allowed size 2000 Mb.")    

        file_type = input("Enter file type [mp4, avi, jpg, png, pdf, docx]: ")

        if file_type not in ["mp4", "avi", "jpg", "png", "pdf", "docx"]:
            raise BadFileType(f"Unsupported file type: {file_type}")

        return File(name, file_type, size)
