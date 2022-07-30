# Flipper Skylanders

This repository store Skylanders Keys to read sector and data of a Skylanders NFC Toys.

Currently under testing.


## How to retrieve the 16 keys 

First we need to read the Skylanders NFC Toy to retrieve its UID, using Flipper Zero or an app that allow you to do that.

![Skylander_UID](https://user-images.githubusercontent.com/22322762/181916763-dfd7f97f-341e-4cc8-898a-5fd77097573f.png)

Then, we need to use the NFC Toys Script <a href="https://nfc.toys/interop-sky.html">"tnp3xxx.py"</a>, to generate the 16 keys which allow us to read sector and data. You can also find it hosted on this repository <a href="scripts/tnp3xxx.py">here</a>

```
┌──(v0lk3n㉿lab)-[~]
└─$ python2 tnp3xxx.py 2453be1f
4b0b20107ccb
ba50b997d1b8
9c3d6dc4067b
0f0b876ded9a
43d12fca431d
d0e7c563a8fc
f68a11307f3f
65bcfb9994de
fd08aad6c9d1
6e3e407f2230
4853942cf5f3
db657e851e12
97bfd622b095
04893c8b5b74
22e4e8d88cb7
b1d202716756
```

Then add those 16 keys to you'r "/nfc/assets/mf_classic_dict_user.nfc" file.

I'm adding my keys for each of my own Skylanders Toys into this file <a href="/nfc/assets/skylanders_dict.nfc">here</a>. Feel free to contribute for skylanders owner! 

At the moment of writing, the flipper zero ignore the tag and doesnt run the dictionnary attack, but a pull request was mad yesterday to implement it, feel free to follow it : https://github.com/flipperdevices/flipperzero-firmware/pull/1497

## Ressources 

<a href="https://nfc.toys/interop-sky.html">[NFC Toys] Skylanders Interoperability</a>
<a href="https://nfc.toys/data-giants.html">[NFC Toys] Skylanders Data Analyse</a>
<a href="https://nfc.toys/prac-keys.html">[NFC Toys] Key Generation</a>
<a href="">[NFC Toys] Writing Your Own Data to Skylanders</a>
<a href="http://con-mod.com/skylanders-nfc/">[Con Mod] Clonning Skylanders NFC !!! NO HTTPS</a>
