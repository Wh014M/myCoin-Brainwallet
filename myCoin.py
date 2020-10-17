# myCoin brainwallet
# Created by A. Petek

import hashlib
import os
import random
import binascii
import ecdsa
import base58
import PySimpleGUI as sg
import pyperclip
import webbrowser
import requests
from json import (load as jsonload, dump as jsondump)
from os import path
import json
import blockcypher


def sal():
    return binascii.hexlify(os.urandom(512)).decode('utf-8')

def seed(f, salt):
    p = f+ ' ' +salt
    return hashlib.sha256(p.encode("utf-8")).hexdigest()



def pub_key(secret_exponent):
    key = binascii.unhexlify(secret_exponent)
    s = ecdsa.SigningKey.from_string(key, curve = ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')

def addr(public_key):
    output = []; alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
    var = '00' + var.hexdigest() + hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()[0:8]
    count = [char != '0' for char in var].index(True) // 2
    n = int(var, 16)
    while n > 0:
        n, remainder = divmod(n, 58)
        output.append(alphabet[remainder])
    for i in range(count): output.append(alphabet[0])
    return ''.join(output[::-1])

def wif(secret_exponent):
    var80 = "80"+secret_exponent
    var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
    return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))), 'utf-8')


def bala(address):
    return blockcypher.get_total_balance(address)

def over(address):
    return blockcypher.get_num_confirmed_transactions(address)



SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window




        
def create_main_window(settings):
    sg.theme(settings['theme'])
    menu_def = [['&Menu', ['&Copy', '&Paste','&Settings', 'E&xit']],
                ['&Help', '&About...']]

    right_click_menu = ['Unused', ['&Copy', '&Paste','Settings', 'E&xit']]

    layout =  [[sg.Menu(menu_def)],
               [sg.Image('bit.png'), sg.Text('', size=(20,1)), sg.Button('', key='paypal', size=(12,1), font=('Helvetica', 9), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                           image_filename='paypal.png', image_size=(80, 50), image_subsample=2, border_width=0),
                 sg.Button('', key='bitcoin', size=(12,1), font=('Helvetica', 9), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                           image_filename='bitcoin.png', image_size=(80, 60), image_subsample=2, border_width=0)],   
               [sg.Output(size=(76, 10), font=('Helvetica', 11), key='out')],
               [sg.Text('Enter seed phrase or to overview address:', font=('Helvetica', 8), size=(15,1))],
               [sg.Multiline(size=(76,3), font=('Helvetica', 11), key = 'gen')],
               [sg.Button('Generate wallet', font=('Helvetica', 11)),sg.Button('Overview address', font=('Helvetica', 11))]]

    return sg.Window('myCoin',
                     layout=layout,
                     default_element_size=(30, 2),
                     font='Helvetica 18',
                     right_click_menu=right_click_menu)
def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read()
        f = values['gen'].rstrip()
        if event in (None, 'Exit'):
            break

        elif event == 'Generate wallet':
            salt = sal()
            secret_exponent = seed(f, salt)
            public_key = pub_key(secret_exponent)
            address = addr(public_key)
            WIF = wif(secret_exponent)
            balance = bala(address)
            overv = over(address)
            data = open("myCoin-Wallet.docx","a")
            data.write("myCoin-Wallet: "+"\n\n" +
                       "Seed phrase + salt: " +str(f)+' '+str(salt)+"\n\n"+
                       "Privatekey: " +str(secret_exponent)+"\n\n"+
                       "Publickey:  " + str(public_key)+"\n\n"+
                       "WIF:        " +str(WIF)+"\n\n"+
                       "Address:    "+str(address)+"\n\n"+
                       "Balance:    "+str(balance)+' '+'btc'+"\n\n"+
                       "Transactions:  " +str(overv)+"\n"+
                       '-------------------------------------------------------------------------------------------------------------'+"\n\n")
            data.close()
            print("Seed phrase + salt:  " +str(f)+ ' ' +str(salt)+"\n"+
                  "Privatekey:      " +str(secret_exponent)+"\n"+
                  "WIF:                " +str(WIF)+"\n"+
                  "Address:         "+str(address)+"\n"+
                  "Balance:          "+str(balance)+' '+'btc'+"\n"+
                  "Transactions:  " +str(overv)+"\n")

        elif event == 'Overview address':
            d = blockcypher.get_address_overview(f)
            print(d)
                  
        elif event == 'Copy':
            pyperclip.copy(str(f))
            pyperclip.paste()

        elif event == 'Paste':
            text = pyperclip.paste()
            window.Element('gen').Update(str(text))

        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)

        elif event == 'About...':
            sg.popup('About:', 'Created by A. Petek', 'myCoin bitcoin brainwallet', 'Version 1.1',)

        elif event == 'paypal':
            webbrowser.open_new_tab("https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=PFB6A6HLAQHC2&source=url")
        
        elif event == 'bitcoin':
            webbrowser.open_new_tab("https://commerce.coinbase.com/checkout/149a6235-ec7e-4d3b-a1ae-b08c4f08b4f6")



    window.Close()    

main()

