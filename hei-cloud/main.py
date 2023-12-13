import sys
from server import CloudStorageServer

hei_cloud = CloudStorageServer(storage_limit=100, request_limit=50)


def quit():
    print("See you later!")
    sys.exit()

def menu():
    print("""
            HEI Cloud
    1. Upload a file
    2. Download a file
    3. Delete a file
    4. Quit
    """)
    choice = int(input())
    if choice == 1:
        hei_cloud.upload_file()
        menu()
    elif choice == 2:
        hei_cloud.download_file()
        menu()
    elif choice == 3:
        hei_cloud.delete_file()
        menu()
    elif choice == 4:
        quit()
    else:
        menu()

menu()
