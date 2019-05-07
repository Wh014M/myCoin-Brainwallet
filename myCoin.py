# -*- coding: utf-8 -*-
# Made by Adrijan Petek
# myCoin-Bitcoin-BrainWallet



try:
    import binascii, ecdsa, time, hashlib, base58, blocksmith, os, random
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'base58==1.0.0'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'ecdsa==0.13'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'blocksmith'])

def print_menu():
    print("""
|************************Menu**************************|
| Coded by Adrijan Petek                               |
|               _                            _         | 
| __      _____| | ___ ___  _ __ ___   ___  | |_ ___   | 
| \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | 
|  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | 
|   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  | 
|                           ____      _                | 
|          _ __ ___  _   _ / ___|___ (_)_ __           | 
|    _____| '_ ` _ \| | | | |   / _ \| | '_ \ _____    | 
|   |_____| | | | | | |_| | |__| (_) | | | | |_____|   | 
|         |_| |_| |_|\__, |\____\___/|_|_| |_|         | 
|                    |___/  _ _      _                 | 
|            __      ____ _| | | ___| |_               | 
|            \ \ /\ / / _` | | |/ _ \ __|              | 
|             \ V  V / (_| | | |  __/ |_               | 
|              \_/\_/ \__,_|_|_|\___|\__|              | 
|------------------------------------------------------|
“We only have what we give.” - Isabel Allende

Donate: BTC - 13vdSzghad1KWymvMDDPixN3ktdkZWaS7f
        ETH - 0x2b6F5a72f7825bC5a2698681CE7a8c0da49AF75c

Your wallet will be saved in txt file!
 1) Bitcoin Wallet
 2) Ethereum Wallet
 0) Exit
 """)
    
loop = True


while loop:
    print_menu()
    menu = int(input("Choose your wallet: "))
    bip39 = 'BIP0039.txt'
    message = os.urandom(8)
    file = open(bip39, "r")
    with file as f:
        words = f.read().split()
        for word in words:
            sent = [random.choice(words)
                    for word in range(int(menu))]
        secret = ' '.join(sent)
    
    if menu == 1:
        print ("Menu 1 has been selected - Bitcoin Wallet")
        phrase = input("Enter your uniqe 12/15/18/21/24/25/26 mnemonic code here: ")
        print("|*******************************************************Bitcoin-Wallet**************************************************************************|"+"\n"+"\n")
        privatekey = hashlib.sha256(phrase.encode('utf-8')).hexdigest()
        key = binascii.unhexlify(privatekey)
        s = ecdsa.SigningKey.from_string(key, curve = ecdsa.SECP256k1)
        publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        c = '0'; byte = '00'; zero = 0
        var = hashlib.new('ripemd160')
        var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
        a = (byte + var.hexdigest())
        doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
        address = a + doublehash[0:8]
        for char in address:
            if (char != c):
                break
            zero += 1
        zero = zero // 2
        n = int(address, 16)
        output = []
        while (n > 0):
            n, remainder = divmod (n, 58)
            output.append(alphabet[remainder])
        count = 0
        while (count < zero):
            output.append(alphabet[0])
            count += 1
        address = ''.join(output[::-1])
        var80 = "80"+(privatekey) 
        var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
        WIF = str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))))
        file = open("Bitcoin Wallet.txt","a")
        file.write("We only have what we give." + "- Isabel Allende" + "\n" + "Donate: BTC - 13vdSzghad1KWymvMDDPixN3ktdkZWaS7f" + "\n"+ "ETH - 0x2b6F5a72f7825bC5a2698681CE7a8c0da49AF75c"+"\n"+"\n"+"\n")
        file.write("Mnemonic: " + " " + str(phrase) + "\n" + "Privatekey: " + " " + str(privatekey) + "\n" + "Publickey: " + " " + str(publickey) + "\n" + "Address: " + " " + str(address) + "\n" + "WIF: " + str(WIF) + "\n" + "\n")
        file.close()
        print("Mnemonic:    " + " " + str(phrase) + "\n" + "Privatekey: " + " " + str(privatekey) + "\n" + "Publickey:  " + " " + str(publickey) + "\n" + "Address:    " + " " + str(address)+ "\n" + "WIF:         " + str(WIF) + "\n" + "\n")

    if menu == 2:
        print("Menu 2 has been selected - Ethereum Wallet")
        phrase = input("Enter your uniqe 12/15/18/21/24/25/26 mnemonic code here: ")
        print("|*******************************************************Ethereum-Wallet**************************************************************************|"+"\n"+"\n")
        secret = hashlib.sha256(phrase.encode('utf-8')).hexdigest()
        address = blocksmith.EthereumWallet.generate_address(privatekey)
        checksum_address = blocksmith.EthereumWallet.checksum_address(address)
        print("Phrases:     " + str(phrase) + "\n" + "\n" + "Privatekey: " + " " + str(privatekey)+ "\n" + "Address:    " + " " + str(address)+ "\n" + "Checksum_a: "+ " " +str(checksum_address)+"\n"+"\n")
        file =  open("Ethereum Wallet.txt","a")
        file.write("We only have what we give." + "- Isabel Allende" + "\n" + "Donate: BTC - 13vdSzghad1KWymvMDDPixN3ktdkZWaS7f" + "\n"+ "ETH - 0x2b6F5a72f7825bC5a2698681CE7a8c0da49AF75c"+"\n"+"\n"+"\n")
        file.write("Phrases: " + str(phrase) + "\n" + "Privatekey: " + " " + str(privatekey)+ "\n" + "Address:    " + " " + str(address)+ "\n" + "Checksum_a: "+ " " +str(checksum_address)+"\n"+"\n")
        file.close()

    elif menu == 0:
        break
        loop=False




                                  
          
