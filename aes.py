from Crypto.Cipher import AES
import scrypt, os, binascii

def encrypt(msg, password):
    kdfSalt = os.urandom(16)
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    #cipherblock = [binascii.hexlify(kdfSalt),binascii.hexlify(secretKey),binascii.hexlify(aesCipher),binascii.hexlify(ciphertext)]
    return [binascii.hexlify(kdfSalt),binascii.hexlify(ciphertext),binascii.hexlify(aesCipher.nonce),binascii.hexlify(authTag)]

def decrypt(encryptedMsg, password):
    kdfSalt = binascii.unhexlify(encryptedMsg[0])
    ciphertext = binascii.unhexlify(encryptedMsg[1])
    nonce = binascii.unhexlify(encryptedMsg[2])
    authTag = binascii.unhexlify(encryptedMsg[3])
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext
