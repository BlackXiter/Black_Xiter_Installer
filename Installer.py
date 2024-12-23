import os
print('''\033[1;36;40mBlack_Xiter_Hack Installer By Black Xiter
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@iamblackxiter \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/BlackXiter/Black_Xiter_Hack")

os.system("cd ..;chmod +x Black_Xiter_Hack/blackxiter.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Black_Xiter_Hack/blackxiter.py -i wlan0 -K")
