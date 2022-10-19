import os, platform,time
print("\t NOTE : 1ST COPY KEY THEN SENT ME KEY")
os.system('xdg-open https://www.facebook.com/profile.php?id=100076321219909');time.sleep(1.2)
try:

        import requests

except:

        os.system('pip2 install requests')


import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from max import check_my_key

        check_my_key()



elif bit == "32bit":

        print("\t [x] SRY BRO BYPASS NOY SUPPORT")
