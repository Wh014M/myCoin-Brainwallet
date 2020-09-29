# my Coin Bitcoin brainwallet 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/adrijano/myCoin-Brainwallet/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/adrijano/myCoin-Brainwallet/graphs/commit-activity)

![myCoin](myCoin.gif)

![Adrijan's github stats](https://github-readme-stats.vercel.app/api?username=adrijano&show_icons=true)

[![paypal](https://svgshare.com/i/Q0_.svg)](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=PFB6A6HLAQHC2&source=url)  [![Bitcoin](https://svgshare.com/i/PzX.svg)](https://commerce.coinbase.com/checkout/149a6235-ec7e-4d3b-a1ae-b08c4f08b4f6)

# If you like it give it a star

[![GitHub stars](https://img.shields.io/github/stars/adrijano/myCoin-Brainwallet.svg?style=social&label=Star&maxAge=0)](https://github.com/adrijano/myCoin-Brainwallet/)

**Programmed in Python | PySimpleGUI**

# How it works
```
Salt is created with os.urandom(512) 1024 long character length, bit lenght 4096, character type hexidecimal. So therefore, the program can make unique wallets.

From seed phrase and salt everytime create different bitcoin
privatekey and then convert it to Wallet Interchange Format key (WiF) format, 
which is a Base-58 form for the random key. 
This is the format that is stored in the Bitcoin Wallet. 


For example a sample private key is generated from:

seed phrase and salt: alfanumerico bca40802fc9634650614943a5238d0c54711433e95223f4dba73e55a4f47216d7202fefe35485feee98c0311cfa949abd3466026f099ff7151df44f64ad4c5b54470884004a54c3b3433fcf6c0a87d20ff987614ddd61b32d11a898a2151b82c0f9659a05b7badf4a16c75e7e9c89cfbdabf7b3b20361d49b5d30cd5e648f688ed7015d0be362f44a28623cb63bea7e21dda848557eaefc386a9eba95524a0570500bc14f363aee006e9a234b81f005b389a29f80c205c1e3ecaa344eba6050173aefe29198fd8c89c9b9f1d60d0226b8b5d38b800360e94da7ee6b1700c5eb2c6934cc7d3deaf85433b151daa3308dfb249823b8924cbd524c630d04b8967c52f4d509e450f85a7e6936908b29746e9e7ce5e1c0fc1d4414a277df7e67ef9d942816a61fa61d1b0aa2e04f5e4a6ef928a81cc394e181dc77e7e085d155ab290a19e444f3f2bd4b06f78f46b875b68026672b3f9bddf72f79c1b1ae1823c1451b853634f8eb2aa3640699c1bd570a954c4a382b82907b21b6f7d3166609f65cf387c00725251fdb28a99a4a47ccab2fee5e98a9cd8eff83591c07fd498ffdf047a42682e40818da931b7e301fab5b1068f2ec518c7c0b096ea9a4175281e94a5a0725afbcce91db750cbbb9d93ad38369257e62fc7556d81090959c78438e9c644f9a92518848d1d06e2fa5aad4611f1eb3c932cbf4f5b4fc523fe554e8d5ac4


Privatekey:  

ab28b47420db5808c755a6b9bfa6625bfd5d7906466eed3395c5a63415676872



We then convert this into WiF format (Base-58):

5K7fcFMxR5jUvQRkAEwHVnBatXcu2i2PMfDzviFGJJVjL5zYN7V

This can be stored in a Bitcoin wallet. Next we can take then private key and a 
hash value, and covert it into a useable Bitcoin address, such as:

16P2ACQ1c3ETy3D1eSgRGViQ1taRBs16Jo

The format of the keys is defined below, where we create a 256-bit private key 
and convert this to a WiF private key. Next we generate a 512-bit public key, 
and then take a 160-bit RIPEM-160 hash and convert to a Bitcoin address.
```
### Address overview
```
Paste address and click Overview address you want.

```
# How to use

### Python3+
```
git clone https://github.com/adrijano/myCoin-Brainwallet.git

cd myCoin-Brainwallet && pip install -r requirements.txt

python3 myCoin.py
```
## Sample

**myCoin-Wallet is saved in myCoin-Wallet.docx**

```
-------------------------------------------------------------------------------------------------------------------------------

myCoin-Wallet: 

Seed phrase + salt: alfanumerico bca40802fc9634650614943a5238d0c54711433e95223f4dba73e55a4f47216d7202fefe35485feee98c0311cfa949abd3466026f099ff7151df44f64ad4c5b54470884004a54c3b3433fcf6c0a87d20ff987614ddd61b32d11a898a2151b82c0f9659a05b7badf4a16c75e7e9c89cfbdabf7b3b20361d49b5d30cd5e648f688ed7015d0be362f44a28623cb63bea7e21dda848557eaefc386a9eba95524a0570500bc14f363aee006e9a234b81f005b389a29f80c205c1e3ecaa344eba6050173aefe29198fd8c89c9b9f1d60d0226b8b5d38b800360e94da7ee6b1700c5eb2c6934cc7d3deaf85433b151daa3308dfb249823b8924cbd524c630d04b8967c52f4d509e450f85a7e6936908b29746e9e7ce5e1c0fc1d4414a277df7e67ef9d942816a61fa61d1b0aa2e04f5e4a6ef928a81cc394e181dc77e7e085d155ab290a19e444f3f2bd4b06f78f46b875b68026672b3f9bddf72f79c1b1ae1823c1451b853634f8eb2aa3640699c1bd570a954c4a382b82907b21b6f7d3166609f65cf387c00725251fdb28a99a4a47ccab2fee5e98a9cd8eff83591c07fd498ffdf047a42682e40818da931b7e301fab5b1068f2ec518c7c0b096ea9a4175281e94a5a0725afbcce91db750cbbb9d93ad38369257e62fc7556d81090959c78438e9c644f9a92518848d1d06e2fa5aad4611f1eb3c932cbf4f5b4fc523fe554e8d5ac4

Privatekey: ab28b47420db5808c755a6b9bfa6625bfd5d7906466eed3395c5a63415676872

Publickey:  048e93a34054617f1807ffe3fa99f36b2520ab459a6ac1e51cb8aef46c75970e735c55a6bbfed8ab596b3b8abdf3c9f5315ef93e2387390719638d2cef5b58e1b9

WIF:        5K7fcFMxR5jUvQRkAEwHVnBatXcu2i2PMfDzviFGJJVjL5zYN7V

Address:    16P2ACQ1c3ETy3D1eSgRGViQ1taRBs16Jo

Balance:    0 btc

Transactions:  0
-------------------------------------------------------------------------------------------------------------------------------

myCoin-Wallet: 

Seed phrase: correct horse battery staple 26095e53cf5dcee90c1c0d407f6b235ec94513777f7c5262116bac461a75d6cb62a5cc12c2dce13c1e9ee68d7340845573a80da91825e5a8a2f2d40b909cb14bfd3ab95c7917d6d0374ad23819c11b6f3335ccfeb319303bc08df0cf56633f4dcc890a643a3bad68fc764b002086ab55961176549f8badde8f16178384c43dca221924310b92af0f5adf2e546b37f172585c336b69b8ba59ea33187e96f8d644bcdc3d1003e81305338ef373c33a1496a98b4367042ca245ddc994ddf5a12be42410c99b69137b42c46184a895843e98a574a1e595db463c97fa3e699c974834403230ead00193ea2a0a170c981989d7a037ca8acb7a69143aa60b7d8beb449cdd53407f868f75fc93f7f922eb5bf503265f35bd2ab27537fc4b818776aa45bd4de8a1388ffa3d06deb404efe3f020000b75246dfd0db384ad5580959ac8909d66016e55a89edc2d22d306c785e1bfb253ee50b6ff7a098c1e898809249a9fd8e84a5db587d7807676f73ff0daeb5f5b0a5ec207b04d35d975c98bbc003df268faa55bb1aa71208300edf077ade3f6532f20a77a94431d63a0a9e208bf6d203b6a78ab40fbd45fbf760b67f3d6db9fc7a36e4c019855d18e6707b907fdfb4825a72592ba332a6b8fadcc44dc66b3cba3e14901232f0dfdf9b8dcf3a31fa66cdcdd0edde7cd0248a96b13f1f5c6a1e9cd487bf236c02549ef86c6e64116e81c81

Privatekey: 1f69bcaf86fc3895ac4d3748b0b2c52e3d4590555c382d330af6af1cd51d2cf2

Publickey:  045c5bb68b96d8714c4c71919d9a19092a0cfa36dd0c4b3bf7ee79734a7878abbcfc78f59645284d9bf85d8bea6765809f99fce4d703edfc67a87dba0f2de0d94b

WIF:        5J47z6vhuJcR94o5dBtmqjjVnJ92G9vxdHEPEnNAfZSnKMMJJjW

Address:    1Mr2i1GPYh8BMgV8a9frXrgou83P84fkbn

Balance:    0 btc

Transactions:  0
-------------------------------------------------------------------------------------------------------------------------------

```
![myCoin](Capture1.PNG)
![myCoin](Capture9.PNG)

## Donations
If you would like to support me, donations are very welcome.

```
You can use Paypal to donate using your own credit card. 
The payment is processed by PayPal but you don't need to have a
PayPal account or sign-up for one if you are paying by credit card.

You can also use your own Paypal account to donate.

You can also donate Bitcoin, Bitcoin Cash, Dai, Ethereum, Litecoin and USD Coin.
```
[![paypal](https://svgshare.com/i/Q0_.svg)](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=PFB6A6HLAQHC2&source=url)  [![Bitcoin](https://svgshare.com/i/PzX.svg)](https://commerce.coinbase.com/checkout/149a6235-ec7e-4d3b-a1ae-b08c4f08b4f6)




# Disclaimer


**The code within this repository comes with no guarantee, the use of this code is your responsibility. I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.**


[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/adrijano/myCoin-Brainwallet/)

