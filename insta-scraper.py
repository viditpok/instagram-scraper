import instaloader

BLUE = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

bot = instaloader.Instaloader()

username = input("Enter your username: ")
password = input("Enter your password: ")
bot.login(username, password)

profile = instaloader.Profile.from_username(bot.context, username)

print(f"\n{BLUE}{BOLD}Username{END}: {profile.username}")
print(f"{BLUE}{BOLD}User ID{END}: {profile.userid}")
print(f"{BLUE}{BOLD}Number of Posts{END}: {profile.mediacount}")
print(f"{BLUE}{BOLD}Followers{END}: {profile.followers}")
print(f"{BLUE}{BOLD}Followees{END}: {profile.followees}\n")
