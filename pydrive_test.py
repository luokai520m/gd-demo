from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import socket
import socks
socket.setdefaulttimeout(150)
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1081)
socket.socket = socks.socksocket

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

textfile = drive.CreateFile()
textfile.SetContentFile('eng.txt')
textfile.Upload()
print(textfile)

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload() # Files.insert()

file1['title'] = 'HelloWorld.txt'  # Change title of the file
file1.Upload() # Files.patch()

content = file1.GetContentString()  # 'Hello'
file1.SetContentString(content+' World!')  # 'Hello World!'
file1.Upload() # Files.update()

# file2 = drive.CreateFile()
# file2.SetContentFile('hello.png')
# file2.Upload()
# print('Created file %s with mimeType %s' % (file2['title'],
# file2['mimeType']))
# # Created file hello.png with mimeType image/png

# file3 = drive.CreateFile({'id': file2['id']})
# print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
# file3.GetContentFile('world.png')  # Save Drive file as a local file

# # or download Google Docs files in an export format provided.
# # downloading a docs document as an html file:
# docsfile.GetContentFile('test.html', mimetype='text/html')


drive.CreateFile({'id':textfile['id']}).GetContentFile('eng-dl.txt')