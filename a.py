import win32api
from pyDes import *
import  base64
def ass():
    Des_Key = b"BHC#@*UM"
    Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7"
    CVolumeSerialNumber = str(win32api.GetVolumeInformation("C:\\")[1])
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(CVolumeSerialNumber)
    registencode = base64.b64encode(EncryptStr)
    registencode = registencode.decode('utf-8')
    return registencode
    # with open('注册码.txt', 'w') as f:
    #     f.write(registencode)
