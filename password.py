from cryptography.fernet import Fernet

fileDir = 'very/secret/path/'

def save_file(fileName, contents, path):
    with open(path+fileName, 'wb') as myFile: #write bytes to file
        myFile.write(contents)

myKey = Fernet.generate_key()
save_file('key.key', myKey, fileDIR)

cipher = Fernet(myKey)

username = input("Please input username to encrypt")
encryptedUsername = cipher.encrypt(username.encode('utf-8')) # bytes
save_file('user.txt', encryptedUsername, fileDIR+'enc/')

password = input("Please input password to encrypt")
encryptedPassword = cipher.encrypt(password.encode('utf-8'))
save_file('pass.txt', encryptedPassword, fileDIR+'enc/')
