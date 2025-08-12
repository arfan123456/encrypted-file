import marshal
import sys
import time
import os
os.system("clear")
print("\n\n\n\n\n")
a="\t\tSystem loading..."
for c in a:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(2)
os.system("clear")
print("\n\n\n\n\n")
a="\t\t\033[1;32mSuccesfully loaded!!!!"
for c in a:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
n=input("\n\t\t\033[1;35mYour Name: ")
a="\t\t\033[1;33mHey!\033[1;32m"+n+", \033[1;33mBe Ethical..."
for c in a:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n")
time.sleep(2)
os.system("clear")
print("""\033[1;36m

\t\t_____________  _________ 
\t\t__  ___/__   |/  /__    |
\t\t_____ \__  /|_/ /__  /| |
\t\t____/ /_  /  / / _  ___ |
\t\t/____/ /_/  /_/  /_/  |_|
                         
\033[1;33m
\t=========================================
\033[1;33m
\t\tOwner : SMA
\t\tGithub : Something
\t\tFacebook: SMA
\t\tUse only for educational puposes
\033[1;33m
\t=========================================
""")
inp=input("\t\033[1;36mEnter File Path: ")
out=input("\t\033[1;34mFile Output Name: ")
f=open(inp,"r")
f=f.read()
comp=compile(f," ","exec")
com=marshal.dumps(comp)
new=open(out,"w")
new.write(f"import marshal\nexec(marshal.loads{repr(com)})")