import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import *
import base64,base58,base36,base62,base91
import urllib.parse
import requests
import string
import html
import random
import time
import os
version = '1.0'
update_time = '2022.2.22'
class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 600, 640)
        self.setWindowTitle('ctftools-decode_or_encode' + version + ' ' + update_time + '  By chrislyy ')
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.label_in = QLabel('输入加解密文')
        self.label_out = QLabel('输出结果')
        self.text_in = QTextEdit()
        self.text_out = QTextEdit()
        self.comboBox_1 = QComboBox()
        self.comboBox_1.addItems(['选择待加解密类型','base16','base32' , 'base64','base36','base58','base62','base85','base91',
                                  'rot13','凯撒','培根','栅栏','云影','键盘Qwerty','摩斯','当铺','维吉尼亚','埃特巴什码',
                                  '字符串--二进制','字符串--八进制','字符串--十六进制','字符串--十进制',
                                  'url-utf8','url-gb2312','unicode','htmlcode',
                                  'jsfuck','brainfuck','Ook','shortOok','printable','与佛论禅','词频分析'])
        self.btn1 = QPushButton('传入文本')
        self.btn2 = QPushButton('开始解密')
        self.btn3 = QPushButton('开始加密')
        self.btn4 = QPushButton('清空输入')
        self.De_Or_En_type = ''
        self.weiyi = ''
        self.n = ''
        self.key = ''
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        for btn in (self.btn1, self.btn2,self.btn3):
            h1.addWidget(btn)
        for label in (self.label_out, self.btn4):
            h2.addWidget(label)
        layout = QVBoxLayout()
        layout.addWidget(self.label_in)
        layout.addWidget(self.text_in)
        #layout.addWidget(self.label_out)
        layout.addLayout(h2)
        layout.addWidget(self.text_out)
        layout.addWidget(self.comboBox_1)
        layout.addLayout(h1) 
        self.label_in.setMinimumSize(150, 30)
        self.label_out.setMinimumSize(150, 30)
        self.label_in.setFont(QFont("微软雅黑", 10, QFont.Bold))
        self.label_out.setFont(QFont("微软雅黑", 10, QFont.Bold))
        self.label_in.setStyleSheet(
            "QLabel{margin-left:15px}"
            "QLabel{margin-right:450px}")
        self.label_out.setStyleSheet(
            "QLabel{margin-left:15px}"
            "QLabel{margin-right:300px}")
        self.text_in.setStyleSheet("QTextEdit{font:16px}"
                                   "QTextEdit{margin-left:15px}"
                                   "QTextEdit{margin-right:15px}")
        self.text_out.setStyleSheet("QTextEdit{font:16px}"
                                    "QTextEdit{margin-left:15px}"
                                    "QTextEdit{margin-right:15px}")
        self.comboBox_1.setStyleSheet("QComboBox{color:black}"
                                      "QComboBox:hover{color:red}"
                                      "QComboBox{background-color:rgb(176,224,230)}"
                                      "QComboBox{border-radius:2px}"
                                      "QComboBox{padding:5px 200px }"
                                      "QComboBox{margin:2px 20px}"
                                      "QComboBox{font:20px}"
                                )
        self.btn1.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px }"
                                "QPushButton{font:18px}"
                                )
        self.btn2.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px }"
                                "QPushButton{font:18px}"
                                )
        self.btn3.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px }"
                                "QPushButton{font:18px}"
                                )
        self.btn4.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:16px}"
                                )
        self.btn1.setMinimumHeight(40)
        self.btn2.setMinimumHeight(40)
        self.btn3.setMinimumHeight(40)
        self.btn4.setMinimumHeight(30)
        self.setLayout(layout)
        self.btn1.clicked.connect(self.Get_strings)
        self.btn2.clicked.connect(self.Decode)
        self.btn3.clicked.connect(self.Encode)
        self.btn4.clicked.connect(self.Clear)
    def Get_strings(self):
        try:
            gettext = self.text_in.toPlainText()
            if gettext == '':
                self.text_in.setText('请输入待加解密字符串！')
                return 0
            else:
                self.De_Or_En_type = self.comboBox_1.currentText()
                return self.De_Or_En_type
        except Exception as e:
            self.text_in.setText('error:' + str(e))
            pass
    def Decode(self):
        try:
            result_text = ''
            text = self.text_in.toPlainText()
            if text == '':
                self.text_in.setText('请输入待加解密字符串！')
                return 0
            result = self.Get_strings()
            if result == 'base16':
                text = base64.b16decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base16:' + result_text)
            elif result == 'base32':
                text = base64.b32decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base32:' + result_text)
            elif result == 'base64':
                text = base64.b64decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base64:' + result_text)
            elif result == 'base36':
                c = base36.dumps(int(text))
                self.text_out.setText('base36:' + c)
            elif result == 'base58':
                text = base58.b58decode(text.encode('utf-8'))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base58:' + result_text)
            elif result == 'base62':
                c = base62.decode(str(text))
                self.text_out.setText('base62:' + str(c))
            elif result == 'base85':
                c = base64.a85decode(str(text)).decode()
                self.text_out.setText('base85:'+ str(c))
            elif result == 'base91':
                c = base91.decode(str(text)).decode()
                self.text_out.setText('base91:' + str(c))
            elif result == 'rot13':
                dict = {
                    "a": "n", "b": "o", "c": "p", "d": "q", "e": "r",
                    "f": "s", "g": "t", "h": "u", "i": "v", "j": "w",
                    "k": "x", "l": "y", "m": "z", "n": "a", "o": "b",
                    "p": "c", "q": "d", "r": "e", "s": "f", "t": "g",
                    "u": "h", "v": "i", "w": "j", "x": "k", "y": "l",
                    "z": "m", "A": "N", "B": "O", "C": "P", "D": "Q",
                    "E": "R", "F": "S", "G": "T", "H": "U", "I": "V",
                    "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A",
                    "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F",
                    "T": "G", "U": "H", "V": "I", "W": "J", "X": "K",
                    "Y": "L", "Z": "M"
                }
                result_text = "".join(dict.get(c, c) for c in text)
                self.text_out.setText('rot13:' + result_text)
            elif result == '凯撒':
                inputStr = text
                result = ''
                for j in range(26):
                    result_list = []
                    for i, num in zip(inputStr, range(len(inputStr))):
                        if i.islower:
                            caseS1 = string.ascii_lowercase * 2
                        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                            caseS1 = string.ascii_uppercase * 2
                        status = caseS1.find(i)
                        if status != -1:
                            result_list.append(caseS1[status + j])
                        else:
                            result_list.append(inputStr[num])
                    text2 = ("".join(result_list), "  向右偏移了{}位".format(j))
                    result += text2[0] + ' ' + text2[1] + '\n'
                result_text = result
                self.text_out.setText('凯撒密码:\n' + result_text)
            elif result == '培根':
                return_str = ''
                dicts = {'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y',
                         'abbab': 'N',
                         'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F',
                         'aabaa': 'E',
                         'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D',
                         'abbbb': 'P',
                         'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
                sums = len(text)
                j = 5  
                for i in range(int(sums / j)):
                    result = text[j * i:j * (i + 1)].lower()
                    return_str += str(dicts[result])
                result_text = return_str
                self.text_out.setText('培根密码:' + result_text)
            elif result == '栅栏':
                for n in range(2, text.__len__() - 1):
                    ans = ''
                    for i in range(n):
                        for j in range(int(text.__len__() / n + 0.5)):
                            try:
                                ans += text[j * n + i]
                            except:
                                pass
                    result_text += "分为%s栏，解密结果为:%s\n" % (n, ans)
                    self.text_out.setText('栅栏密码:\n' + result_text)
            elif result == '云影':
                charList = [chr(i) for i in range(ord('a'), ord('z') + 1)]
                ret = []
                plaintext = [i for i in text.split('0')]
                for i in plaintext:
                    tmp = 0
                    for j in range(len(i)):
                        tmp += int(i[j])
                    ret.append(charList[tmp - 1])
                result_text = ''.join(ret)
                self.text_out.setText('云影密码:' + result_text)
            elif result == '键盘Qwerty':
                dict = {
                    'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g',
                    'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n',
                    'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
                    'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z',
                    'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G',
                    'I': 'H', 'O': 'I', 'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N',
                    'G': 'O', 'H': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'Z': 'T',
                    'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X', 'N': 'Y', 'M': 'Z',
                }
                result_text = ''
                for i in range(0, len(text)):
                    if text[i] != ' ':
                        result_text = result_text + dict.get(text[i])
                    else:
                        result_text = result_text + ' '
                self.text_out.setText('键盘Qwerty密码:' + result_text)
            elif result == '摩斯':
                dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                        '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                        '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                        '..--..': '?', '-..-.': '/', '-.--.-': '()', '-....-': '-',
                        '.-.-.-': '.'
                        }
                msg = ''
                s = text.split(' ')
                for item in s:
                    if item != '' and item != ' ':
                        msg += (dict[item])
                result_text = msg
                self.text_out.setText('摩斯密码:' + result_text)
            elif result == '当铺':
                result_text = ''
                dict = {'田': 0, '由': 1, '中': 2, '人': 3, '工': 4, '大': 5, '王': 6, '夫': 7, '井': 8, '羊': 9}
                for item in text:
                    result_text += str((dict[item]))
                self.text_out.setText('当铺密码:' + result_text)
            elif result == '维吉尼亚':
                try:
                    value, ok = QInputDialog.getText(self, "添加key", "请输入key(字母):", QLineEdit.Normal, "请输入key(字母)")
                    self.key = value
                    Flag=False
                    for i in self.key:
                        if i.isalpha():
                            continue
                        else:
                            Flag=True
                    letter_list = string.ascii_uppercase
                    letter_list2 = string.ascii_lowercase
                    if Flag:
                        self.text_out.setText('key只能为字母组成!')
                        return
                    if len(self.key) == 0:
                        self.text_out.setText('请输入一个合法的key!')
                        return
                    key_list = []
                    for i in self.key:
                        key_list.append(ord(i.upper()) - 65)
                    plaintext = ""
                    flag = 0
                    for cipher in text:
                        if flag % len(key_list) == 0:
                            flag = 0
                        if cipher.isalpha():
                            if cipher.isupper():
                                plaintext += letter_list[(ord(cipher) - 65 - key_list[flag]) % 26]
                                flag += 1
                            if cipher.islower():
                                plaintext += letter_list2[(ord(cipher) - 97 - key_list[flag]) % 26]
                                flag += 1
                        else:
                            plaintext += cipher
                    if plaintext != '':
                        self.text_out.setText('维吉尼亚密码:' + plaintext)
                    else:
                        self.text_out.setText('解密失败！')
                except Exception as e:
                    self.text_out.setText(str(e))
            elif result == '埃特巴什码':
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                for s in text:
                    if s != ' ':
                        result_text = result_text + str2[str1.index(s)]
                    else:
                        result_text = result_text + ' '
                self.text_out.setText('埃特巴什码:' + result_text)
            elif result == '字符串--二进制':
                s = text.split(' ')
                result_text = ''
                for item in s:
                    a = int(item, 2)
                    result_text += chr(a)
                self.text_out.setText('二进制转字符串:' + result_text)
            elif result == '字符串--八进制':
                s = text.split(' ')
                result_text = ''
                for item in s:
                    a = int(item, 8)
                    result_text += chr(a)
                self.text_out.setText('八进制转字符串:' + result_text)
            elif result == '字符串--十六进制':
                s = text.split(' ')
                result_text = ''
                for item in s:
                    a = int(item, 16)
                    result_text += chr(a)
                self.text_out.setText('十六进制转字符串:' + result_text)
            elif result == '字符串--十进制':
                s = text.split(' ')
                result_text = ''
                for item in s:
                    a = int(item,10)
                    result_text += chr(a)
                self.text_out.setText('十进制转字符串:' + result_text)
            elif result == 'url-utf8':
                result_text = str(urllib.parse.unquote(text))
                self.text_out.setText('url-utf8:' + result_text)
            elif result =='url-gb2312':
                result_text = str(urllib.parse.unquote(text, 'gb2312'))
                self.text_out.setText('url-gb2312:' + result_text)
            elif result =='unicode':
                result_text = text.encode('utf8').decode('unicode_escape')
                self.text_out.setText('unicode:' + result_text)
            elif result == 'htmlcode':
                result_text = html.unescape(text)
                self.text_out.setText('htmldecode:' + result_text)
            elif result =='jsfuck' :
                result_text = '<a href="http://www.jsfuck.com/">http://www.jsfuck.com/</a>'
                self.text_out.setText('jsfuck，其在线解密网址:' + result_text)
            elif result == 'brainfuck' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText('brainfuck，其在线解密网址:' + result_text )
            elif result == 'Ook' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    'Ook(若待解码的文本出现了O,o,k），其在线解密网址:' + result_text )
            elif result =='shortOok' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    'shortOok(若待解码的文本中无O,o,k)其在线解密网址:' + result_text )
            elif result =='printable':
                result_text = '<a href="http://www.mxcz.net/tools/quotedprintable.aspx">http://www.mxcz.net/tools/quotedprintable.aspx</a>'
                self.text_out.setText('Quoted-Printable，其在线解密网址:' + result_text)
            elif result =='与佛论禅' :
                result_text = '<a href="http://www.keyfc.net/bbs/tools/tudoucode.aspx">http://www.keyfc.net/bbs/tools/tudoucode.aspx</a>'
                result_texts = '<a href="http://hi.pcmoe.net/buddha.html">http://hi.pcmoe.net/buddha.html</a>'
                self.text_out.setText(
                    '与佛论禅，其在线解密网址:' + result_text + '\n新与佛论禅，其在线解密网址:'+ result_texts )
            elif result =='词频分析':
                result_text = '<a href="http://quipqiup.com/">http://quipqiup.com/</a>'
                self.text_out.setText(
                    '英文字符数挺多，毫无章法，试试词频分析吧，其在线解密网址:' + result_text )
            else:
                self.text_out.setText('解密错误，请再核对解密类型！')
        except Exception as e:
            self.text_in.setText('error:' + str(e))
            pass
    def sto10(self):
        tmp = []
        text = self.text_in.toPlainText()
        for c in text:
            tmp.append((ord(c)))
        result_text = str(tmp)
        return result_text
    def Encode(self):
        try:
            result_text = ''
            text = self.text_in.toPlainText()
            if text == '':
                self.text_in.setText('请输入待加解密字符串！')
                return 0
            result = self.Get_strings()
            if result == 'base16':
                text = base64.b16encode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base16:' + result_text)
            elif result == 'base32':
                text = base64.b32encode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base32:' + result_text)
            elif result == 'base64':
                text = base64.b64encode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base64:' + result_text)
            elif result == 'base36':
                result_text = str(base36.loads(text))
                self.text_out.setText('base36:' + result_text)
            elif result == 'base58':
                text = base58.b58encode(text.encode('utf-8'))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base58:' + result_text)
            elif result == 'base62':
                c = base62.encode(int(text))
                self.text_out.setText('base62:' + str(c))
            elif result == 'base85':
                c = base64.a85encode(text.encode('utf-8')).decode()
                self.text_out.setText('base85:'+ str(c))
            elif result == 'base91':
                c = base91.encode(text.encode('utf-8'))
                self.text_out.setText('base91:' + str(c))
            elif result == 'rot13':
                d = {chr(i + c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
                result_text = ''.join([d.get(c, c) for c in text])
                self.text_out.setText('rot13:' + str(result_text))
            elif result =='凯撒':
                value, ok = QInputDialog.getText(self, "添加位移", "请输入位移位数:", QLineEdit.Normal, "请输入数字")
                self.weiyi = value
                Flag = False
                for i in self.weiyi:
                    if i.isdigit():
                        continue
                    else:
                        Flag = True
                if Flag:
                    self.text_out.setText('位移数只能为数字!')
                    return
                if len(self.weiyi) == 0:
                    self.text_out.setText('请输入位移数!')
                    return
                self.weiyi = int(value)
                t = ""
                for c in text:
                    if 'a' <= c <= 'z': 
                        t += chr(ord('a') + ((ord(c) - ord('a')) + self.weiyi) % 26)
                    elif 'A' <= c <= 'Z':
                        t += chr(ord('A') + ((ord(c) - ord('A')) + self.weiyi) % 26)
                    else:
                        t += c
                result_text = t
                self.text_out.setText('凯撒密码:' + result_text)
            elif result == '培根':
                dicts = {  
                    'aaaaa': 'a', 'aaaab': 'b', 'aaaba': 'c', 'aaabb': 'd', 'aabaa': 'e', 'aabab': 'f', 'aabba': 'g',
                    'aabbb': 'h', 'abaaa': 'i', 'abaab': 'j', 'ababa': 'k', 'ababb': 'l', 'abbaa': 'm', 'abbab': 'n',
                    'abbba': 'o', 'abbbb': 'p', 'baaaa': 'q', 'baaab': 'r', 'baaba': 's', 'baabb': 't', 'babaa': 'u',
                    'babab': 'v', 'babba': 'w', 'babbb': 'x', 'bbaaa': 'y', 'bbaab': 'z'
                }
                dict = text.lower()
                listStr = ''
                for i in dict:
                    if i in dicts.values():
                        listStr += list(dicts.keys())[list(dicts.values()).index(i)]
                result_text = listStr.upper()  
                self.text_out.setText('培根密码:' + result_text)
            elif result == '栅栏':
                value, ok = QInputDialog.getText(self, "添加栏数", "请输入分栏栏数:", QLineEdit.Normal, "请输入数字")
                self.n = value
                Flag = False
                for i in self.n:
                    if i.isdigit():
                        continue
                    else:
                        Flag = True
                if Flag:
                    self.text_out.setText('栏数只能为数字!')
                    return
                if len(self.n) == 0:
                    self.text_out.setText('请输入分栏数!')
                    return
                self.n=int(self.n)
                try:
                    ans = ''
                    for i in range(self.n):
                        for j in range(int(text.__len__() / self.n + 0.5)):
                            try:
                                ans += text[j * self.n + i]
                            except:
                                pass
                except:
                    ans = "请输入正确的分栏！"
                if ans != '':
                    self.text_out.setText('栅栏密码:' + ans)
                else:
                    self.text_out.setText('加密失败!')
            elif result == '云影':
                charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                cipher = [i for i in text.upper()]
                tmp = []
                ret = []
                for i in range(len(cipher)):
                    for j in range(len(charList)):
                        if charList[j] == cipher[i]:
                            tmp.append(j + 1)
                for i in tmp:
                    res = ''
                    if i >= 8:
                        for j in range(0, int(i / 8)):
                            res += '8'
                    if i % 8 >= 4:
                        for j in range(0, int(i % 8 / 4)):
                            res += '4'
                    if i % 4 >= 2:
                        for j in range(0, int(i % 4 / 2)):
                            res += '2'
                    if i % 2 >= 1:
                        for j in range(0, int(i % 2 / 1)):
                            res += '1'
                    ret.append(res + '0')
                result_text = ''.join(ret)[:-1]
                self.text_out.setText('云影密码:' + result_text)
            elif result == '键盘Qwerty':
                str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                result_text = ""
                for s in text:
                    if s in str1:
                        if s != ' ':
                            result_text = result_text + str1[str2.index(s)]
                        else:
                            result_text = result_text + ' '
                    else:
                        self.text_out.setText('Qwerty只能对字母加密!')
                self.text_out.setText('键盘Qwerty密码:' + result_text)
            elif result == '摩斯':
                dicts = {'A': '.-', 'B': '-...', 'C': '-.-.',
                        'D': '-..', 'E': '.', 'F': '..-.',
                        'G': '--.', 'H': '....', 'I': '..',
                        'J': '.---', 'K': '-.-', 'L': '.-..',
                        'M': '--', 'N': '-.', 'O': '---',
                        'P': '.--.', 'Q': '--.-', 'R': '.-.',
                        'S': '...', 'T': '-', 'U': '..-',
                        'V': '...-', 'W': '.--', 'X': '-..-',
                        'Y': '-.--', 'Z': '--..',
                        '0': '-----', '1': '.----', '2': '..---',
                        '3': '...--', '4': '....-', '5': '.....',
                        '6': '-....', '7': '--...', '8': '---..',
                        '9': '----.', '?': '..--..', '/': '-..-.',
                        '()': '-.--.-', '-': '-....-', '.': '.-.-.-'
                        }
                msg = ''
                for char in text.upper():
                    if char in dicts:
                        if char == ' ':
                            pass
                        else:
                            msg += (dicts[char.upper()] + ' ')
                    else:
                        msg = '文本中含有不能识别的字符！'
                result_text = msg
                self.text_out.setText('摩斯密码:' + result_text)
            elif result == '当铺':
                mapping_data = [['田'], ['由'], ['中'], ['人'], ['工'], ['大'], ['王'], ['夫'], ['井'], ['羊']]
                try:
                    result = []
                    for c in text:
                        c_list = mapping_data[int(c)]
                        c_index = random.randint(0, len(c_list) - 1)
                        result.append(c_list[c_index])
                    result_text = ''.join(result)
                except:
                    result_text = '未找到该字符串对应的中文！'
                self.text_out.setText('当铺密码:' + result_text)
            elif result == '维吉尼亚':
                try:
                    value, ok = QInputDialog.getText(self, "添加key", "请输入key(字母):", QLineEdit.Normal, "请输入key(字母)")
                    self.key = value
                    Flag=False
                    for i in self.key:
                        if i.isalpha():
                            continue
                        else:
                            Flag=True
                    if Flag:
                        self.text_out.setText('key只能为字母组成!')
                        return
                    if len(self.key) == 0:
                        self.text_out.setText('请输入一个合法的key!')
                        return
                    ptLen = len(text)
                    keyLen = len(self.key)
                    quotient = ptLen // keyLen  
                    remainder = ptLen % keyLen  
                    for i in range(0, quotient):
                        for j in range(0, keyLen):
                            c = int((ord(text[i * keyLen + j]) - ord('a') + ord(self.key[j]) - ord('a')) % 26 + ord('a'))
                            result_text += chr(c)
                    for i in range(0, remainder):
                        c = int((ord(text[quotient * keyLen + i]) - ord('a') + ord(self.key[i]) - ord('a')) % 26 + ord('a'))
                        result_text += chr(c)
                    if result_text != '':
                        self.text_out.setText('维吉尼亚密码:' + result_text)
                    else:
                        self.text_out.setText('加密失败')
                except Exception as e:
                    self.text_out.setText(str(e))
            elif result == '埃特巴什码':
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                for s in text:
                    if s in str1:
                        if s != ' ':
                            result_text = result_text + str2[str1.index(s)]
                        else:
                            result_text = result_text + ' '
                    else:
                        result_text = '埃特巴什码只能对英文字母加密！'
                self.text_out.setText('埃特巴什码:' + result_text)
            elif result == '字符串--二进制':
                tmp = []
                for c in text:
                    tmp.append(bin(ord(c)).replace('0b', ''))
                result_text = ' '.join(tmp)
                self.text_out.setText('字符串转二进制:' + result_text)
            elif result == '字符串--八进制':
                tmp = []
                for c in text:
                    tmp.append(oct(ord(c)).replace('0o', ''))
                result_text = ' '.join(tmp)
                self.text_out.setText('字符串转八进制:' + result_text)
            elif result == '字符串--十六进制':
                tmp = []
                for c in text:
                    tmp.append(hex(ord(c)).replace('0x', ''))
                result_text = ' '.join(tmp)
                self.text_out.setText('字符串转十六进制:' + result_text)
            elif result == '字符串--十进制':
                result_text = self.sto10()
                self.text_out.setText('字符串转十进制:' + result_text)
            elif result == 'url-utf8':
                result_text = urllib.parse.quote(text)
                self.text_out.setText('url-utf8:' + result_text)
            elif result =='url-gb2312':
                result_text = urllib.parse.quote(text, 'gb2312')
                self.text_out.setText('url-gb2312:' + result_text)
            elif result =='unicode':
                result_text = text.encode('unicode_escape').decode('utf-8')
                self.text_out.setText('unicode:' + result_text)
            elif result == 'htmlcode':
                result_text = html.escape(text)
                self.text_out.setText('htmlencode:' + result_text)
            elif result =='jsfuck' :
                result_text = '<a href="http://www.jsfuck.com/">http://www.jsfuck.com/</a>'
                self.text_out.setText('jsfuck，其在线解密网址:' + result_text)
            elif result == 'brainfuck' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText('brainfuck，其在线解密网址:' + result_text )
            elif result == 'Ook' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    'Ook(若待解码的文本出现了O,o,k），其在线解密网址:' + result_text )
            elif result =='shortOok' :
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    'shortOok(若待解码的文本中无O,o,k)其在线解密网址:' + result_text )
            elif result =='printable':
                result_text = '<a href="http://www.mxcz.net/tools/quotedprintable.aspx">http://www.mxcz.net/tools/quotedprintable.aspx</a>'
                self.text_out.setText('Quoted-Printable，其在线解密网址:' + result_text)
            elif result =='与佛论禅' :
                result_text = '<a href="http://www.keyfc.net/bbs/tools/tudoucode.aspx">http://www.keyfc.net/bbs/tools/tudoucode.aspx</a>'
                result_texts = '<a href="http://hi.pcmoe.net/buddha.html">http://hi.pcmoe.net/buddha.html</a>'
                self.text_out.setText(
                    '与佛论禅，其在线解密网址:' + result_text + '\n新与佛论禅，其在线解密网址:'+ result_texts )
            elif result =='词频分析':
                result_text = '<a href="http://quipqiup.com/">http://quipqiup.com/</a>'
                self.text_out.setText(
                    '英文字符数挺多，毫无章法，试试词频分析吧，其在线解密网址:' + result_text )
            else:
                self.text_out.setText('加密错误，请再核对加密类型！')
        except Exception as e:
            self.text_in.setText('error:' + str(e))
            pass
    def Clear(self):
        self.text_in.setText('')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Win()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./beijing.jpg")))
    form.setPalette(palette)
    form.show()
    sys.exit(app.exec_())

