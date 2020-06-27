from cryptography.fernet import Fernet

file_DIR = 'very/secret/path/'

def save_file(file_name, contents, path):
    with open(path+file_name, 'wb') as my_file: #write bytes to file
        my_file.write(contents)

my_key = Fernet.generate_key()
save_file('key.key', my_key, file_DIR)

cipher = Fernet(my_key)

username = input("Please input username to encrypt")
encrypted_username = cipher.encrypt(username.encode('utf-8')) # bytes
save_file('user.txt', encrypted_username, file_DIR+'enc/')

password = input("Please input password to encrypt")
encrypted_password = cipher.encrypt(password.encode('utf-8'))
save_file('pass.txt', encrypted_password, file_DIR+'enc/')
