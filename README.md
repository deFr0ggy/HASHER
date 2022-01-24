
<p align="center">
  <img src="https://raw.githubusercontent.com/deFr0ggy/HASHER/main/hasher.png" />
</p>
 
# HASHER v1.0

A simple python script to automate the HASH calculation of files. Currently it calculates the following hashes.

- MD5
- SHA1
- SHA256
- SHA512

## DEPENDENCIES

- HASHLIB - For Calculating Hashes
- COLORAMA - For Color Output.


## USAGE

HASHER is simple to use. All you need is to have Python 3 instaklled on your system.

### CALCULATING HASH OF SINGLE FILE

```
$ python3 Hasher.py hello.txt 


 __  __     ______     ______     __  __     ______     ______    
/\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   /\  == \   
\ \  __ \  \ \  __ \  \ \___  \  \ \  __ \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ v1.0
                                                                    
 An Automated Hash Calculator
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/deFr0ggy 
 LinkedIn: https://linkedin.com/in/kamransaifullah 

 Usage: ./Hasher.py <File>
    
    
MD5: a438474115db37daf9d8e1307c06eb4a
SHA1: 1d6d222b15f3cf2308a6c09ab199fa8ca3f65c66
SHA256: 0b182d7b071d66361a52df8c1484ad183947fa112cc999f36f270ddf8dae56c4
SHA512: 42f0314b3dbd7c8063883f20ca40f76ba470d5af518e95e562a3f304566421c8001d79d48626253d52d6cc3d130b4471588b24f2873610c382d76536c03b6e8b

```
### CALCULATING HASH OF FILES IN A DIRECTORY

```
python3 Hasher.py ../Hasher/


 __  __     ______     ______     __  __     ______     ______    
/\ \_\ \   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   /\  == \   
\ \  __ \  \ \  __ \  \ \___  \  \ \  __ \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ v1.0
                                                                    
 An Automated Hash Calculator
 ------------------------------
 Coded by Kamran Saifullah - Frog Man
 Twitter: https://twitter.com/deFr0ggy 
 GitHub: https://github.com/deFr0ggy 
 LinkedIn: https://linkedin.com/in/kamransaifullah 

 Usage: ./Hasher.py <File>
    
    
File Name:  README.md

MD5: 5370cbcac5b556870c5f2f3443c77e0c
SHA1: e8e1e415a5257c775f1e71ad3428e91e65601aec
SHA256: 2b341f092cad0ffc2a0f877196931937e0e02abc4afdd8b81f4a8c4076576942
SHA512: 33d7544250f96e1ccecf2c898693e348e9c278a12908763abaf570009d67a25e45d206f60b75aca85e4cf75d8160884ef7b2a21f6fd44d6000fd586e36deea87

File Name:  Hasher.py

MD5: fd70145a805b555eb032f865273db82c
SHA1: a884d62f66c734bf65bcc52240c781752156bee5
SHA256: b50b036c666d4235c1b558a3a128444b47723f585b251bbdf7f8adec5a84b5d6
SHA512: c26f0147d8aac7e8d735229a61fc3965db2abaef8a61a20b9353800a9e503c16e81bd82bc84814d3de7adbafb5ff2a0ecbcadf3884def96dcf9c3269f7360398
```