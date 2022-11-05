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
import win32api
from pyDes import *
import os

version = '2.6'
update_time = '2021.4.6'


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(80, 80, 600, 600)
        self.setWindowTitle('CtfdecodeTools' + version + ' ' + update_time + '  By chrislyy  CSDN:Chrisyyl ')
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.label_in = QLabel('输入待解密文本')
        self.label_out = QLabel('输出解密结果')
        self.text_in = QTextEdit('每次输入新待解密密码都要点一次重置，然后再点传入，最后解密（解密可重复点，直至解密结束）。')
        self.text_out = QTextEdit()
        self.btn3 = QPushButton('重置')
        self.btn1 = QPushButton('传入待解密文本')
        self.btn2 = QPushButton('开始解密')
        self.btn4 = QPushButton('图像解密补充')
        self.btn5 = QPushButton('联系我们')
        self.btn6 = QPushButton('添加注册码')
        self.decode_type = ''
        self.Des_Key = b"BHC#@*UM"  # Key（可换）
        self.Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7"  # 自定义IV向量（可换）
        self.flag_ascii = 0
        self.flag_binary = 0
        self.flag_yunying = 0
        self.flag_bacon = 0
        self.flag_base16 = 0
        self.flag_base32 = 0
        self.flag_base64 = 0
        self.flag_base36 = 0
        self.flag_base58 = 0
        self.flag_base62 = 0
        self.flag_base85 = 0
        self.flag_base91 = 0
        self.flag_rot13 = 0
        self.flag_zhalan = 0
        self.flag_yiwei = 0
        self.flag_jianpan = 0
        self.flag_url = 0
        self.flag_gb2312 = 0
        self.flag_unicode = 0
        self.flag_html = 0
        self.flag_morse = 0
        self.flag_dangpu = 0
        self.flag_aiteba = 0
        self.flag_jsfuck = 0
        self.flag_brainfuck = 0
        self.flag_Ook = 0
        self.flag_shortOok = 0
        self.flag_printable = 0
        self.flag_yufolunchan = 0
        self.flag_xinyufolunchan = 0
        self.flag_quipqiup = 0

        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        for btn in (self.btn3, self.btn1, self.btn2):
            h1.addWidget(btn)
        for btn in (self.btn4, self.btn5, self.btn6):
            h2.addWidget(btn)


        layout = QVBoxLayout()
        layout.addWidget(self.label_in)
        layout.addWidget(self.text_in)
        layout.addWidget(self.label_out)
        layout.addWidget(self.text_out)
        # layout.addWidget(self.btn3)
        # layout.addWidget(self.btn1)
        # layout.addWidget(self.btn2)
        layout.addLayout(h1)
        #layout.addWidget(self.btn4)
        layout.addLayout(h2)




        #给标签设置样式
        self.label_in.setMinimumSize(150,30)
        self.label_out.setMinimumSize(150, 30)
        self.label_in.setFont(QFont("微软雅黑",11,QFont.Bold))
        self.label_out.setFont(QFont("微软雅黑",11,QFont.Bold))
        self.label_in.setStyleSheet(
                                    "QLabel{margin-left:15px}"
                                    "QLabel{margin-right:450px}")
        self.label_out.setStyleSheet(
                                     "QLabel{margin-left:15px}"
                                     "QLabel{margin-right:450px}")
        #设置窗口透明度
        #self.setWindowOpacity(0.9)
        #给多行文本框设置样式
        self.text_in.setStyleSheet("QTextEdit{font:15px}"
                                   "QTextEdit{margin-left:15px}"
                                   "QTextEdit{margin-right:15px}")
        self.text_out.setStyleSheet("QTextEdit{font:15px}"
                                    "QTextEdit{margin-left:15px}"
                                    "QTextEdit{margin-right:15px}")
        #给按钮添加样式
        self.btn1.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"                 
                                "QPushButton{font:15px}"
                                )
        self.btn2.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:15px}"
                                )
        self.btn3.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:15px}"
                                )
        self.btn4.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:15px}"
                                )
        self.btn5.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:15px}"
                                )
        self.btn6.setStyleSheet("QPushButton{color:black}"
                                "QPushButton:hover{color:red}"
                                "QPushButton{background-color:rgb(176,224,230)}"
                                "QPushButton{border-radius:8px}"
                                "QPushButton{padding:4px 4px }"
                                "QPushButton{margin:2px 20px 2px 20px}"
                                "QPushButton{font:15px}"
                                )
        self.btn1.setMinimumHeight(30)
        self.btn2.setMinimumHeight(30)
        self.btn3.setMinimumHeight(30)

        self.setLayout(layout)
        self.btn3.clicked.connect(self.resetting)
        self.btn1.clicked.connect(self.dftype)
        self.btn2.clicked.connect(self.decode)
        self.btn4.clicked.connect(self.adder)
        self.btn5.clicked.connect(self.linker)
        self.btn6.clicked.connect(self.licenser)


    #添加注册码
    def licenser(self):
        value, ok = QInputDialog.getText(self, "添加注册码", "请输入注册码:", QLineEdit.Normal,"")
        try:
            CVolumeSerialNumber = str(win32api.GetVolumeInformation("C:\\")[1])
            k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
            EncryptStr = k.encrypt(CVolumeSerialNumber)
            registencode = base64.b64encode(EncryptStr)
            # print(registencode)
            # print(value)
            if value == registencode.decode('utf-8'):
                self.text_out.setText('successed')
                with open('./register', 'w') as f:
                    f.write(value)
                    f.close()
            else:
                self.text_out.setText('failed')

        except Exception as e:
            self.text_out.setText('error:' + str(e))
            pass


    #联系我们
    def linker(self):
        value, ok = QInputDialog.getMultiLineText(self, "联系我们", "请按照下方联系方式联系我们:", "若您有对软件的建议及意见\n请发送邮箱到chrisslyy@163.com")

    #补充跳出对话框
    def adder(self):

        QMessageBox.information(self,'图形加密补充','补充文档文件在当前程序文件夹下。',QMessageBox.Yes | QMessageBox.No)
        try:
            os.system('补充文档.docx')
        except Exception as e:
            self.text_out.setText('error:' + str(e))
            pass



    # 将所有标志置位
    def resetting(self):
        self.flag_ascii = 1
        self.flag_binary = 1
        self.flag_yunying = 1
        self.flag_bacon = 1
        self.flag_base16 = 1
        self.flag_base32 = 1
        self.flag_base64 = 1
        self.flag_base36 = 1
        self.flag_base58 = 1
        self.flag_base62 = 1
        self.flag_base85 = 1
        self.flag_base91 = 1
        self.flag_rot13 = 1
        self.flag_zhalan = 1
        self.flag_yiwei = 1
        self.flag_jianpan = 1
        self.flag_url = 1
        self.flag_gb2312 = 1
        self.flag_unicode = 1
        self.flag_html = 1
        self.flag_morse = 1
        self.flag_dangpu = 1
        self.flag_aiteba = 1
        self.flag_jsfuck = 1
        self.flag_brainfuck = 1
        self.flag_Ook = 1
        self.flag_shortOok = 1
        self.flag_printable = 1
        self.flag_yufolunchan = 1
        self.flag_xinyufolunchan = 1
        self.flag_quipqiup = 1
        return

    # 判断密码类型
    def dftype(self):
        list1 = []
        string_all = str(self.text_in.toPlainText())
        for i in string_all:
            list1.append(i)
        # 密码字符特征
        string_set_ascii = set([ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',' '])
        string_set_binary = set(['0','1',' '])
        string_set_yunying = set(['0', '1', '2', '4', '8'])
        string_set_base16 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e',
             'f'])
        string_set_base32 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '='])
        string_set_base64 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '='])
        #base36密文内容为int值，加密后字符串表为0123456789abcdefghijklmnopqrstuvwxyz
        string_set_base36 = set([ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        # 去除0 (零), O (大写字母O), I (大写的字母i) and l (小写的字母L) ，和几个影响双击选择的字符，如/, +，=
        string_set_base58 = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1',
             '2', '3', '4', '5', '6', '7', '8', '9'])
        #Base62编码是将数字转换为ASCII字符串（0-9，az和AZ）
        string_set_base62 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9'])
        #0–9, A–Z, a–z, and then the 23 characters !#$%&()*+-;<=>?@^_`{|}~这些字符能被base85encode。
        #ascll85中根据编码算字符!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuv
        string_set_base85 = set(
            [ "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*","+", ",",  "-", ".", "/", "0", "1", "2", "3", "4",
            "5", "6",  "7", "8", "9", ":", ";", "<", "=", ">","?", "@",  "A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J",  "K", "L", "M", "N", "O", "P", "Q", "R","S", "T",  "U", "V", "W", "X", "Y", "Z", "[", "]",
            "^", "_",  "`", "a", "b", "c", "d", "e", "f", "g","h", "i",  "j", "k", "l", "m", "n", "o", "p", "q",
         "r", "s",  "t", "u", "v"])
        string_set_base91 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9','!','#','$','%','&','(',')','*','+',',','.','/',':',';','<','=','>',
        '?','@','[',']','^','_','`','{','|','}','~','"'])
        # 数字保持不变
        string_set_rot13 = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9','{','}','_','!','@','$','?'])
        string_set_zhalan = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9',
             '!', '?', '@','{','}','_','$'])
        string_set_yiwei = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9','{','}','_','!','@','$','?'])
        string_set_jianpan = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' '])
        string_set_bacon1 = set(['a', 'b'])
        string_set_bacon2 = set(['A', 'B'])
        string_set_morse = set(['.', '-', ' '])  # 每个要解密的字符用空格分隔
        string_set_dangpu = set(['田', '由', '中', '人', '工', '大', '王', '夫', '井', '羊'])
        string_set_aiteba = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' '])
        string_set_jsfuck = set(['[',']','(',')','!','+'])
        string_set_brainfuck = set(['>','<','+','-','.',',','[',']',' ','\n'])
        string_set_Ook = set(['O','o','k','.','!','?',' ','\n'])
        string_set_shortOok = set(['.','!','?',' ','\n'])
        string_set_printable = set(['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','='])
        string_set_quipqiup = set(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
                , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9', '-', ',', '.', '!', '?',' '])
        # 判断字符特征集合
        result_ascii = all([word in string_set_ascii for word in list1])
        result_binary = all([word in string_set_binary for word in list1])
        result_yunying = all([word in string_set_yunying for word in list1])
        result_bacon = all([word in string_set_bacon1 for word in list1]) or all(
            [word in string_set_bacon2 for word in list1])
        result_base16 = all([word in string_set_base16 for word in list1])
        result_base32 = all([word in string_set_base32 for word in list1])
        result_base64 = all([word in string_set_base64 for word in list1])
        result_base36 = all([word in string_set_base36 for word in list1])
        result_base58 = all([word in string_set_base58 for word in list1])
        result_base62 = all([word in string_set_base62 for word in list1])
        result_rot13 = all([word in string_set_rot13 for word in list1])
        result_zhalan = all([word in string_set_zhalan for word in list1])
        result_yiwei = all([word in string_set_yiwei for word in list1])
        result_jianpan = all([word in string_set_jianpan for word in list1])
        result_url = '%' in list1
        result_gb2312 = '%' in list1
        result_unicode = '\\' in list1 and 'u' in list1
        result_htmldecode = '&' in list1 and '#' in list1 and ';' in list1
        result_morse = all([word in string_set_morse for word in list1])
        result_dangpu = all([word in string_set_dangpu for word in list1])
        result_aiteba = all([word in string_set_aiteba for word in list1])
        result_base85 = all([word in string_set_base85 for word in list1])
        result_base91 = all([word in string_set_base91 for word in list1])
        result_jsfuck = all([word in string_set_jsfuck for word in list1])
        result_brainfuck = all([word in string_set_brainfuck for word in list1])
        result_Ook = all([word in string_set_Ook for word in list1])
        result_shortOok = all([word in string_set_shortOok for word in list1])
        result_printable = all([word in string_set_printable for word in list1]) or 'Quoted-Printable' in string_all
        result_yufolunchan = (string_all[0] == '佛' and string_all[1] == '曰')
        result_xinyufolunchan = (string_all[0] == '新' and string_all[1] == '佛' and string_all[2] == '曰')
        result_quipqiup = all([word in string_set_quipqiup for word in list1])

        # 判断密码类型，遍历
        if result_binary and self.flag_binary == 1:
            ty = 'binary'
            return ty
        elif result_ascii and self.flag_ascii == 1:
            ty = 'ascii'
            return ty
        elif result_yunying and self.flag_yunying == 1:
            ty = 'yunying'
            return ty
        elif result_bacon and self.flag_bacon == 1:
            ty = 'bacon'
            return ty
        elif result_base16 and self.flag_base16 == 1:
            ty = 'base16'
            return ty
        elif result_base32 and self.flag_base32 == 1:
            ty = 'base32'
            return ty
        elif result_base64 and self.flag_base64 == 1:
            ty = 'base64'
            return ty
        elif result_base36 and self.flag_base36 == 1:
            ty = 'base36'
            return ty
        elif result_base58 and self.flag_base58 == 1:
            ty = 'base58'
            return ty
        elif result_base62 and self.flag_base62 == 1:
            ty = 'base62'
            return ty
        elif result_base85 and self.flag_base85 == 1:
            ty = 'base85'
            return ty
        elif result_base91 and self.flag_base91 == 1:
            ty = 'base91'
            return ty
        elif result_rot13 and self.flag_rot13 == 1:
            ty = 'rot13'
            return ty
        elif result_zhalan and self.flag_zhalan == 1:
            ty = 'zhalan'
            return ty
        elif result_yiwei and self.flag_yiwei == 1:
            ty = 'yiwei'
            return ty
        elif result_jianpan and self.flag_jianpan == 1:
            ty = 'jianpan'
            return ty
        elif result_url and self.flag_url == 1:
            ty = 'url-utf8'
            return ty
        elif result_url and self.flag_gb2312 == 1:
            ty = 'url-gb2312'
            return ty
        elif result_unicode and self.flag_unicode == 1:
            ty = 'unicode'
            return ty
        elif result_htmldecode and self.flag_html == 1:
            ty = 'htmldecode'
            return  ty
        elif result_morse and self.flag_morse == 1:
            ty = 'morse'
            return ty
        elif result_dangpu and self.flag_dangpu == 1:
            ty = 'dangpu'
            return ty
        elif result_aiteba and self.flag_aiteba == 1:
            ty = 'aiteba'
            return ty
        elif result_jsfuck and self.flag_jsfuck == 1:
            ty = 'jsfuck'
            return ty
        elif result_brainfuck and self.flag_brainfuck == 1:
            ty = 'brainfuck'
            return ty
        elif result_Ook and self.flag_Ook == 1:
            ty ='Ook'
            return ty
        elif result_shortOok and self.flag_shortOok == 1:
            ty = 'shortOok'
            return ty
        elif result_printable and self.flag_printable == 1:
            ty = 'printable'
            return ty
        elif result_yufolunchan and self.flag_yufolunchan == 1:
            ty = 'yufolunchan'
            return ty
        elif result_xinyufolunchan and self.flag_xinyufolunchan == 1:
            ty = 'xinyufolunchan'
            return ty
        elif result_quipqiup and self.flag_quipqiup == 1:
            ty = 'quipqiup'
            return ty
        else:
            return 0

    # 获取解密文本并传输判别密码类型结果
    def get_string(self):
        try:
            gettext = self.text_in.toPlainText()
            if gettext == '':
                self.text_out.setText('请输入一个源字符串！')
                return 0
            else:
                self.decode_type = self.dftype()
                return self.decode_type

        except Exception as e:
            self.text_in.setText('error:' + str(e))
            pass

    # 解密
    def decode(self):
        try:
            result_text = ''
            text = self.text_in.toPlainText()
            CVolumeSerialNumber = str(win32api.GetVolumeInformation("C:\\")[1])
            k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
            EncryptStr = k.encrypt(CVolumeSerialNumber)
            registencode = base64.b64encode(EncryptStr)
            f = open('./register', 'r')
            if f.read() != registencode.decode('utf-8'):
                self.text_out.setText('请输入注册码！')
                return 0
            if text == '':
                self.text_out.setText('请输入一个源字符串！')
                return 0
            result = self.get_string()
            if result == 'binary' and self.flag_binary == 1:
                self.flag_binary = 0
                s = text.split(' ')
                result_text = ''
                for item in s:
                    a = int(item, 2)
                    result_text += chr(a)
                self.text_out.setText('二进制转字符串:' + result_text)
            elif result == 'ascii' and self.flag_ascii == 1:
                self.flag_ascii = 0
                s = text.split(' ')
                result =''
                for i in s:
                    if i != '':
                        result = result + chr(int(i))
                result_text = result
                self.text_out.setText('ascii转字符串:' + result_text)
            elif result == 'yunying' and self.flag_yunying == 1:
                self.flag_yunying = 0
                charList = [chr(i) for i in range(ord('a'), ord('z') + 1)]
                ret = []
                # 按零分割，分割每一部分数字相加之和即对应的字母
                plaintext = [i for i in text.split('0')]
                for i in plaintext:
                    tmp = 0
                    for j in range(len(i)):
                        tmp += int(i[j])
                    ret.append(charList[tmp - 1])
                result_text = ''.join(ret)
                self.text_out.setText('云影密码:' + result_text)
            elif result == 'bacon' and self.flag_bacon == 1:
                self.flag_bacon = 0
                return_str = ''
                dicts = {'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y',
                         'abbab': 'N',
                         'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F',
                         'aabaa': 'E',
                         'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D',
                         'abbbb': 'P',
                         'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
                sums = len(text)
                j = 5  ##每5个为一组
                for i in range(int(sums / j)):
                    result = text[j * i:j * (i + 1)].lower()
                    return_str += str(dicts[result])
                result_text = return_str
                self.text_out.setText('培根密码:' + result_text)
            elif result == 'base16' and self.flag_base16 == 1:
                self.flag_base16 = 0
                text = base64.b16decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base16:' + result_text)
            elif result == 'base32' and self.flag_base32 == 1:
                self.flag_base32 = 0
                text = base64.b32decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base32:' + result_text)
            elif result == 'base64' and self.flag_base64 == 1:
                self.flag_base64 = 0
                text = base64.b64decode(text.encode("utf-8"))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base64:' + result_text)
            elif result == 'base36' and self.flag_base36 == 1:
                self.flag_base36 = 0
                c = base36.dumps(int(text))
                #result_text = str(c, encoding='utf-8')
                self.text_out.setText('base36:' + c)
            elif result == 'base58' and self.flag_base58 == 1:
                self.flag_base58 = 0
                text = base58.b58decode(text.encode('utf-8'))
                result_text = str(text, encoding='utf-8')
                self.text_out.setText('base58:' + result_text)
            elif result == 'base62' and self.flag_base62 == 1:
                self.flag_base62 = 0
                c = base62.decode(str(text))
                #result_text = str(text, encoding='utf-8')
                self.text_out.setText('base62:' + str(c))
            elif result == 'base85' and self.flag_base85 == 1:
                self.flag_base85 = 0
                c = base64.a85decode(str(text)).decode()
                self.text_out.setText('base85:'+ str(c))
            elif result == 'base91' and self.flag_base91 == 1:
                self.flag_base91 = 0
                c = base91.decode(str(text)).decode()
                #result_text = str(text, encoding='utf-8')
                self.text_out.setText('base91:' + str(c))
            elif result == 'rot13' and self.flag_rot13 == 1:
                self.flag_rot13 = 0
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
            elif result == 'zhalan' and self.flag_zhalan == 1:
                self.flag_zhalan = 0
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
            elif result == 'yiwei' and self.flag_yiwei == 1:
                self.flag_yiwei = 0
                inputStr = text
                result = ''
                for j in range(26):
                    result_list = []
                    for i, num in zip(inputStr, range(len(inputStr))):
                        if i.islower:
                            # abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
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
                self.text_out.setText('移位密码:\n' + result_text)
            elif result == 'jianpan' and self.flag_jianpan == 1:
                self.flag_jianpan = 0
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
                self.text_out.setText('键盘密码:' + result_text)
            elif result == 'url-utf8' and self.flag_url == 1:
                self.flag_url = 0
                result_text = str(urllib.parse.unquote(text))
                self.text_out.setText('url-utf8:' + result_text)
            elif result == 'url-gb2312' and self.flag_gb2312 == 1:
                self.flag_gb2312 = 0
                result_text = str(urllib.parse.unquote(text, 'gb2312'))
                self.text_out.setText('url-gb2312:' + result_text)
            elif result == 'unicode' and self.flag_unicode == 1:
                self.flag_unicode = 0
                result_text = bytes(text, encoding="utf8").decode('unicode_escape')
                self.text_out.setText('unicode:' + result_text)
            elif result =='htmldecode' and self.flag_html == 1:
                self.flag_html = 0
                result_text = html.unescape(text)
                self.text_out.setText('htmldecode:' + result_text)
            elif result == 'morse' and self.flag_morse == 1:
                self.flag_morse = 0
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
            elif result == 'dangpu' and self.flag_dangpu == 1:
                self.flag_dangpu = 0
                result_text = ''
                dict = {'田': 0, '由': 1, '中': 2, '人': 3, '工': 4, '大': 5, '王': 6, '夫': 7, '井': 8, '羊': 9}
                for item in text:
                    result_text += str((dict[item]))
                self.text_out.setText('当铺密码:' + result_text)
            elif result =='aiteba' and self.flag_aiteba == 1:
                self.flag_aiteba = 0
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                result_text = ""
                for s in text:
                    if s != ' ':
                        result_text = result_text + str2[str1.index(s)]
                    else:
                        result_text = result_text + ' '
                self.text_out.setText('埃特巴什码:' + result_text)
            elif result =='jsfuck' and self.flag_jsfuck == 1:
                self.flag_jsfuck = 0
                result_text = '<a href="http://www.jsfuck.com/">http://www.jsfuck.com/</a>'
                self.text_out.setText('此编码很可能为jsfuck，其在线解密网址:' + result_text)
            elif result == 'brainfuck' and self.flag_brainfuck == 1:
                self.flag_brainfuck = 0
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText('此编码很可能为brainfuck，其在线解密网址:' + result_text )
            elif result == 'Ook' and self.flag_Ook == 1:
                self.flag_Ook = 0
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    '此编码很可能为Ook(若待解码的文本出现了O,o,k），其在线解密网址:' + result_text )
            elif result =='shortOok' and self.flag_shortOok == 1:
                self.flag_shortOok = 0
                result_text = '<a href="https://www.splitbrain.org/services/ook">https://www.splitbrain.org/services/ook</a>'
                self.text_out.setText(
                    '此编码很可能为shortOok(若待解码的文本中无O,o,k)其在线解密网址:' + result_text )
            elif result =='printable' and self.flag_printable == 1:
                self.flag_printable = 0
                result_text = '<a href="http://www.mxcz.net/tools/quotedprintable.aspx">http://www.mxcz.net/tools/quotedprintable.aspx</a>'
                self.text_out.setText('此编码很可能为Quoted-Printable，其在线解密网址:' + result_text)
            elif result =='yufolunchan' and self.flag_yufolunchan == 1:
                self.flag_yufolunchan = 0
                result_text = '<a href="http://www.keyfc.net/bbs/tools/tudoucode.aspx">http://www.keyfc.net/bbs/tools/tudoucode.aspx</a>'
                self.text_out.setText(
                    '此编码很可能为与佛论禅，其在线解密网址:' + result_text )
            elif result =='xinyufolunchan' and self.flag_xinyufolunchan == 1:
                self.flag_xinyufolunchan = 0
                result_text = '<a href="http://hi.pcmoe.net/buddha.html">http://hi.pcmoe.net/buddha.html</a>'
                self.text_out.setText(
                    '此编码很可能为新与佛论禅，其在线解密网址:' + result_text )
            elif result =='quipqiup' and self.flag_quipqiup == 1:
                self.flag_quipqiup = 0
                result_text = '<a href="http://quipqiup.com/">http://quipqiup.com/</a>'
                self.text_out.setText(
                    '英文字符数挺多，毫无章法，试试词频分析吧，其在线解密网址:' + result_text )
            else:
                self.text_out.setText('解码结束，再无符合密码！')
        except Exception as e:
            self.text_out.setText('error:' + str(e))
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Win()
    #用QPalette设置背景图片和背景颜色
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./beijing.jpg")))
    form.setPalette(palette)
    form.show()
    sys.exit(app.exec_())

