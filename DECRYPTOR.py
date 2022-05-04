inputfile = input('nama file yg akan di decrypt:')
key = input('masukan password:')
simpan = input('nama file setelah di decrypt:')

#decryptorvigenere
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def decryptorvigenere(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            if letter == " ":
                decrypted += " "
            elif letter == ",":
                decrypted += ","
            elif letter == ".":
                decrypted += "."
            elif letter == "'":
                decrypted += "'"
            elif letter == "/":
                decrypted += "/"
            elif letter == "-":
                decrypted += "-"
            elif letter == "?":
                decrypted += "?"
            elif letter == "!":
                decrypted += "!"
            elif letter == "(":
                decrypted += "("
            elif letter == ")":
                decrypted += ")"
            elif letter == "0":
                decrypted += "0"
            elif letter == "1":
                decrypted += "1"
            elif letter == "2":
                decrypted += "2"
            elif letter == "3":
                decrypted += "3"
            elif letter == "4":
                decrypted += "4"
            elif letter == "5":
                decrypted += "5"
            elif letter == "6":
                decrypted += "6"
            elif letter == "7":
                decrypted += "7"
            elif letter == "8":
                decrypted += "8"
            elif letter == "9":
                decrypted += "9"
            else:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
            i += 1
    return decrypted

#decryptpolybius
def decryptpolybius(y):
    list1 = list(y)
    hasil = ""
    for i in range (0,len(y),2):
        if str(list1[i])+str(list1[i+1]) == '98':
            hasil = hasil+ 'j'
        elif str(list1[i])+str(list1[i+1]) == '89':
            hasil = hasil+ 'i'
        elif list1[i] + list1[i+1] == '  ':
            hasil = hasil+ ' '
        elif list1[i] + list1[i+1] == '..':
            hasil = hasil+ '.'
        elif list1[i] + list1[i+1] == ',,':
            hasil = hasil + ','
        elif list1[i] + list1[i+1] == '--':
            hasil = hasil + '-'
        elif list1[i] + list1[i+1] == "''":
            hasil = hasil + "'"
        elif list1[i] + list1[i+1] == '//':
            hasil = hasil + '/'
        elif list1[i] + list1[i+1] == '((':
            hasil = hasil + '('
        elif list1[i] + list1[i+1] == '))':
            hasil = hasil + ')'
        elif list1[i] + list1[i+1] == '71':
            hasil = hasil + '0'
        elif list1[i] + list1[i+1] == '72':
            hasil = hasil + '11'
        elif list1[i] + list1[i+1] == '73':
            hasil = hasil + '2'
        elif list1[i] + list1[i+1] == '74':
            hasil = hasil+ '3'
        elif list1[i] + list1[i+1] == '75':
            hasil = hasil+ '4'
        elif list1[i] + list1[i+1] == '76':
            hasil = hasil+ '5'
        elif list1[i] + list1[i+1] == '77':
            hasil = hasil+ '6'
        elif list1[i] + list1[i+1] == '78':
            hasil = hasil + '7'
        elif list1[i] + list1[i+1] == '79':
            hasil = hasil+ '8'
        elif list1[i] + list1[i+1] == '80':
            hasil = hasil+ '9'
        else:
            p = int(list1[i])
            q = int(list1[i+1])
            huruf = chr(((p-1)*5+q+96))
            if (ord(huruf)-96 >= 10):
                huruf = chr(((p-1)*5+q+96+1))
            huruf1 = str(huruf)
            hasil = hasil + huruf1
    return hasil

#buka file yg ingin di dekripsi
f = open(inputfile,'rb+')
ch=f.read()
file_dekripsi=str(ch,'utf-8').lower()
print(file_dekripsi)

#hitung kata
jumlah_kata = 0
with open(inputfile, 'r') as nn:
    for line in nn:
        kata = line.split()
        jumlah_kata += len(kata)

#Proses dan output
if jumlah_kata >= 50:
    hasil_dekripsi_pol = decryptpolybius(file_dekripsi)
    hasil_dekripsi_vig = decryptorvigenere(hasil_dekripsi_pol,key)
    hasildecyrptor1 = hasil_dekripsi_vig.encode()
    print(hasil_dekripsi_vig)
    with open (simpan, 'wb') as encrypted_file:
        encrypted_file.write(hasildecyrptor1)
else :
    print('masukan dokumen lebih banyak kata lagi')

