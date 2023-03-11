# Flipper Infinity Skylanders

This repository stores Skylanders and Disney Infinity A-Keys to read sector and data of Skylanders and Disney Infinity NFC Toys.

Currently under testing.

## Skylanders - How to retrieve the 16 keys 

First, we need to read the Skylanders NFC Toy to retrieve its UID, using Flipper Zero or an app that allows you to do that.

![Skylander_UID](https://user-images.githubusercontent.com/22322762/181916763-dfd7f97f-341e-4cc8-898a-5fd77097573f.png)

Then, we need to use the NFC Toys Script <a href="https://nfc.toys/interop-sky.html">"tnp3xxx.py"</a>, to generate the 16 keys which allow us to read sector and data. You can also find it hosted on this repository <a href="scripts/tnp3xxx.py">here</a>

```
┌──(v0lk3n㉿lab)-[~]
└─$ python3 scripts/tnp3xxx.py 2453be1f
4B0B20107CCB
BA50B997D1B8
9C3D6DC4067B
0F0B876DED9A
43D12FCA431D
D0E7C563A8FC
F68A11307F3F
65BCFB9994DE
FD08AAD6C9D1
6E3E407F2230
4853942CF5F3
DB657E851E12
97BFD622B095
04893C8B5B74
22E4E8D88CB7
B1D202716756
```

Then, add those 16 keys to your "/nfc/assets/mf_classic_dict_user.nfc" file.

## Disney Infinity - How to Retrieve the Key

First, we need to read the Disney Infinity NFC Toy to retrieve its UID, using Flipper Zero or an app that allows you to do that.

Then, we need to use the NFC Toys Script <a href="https://nfc.toys/interop-inf.html">"infsha.py"</a>, to generate the key which allow us to read sector and data. You can also find it hosted on this repository <a href="scripts/infsha.py">here</a>

```
┌──(v0lk3n㉿lab)-[~]
└─$ python3 scripts/infsha.py 048376728B3A80
9327436F1966 
```
Then, add the one key to your "/nfc/assets/mf_classic_dict_user.nfc" file.

I'm adding my keys for each of my own Toys into this file <a href="https://github.com/V0lk3n/Flipper-Skylanders/blob/main/nfc/assets/mf_classic_dict_user.nfc">here</a>. Feel free to contribute!

Flipper zero now run the dictionnary attack on the skylanders nfc tags. 
Thanks to this pull request: https://github.com/flipperdevices/flipperzero-firmware/pull/1497

## Resources 

* <a href="https://nfc.toys/interop-sky.html">[NFC Toys] Skylanders Interoperability</a>
* <a href="https://nfc.toys/interop-inf.html">[NFC Toys] Disney Infinity Interoperability</a>
* <a href="https://nfc.toys/data-giants.html">[NFC Toys] Skylanders Data Analysis</a>
* <a href="https://nfc.toys/prac-keys.html">[NFC Toys] Key Generation</a>
* <a href="https://nfc.toys/workflow-sky.html">[NFC Toys] Writing Your Own Data to Skylanders</a>
* <a href="https://nfc.toys/workflow-inf.html">[NFC Toys] Writing Your Own Data to Disney Infinity</a>
* <a href="http://con-mod.com/skylanders-nfc/">[Con Mod] Cloning Skylanders NFC !!! NO HTTPS</a>
