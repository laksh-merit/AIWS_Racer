from flask import Flask
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive( gauth )
app = Flask(__name__)
if __name__ == '__main__':
    while True:
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format( '1r0V3vOheKCTNqkXFQeN2ROfdDj8X2juZ' )} ).GetList()
        if( len( file_list ) >0 ):
            # download files from google drive
            for i, file in enumerate( sorted( file_list, key=lambda x: x['title'] ), start=1 ):
                print( 'Downloading {} file from GDrive ({}/{})'.format( file['title'], i, len( file_list ) ) )
                file.GetContentFile( 'client/' + file['title'] )
                id = file['id']
                file2 = drive.CreateFile( {'id': id} )
                file2.Delete()
                break
            continue
        else:
            continue
