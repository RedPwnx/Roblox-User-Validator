import requests, random, os, fade, string
from colorama import Fore, init
import threading
lock = threading.Lock()
google = 'https://google.com'
api = "https://auth.roblox.com/v1/usernames/validate?birthday=1992-12-31T23:00:00.000Z&context=Signup&username="
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
}
init(autoreset=True)
lb = Fore.LIGHTBLACK_EX
r = Fore.RED
g = Fore.GREEN
colors = [Fore.YELLOW]
mc = random.choice(colors)
xDxddasdsadsadsa = True
UsersList = []
Users2Save = []
proxyCounter = 0
checkProxy = False

def printt(args):
    lock.acquire()
    print(args)
    lock.release()
def userGen():
    UsersList.clear()
    try:
        os.remove('temp.dat')
    except:
        pass
    try:
        os.remove('users.txt')
    except:
        pass
    usercount = int(input(f'{lb}[ {mc}How many users? {lb}]: {mc}'))
    userlength = int(input(f'{lb}[ {mc}Length of each user? {lb}]: {mc}'))
    usercountCounter = 0
    for i in range(int(usercount)):
        usercountCounter += 1
        textList = list(''.join((string.ascii_letters, string.digits, string.digits)))
        userX = ''.join(random.choice(textList) for i in range(int(userlength)))
        print(f'{lb}[{mc} {usercountCounter} {lb}] {mc}{userX}')
        with open('users.txt', 'a+') as file:
            file.write(userX+'\n')
    input('Press Any key to continue..')
    main()
# ------------------------------------ [ Proxy Checker Loader
proxiesList = []
# socks5 = open('proxies.txt', 'r').read().splitlines()
# for proxy2 in socks5:
#     proxiesList.append(f'http://{proxy2}')
# CheckedProxy = []
# ------------------------------------ [ User Checker
def userChecker(userr):
    api = f"https://auth.roblox.com/v1/usernames/validate?birthday=1992-12-31T23:00:00.000Z&context=Signup&username={userr}"
    with open('temp.dat', 'r') as reuserx:
        reuser = reuserx.read().splitlines()
        if userr not in reuser:
            os.system(f'title Roblox User Checker - List: {len(UsersList)} Checked: {userCheckedCounter}')
            Users2Save.append(userr)
            try:
                apires = requests.get(api, headers=head)
                endpoint = apires.json()
                if apires.status_code == 200:
                    if endpoint['code'] == 1:
                        printt(f'{r}[ {userr} ]: ERR')
                    elif endpoint['code'] == 0:
                        printt(f'{g}[ {userr} ]: Found!')
                        with open('found.txt', 'a+') as file:
                            file.write(userr+'\n')
                else:
                    pass
                    printt('Passed')
                    printt(apires.text)
                with open('temp.dat', 'a') as reuser:
                    for line in Users2Save:
                        reuser.write(line + '\n')
                        Users2Save.remove(line)
            except:
                pass

# ------------------------------------ [ Creditsssss
def credits():
    s = requests.Session()
    url2 = "https://pastebin.com/raw/jekV761W"
    r2 = s.get(url2)
    if r2.ok:
        data = r2.text
        disid = data.split(';')[0]
        url = f"https://dashboard.botghost.com/api/public/tools/user_lookup/{disid}"
        r = s.get(url)
        response = r.json()
        if r.ok:
            discordUser = (response['username'])
            return discordUser
    else:
        return "github/xst4"
# ------------------------------------ [ CMD Initialize
def titlee():
    os.system(f'title Roblox User Checker v1')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def userscounter():
    with open('users.txt', 'r') as file:
        for line in file.read().splitlines():
            UsersList.append(line)
def logo():
    logo=f"""
██╗   ██╗███████╗███████╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║███████╗█████╗  ██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝███████║███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
 Roblox User Checker!


"""
    logo2 = ""
    for line in logo.splitlines():
        logo2 += f'{line}'.center(os.get_terminal_size().columns)+'\n'
    print(fade.fire(logo2))
# ------------------------------------ [ Main
def main():
    clear()
    titlee()
    userscounter()
    # proxyCheck()
    logo()
    title = f"{f'by xStrong(Discord: {credits()}) - @Ghostbyte              -           Users List: {len(UsersList)}'.center(os.get_terminal_size().columns)}\n{'╭──────────────────────────────────────────────────────────────────────╮'.center(os.get_terminal_size().columns)}\n{'│                        «1» List Check                                │'.center(os.get_terminal_size().columns)}{'│                        «2» User Generator                            │'.center(os.get_terminal_size().columns)}\n{'╰──────────────────────────────────────────────────────────────────────╯'.center(os.get_terminal_size().columns)}\n"
    print(fade.fire(title))
    while True:
        choice = input(f'{lb}[ {mc}Input Your Choice {lb}]: {mc}')
        if choice == '2':
            userGen()
        elif choice == '1':
            global userCheckedCounter
            userCheckedCounter = 0
            if os.path.exists('temp.dat') == False:
                with open('temp.dat', 'w') as file:
                    file.write("")
                    file.close()
            while xDxddasdsadsadsa:
                if threading.active_count() < 7:
                    try:
                        threading.Thread(target=userChecker, args=(UsersList[userCheckedCounter],)).start()
                        userCheckedCounter += 1
                    except:
                        pass
                    if len(UsersList) <= userCheckedCounter:
                        print(f'{g}[OK] ALL users Saved to Done.txt')

                        break
            break
        else:
            print(f'{r}Err in choice!')
main()
