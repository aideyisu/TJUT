'''
/************************************************************/
/*                程序作者：爱的伊苏                        */
/*                程序完成时间：2019/5/18                   */
/*                有任何问题请联系：740531307@qq.com        */
/************************************************************/
//@永远得意的笑下去
 
 
'''
CaesaTable = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
              ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a'],
              ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b'],
              ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c'],
              ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],
              ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e'],
              ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'],
              ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
              ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
              ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
              ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
              ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
              ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
              ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
              ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
              ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
              ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'],
              ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
              ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'],
              ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
              ['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'],
              ['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
              ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
              ['y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
              ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#首先建立对应的凯撒表，随后再建立一个顺序的字母表

def jiami():
    print("Please input your encryption key(请输入你的密钥)")
    key = input('Key: ')

    print("PLease input your text")
    text = input('Text: ')

    pos = 0 #当前加密段位置
    ans = ""#加密结果字符串

    for x in text:
        if x == " ":
            ans += " "
            continue
        #过滤空格
        i = alphabet.find(x) #在加密表中找到对应字母
        cipherKey = key[pos] #当前位密钥
        j = alphabet.find(cipherKey)#当前位置密钥在密码表中的列数
        ans += CaesaTable[i][j] #在凯撒表中行列相加完成位置加密
        #此步骤为pos模密钥长度的过程，实现循环加密
        if pos == len(key) - 1:
            pos = 0
        else:
            pos += 1
    print("the result is : ")
    print(ans)#最终输出加密结果


def jiemi():
    print("Please input your encryption key(请输入你的密钥)")
    key = input("key : ")

    print("Please input your ciphertext")
    ciphertext = input("Ciphertext : ")
    
    pos = 0
    ans = ""

    for x in ciphertext:
        if x == " ":
            ans += " "
            continue
        #同理过滤空格
        j = alphabet.find(x) 
        cipherKey = key[pos] #当前位密钥
        i = alphabet.find(cipherKey)
        ans += CaesaTable[26-i][j] #在凯撒表中行列相加完成位置加密
        #此步骤为pos模密钥-长度的过程，实现循环加密
        if pos == len(key) - 1:
            pos = 0
        else:
            pos += 1
    print("the result is : ")
    print(ans)#最终输出加密结果
        

def getKeyLen(ciphertext):
    keylength = 1
    maxcount = 0


    for step in range(3,18):  #可能的密钥长度
        count = 0
        for i in range(step, len(ciphertext)-step):
            if ciphertext[i] == ciphertext[i + step]:
                count += 1
        if count > maxcount:
            maxcount = count
            keylength = step
    return keylength


#密文 and 密钥长度
def getKey(text,length): # 获取密钥
    key = [] # 定义空白列表用来存密钥
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    matrix =textToList(text,length)
    for i in range(length):
        w = [row[i] for row in matrix] #获取每组密文
        li = countList(w) 
        powLi = [] #算乘积
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k]*li[k]
            powLi.append(Sum)
            li = li[1:]+li[:1]#循环移位
        Abs = 100
        ch = ''
        for j in range(len(powLi)):
             if abs(powLi[j] -0.065546)<Abs: # 找出最接近英文字母重合指数的项
                 Abs = abs(powLi[j] -0.065546) # 保存最接近的距离，作为下次比较的基准
                 ch = chr(j+97)
        key.append(ch)
    return key 


def No_Cipher_jiemi():
    print("Please inpit your ciphertext (请输入密文) ")
    ciphertext = input("cipher : ")
    length = getKeyLen(ciphertext) #得到密钥长度
    key = getKey(ciphertext,length) #找到密钥
    keyStr = ''
    for k in key:
        keyStr+=k
    print('the Key is:',keyStr)
    plainText = ''
    index = 0
    for ch in cipherText:
        c = chr((ord(ch)-ord(key[index%length]))%26+97)
        plainText += c
        index+=1
    return plainText # 返回明文
  
    

print("输出你所需要的指令")
choose = input("1-加密    2-解密    3-暴力解密（无需密钥）")
if choose == '1':
    jiami()
elif choose == '2':
    jiemi()
elif choose == '3':
    No_Cipher_jiemi()
else:
    print("错误输入，程序退出")
