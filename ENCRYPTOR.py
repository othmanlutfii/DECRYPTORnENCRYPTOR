inputfile = input('nama file yg akan di encrypt:')
key = input('masukan password:')
simpan = input('nama file setelah di encrypt:')

#encryptorvigenere
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))
def encryptorvigenere(message, key):
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            if letter == " ":
                encrypted += " "
            elif letter == "-":
                encrypted += "-"
            elif letter == ",":
                encrypted += ","
            elif letter == ".":
                encrypted += "."
            elif letter == "/":
                encrypted += "/"
            elif letter == "?":
                encrypted += "?"
            elif letter == "!":
                encrypted += "!"
            elif letter == "(":
                encrypted += "("
            elif letter == ")":
                encrypted += ")"
            elif letter == "0":
                encrypted += "0"
            elif letter == "1":
                encrypted += "1"
            elif letter == "2":
                encrypted += "2"
            elif letter == "3":
                encrypted += "3"
            elif letter == "4":
                encrypted += "4"
            elif letter == "5":
                encrypted += "5"
            elif letter == "6":
                encrypted += "6"
            elif letter == "7":
                encrypted += "7"
            elif letter == "8":
                encrypted += "8"
            elif letter == "9":
                encrypted += "9"
            elif letter == "'":
                encrypted += "'"
            else:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
            i += 1
    return encrypted
#encryptpolybius
def encryptpolybius(s):
    enct = ""
    for char in s:
        if char == 'j':
            enct = enct + '98'
        elif char == 'i':
            enct = enct + '89'
        elif char == "'":
            enct = enct + "''"
        elif char == ' ':
            enct = enct + '  '
        elif char == '.':
            enct = enct + '..'
        elif char == ',':
            enct = enct + ',,'
        elif char == '/':
            enct = enct + '//'
        elif char == '(':
            enct = enct + '(('
        elif char == ')':
            enct = enct + '))'
        elif char == '-':
            enct = enct + '--'
        elif char == '0':
            enct = enct + '71'
        elif char == '1':
            enct = enct + '72'
        elif char == '2':
            enct = enct + '73'
        elif char == '3':
            enct = enct + '74'
        elif char == '4':
            enct = enct + '75'
        elif char == '5':
            enct = enct + '76'
        elif char == '6':
            enct = enct + '77'
        elif char == '7':
            enct = enct + '78'
        elif char == '8':
            enct = enct + '79'
        elif char == '9':
            enct = enct + '80'
        else:
            row = int((ord(char) - ord('a')) / 5) + 1
            col = ((ord(char) - ord('a')) % 5) + 1
            if char == 'k':
                row = row - 1
                col = 5 - col + 1
            elif ord(char) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            r=str(row)
            c=str(col)
            enct = enct + r + c
    return enct

#buka file yg ingin di enkripsi
f = open(inputfile,'rb+')
ch=f.read()
file_enkripsi=str(ch,'utf-8').lower()
print(file_enkripsi)

#hitung kata
jumlah_kata = 0
with open(inputfile, 'r') as nn:
    for line in nn:
        kata = line.split()
        jumlah_kata += len(kata)

#Proses dan output
if jumlah_kata >= 50:
    hasil_enkripsi_vig = encryptorvigenere(file_enkripsi,key)
    hasil_enkripsi_pol = encryptpolybius(hasil_enkripsi_vig)
    hasilencyrptor1 = hasil_enkripsi_pol.encode()
    print(hasilencyrptor1)
    with open (simpan, 'wb') as encrypted_file:
        encrypted_file.write(hasilencyrptor1)
else :
    print('masukan dokumen lebih banyak kata lagi')