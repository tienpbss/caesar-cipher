import re;
import string;

regex = re.compile('[^a-zA-Z]')

alphabet = regex.sub('', string.ascii_lowercase)

amount = len(alphabet) # 26

def clean(message):
    return regex.sub('', message)

def numberToLetter(n):
    while (n<0):
        n+=amount
    return alphabet[n%amount]

def encode(message, key):
    res = ''
    for i in message:
        if i != ' ':
            position = alphabet.find(i)
            # print(position)
            position += key
            # print(position)
            res += numberToLetter(position)
        else: res+=i
    return res
    
def decode(message, key):
    res = ''
    for i in message:
        if i != ' ':
            position = alphabet.find(i)
            # print(position)
            position -= key
            # print(position)
            res += numberToLetter(position)
        else: res+=i
    return res

def decodeNoneKey(message):
    res = []
    for i in range(amount):    # 0 - 25
        res.append(decode(message, i))
    return res


def main():
    while True:
        action = input('Enter 1 to encode, 2 to decode, 3 to decode without key other to exit: ')
        if (action == '1'):
            message = input('Enter message that you want to encode: ')
            key = input('Enter key for encode: ')
            try:
                key = int(key)
            except:
                print('Key must be integer!')
                continue
            en = encode(message, key)
            print('After encode:', en)
        elif(action == '2'):
            message = input('Enter message that you want to decode: ')
            key = input('Enter key for decode: ')
            try:
                key = int(key)
            except:
                print('Key must be integer!')
                continue
            de = decode(message, key)
            print('After decode:', de)

        elif(action == '3'):
            message = input('Enter message that you want to decode without key: ')
            results = decodeNoneKey(message)
            print('List case:')
            for i in results:
                print(i)
        else:
            break


if __name__ == '__main__':
    main()