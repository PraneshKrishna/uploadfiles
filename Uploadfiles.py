import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                #construct full local path
                local_path = os.path.join(root, filename)

                #construct full dropbox path
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                #upload the file
                with open(local_path,'rb')as f :
                    dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))


def main():
    access_token = 'sl.A8ZRscI35JqVfJDRYiPTWYIihXMWQUzTl7LZKzgtinyanr2OqeXSD4jANtvkaHLKbDBX9b0d7QJ0B4QHbNHtcdoGV1-kUMJy2DMFQZTnFok1Zf1hKY_9juCU_9d-IE4wVQLYolE' 
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()

    