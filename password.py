from cryptography.fernet import Fernet

fileDir = 'very/secret/path/'

def save_file(fileName, contents, path):
    with open(path+fileName, 'wb') as myFile: #write bytes to file
        myFile.write(contents)

myKey = Fernet.generate_key()
save_file('key.key', myKey, fileDir)
