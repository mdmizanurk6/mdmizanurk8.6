import os,random,sys,time
os.system("pkg install espeak")
from os import system as _Md MizanurK_
def lo(word):
    Mizanur = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(Mizanur)):
            sys.stdout.write(('\r{}{}').format(str(word), Mizanur[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
	print(f"""\n\033[
███    ███ ██ ███████  █████  ███    ██ ██    ██ ██████      
████  ████ ██    ███  ██   ██ ████   ██ ██    ██ ██   ██     
██ ████ ██ ██   ███   ███████ ██ ██  ██ ██    ██ ██████      
██  ██  ██ ██  ███    ██   ██ ██  ██ ██ ██    ██ ██   ██     
██      ██ ██ ███████ ██   ██ ██   ████  ██████  ██   ██] """)
try:
    import marshal
    os.system('clear')
    lo("     𝙋𝙇𝙕 𝙒𝘼𝙄𝙏...")
    _Md Mizanur K _("clear")
    logo()
    _Md Mizanur K _("espeak \"import your script\"")
    __F = input('\n \033[1;92m╔══[🐼] \033[1;90mInput script path\033[1;91m:\033[1;97m ')
    _Md Mizanur K _(f"espeak \"you choose input {__F}\"")
    O__ = input(' \033[1;92m╚══[🐼] \033[1;90mOut put path\033[1;91m:\033[1;97m ')
    _Md Mizanur K _(f"espeak \"you choose out put {O__}\"")
    try:
        __R = open(__F,'r').read()
    except:
        exit('\n script not found ')
        
    os.system(f'cp {__F} {O__}')
    for _ in range(20):
        cc = open(O__,'r').read()
        data = marshal.dumps(cc)
        _nop_ = open(O__,'w')
        _nop_.write('#_____________________________________\n#|>| THIS TOOL IS ENC BY Md Mizanur K \n#|>|FB_LINK:-https://www.facebook.com/mdmizanurk6\n#|>|WHATS_APP:-+8801774516086\n#_____________________________________\n')
        _nop_.write('import marshal\n')
        _nop_.write(f'exec(marshal.loads({repr(data)}))')
        _nop_.close()
    print(f'\n [•] file saved in: {O__}')
    exit()
except Exception as e:
    exit(e)