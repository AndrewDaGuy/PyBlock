import platform
import sys
import datetime
import time
import re


class colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'


regex = "^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}"

print(f"{colors.header}PyBlock{colors.end}")
print(f"{colors.bold}===================={colors.end}")
print()

# Default to windows settings
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redir = "127.0.0.1"

# Check OS and apply settings

if platform.system == "":
    print(f"{colors.red}Sorry but your system is not supported.{colors.end}")
    sys.exit()

else:
    if platform.system() == "Windows":
        hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        redir = "127.0.0.1"
    else:
        if platform.system() == "Darwin":
            hostsPath = r"`/private/etc/hosts`"
            redir = "0.0.0.0"
        else:
            if platform.system() == "Linux":
                hostsPath = r"/etc/hosts"
                redir = "192.168.1.10"
            else:
                print(
                    f"{colors.red}Sorry but your system is not supported.{colors.end}")
                sys.exit()


# Ask for input
website = input(f"{colors.yellow}Domain to block > {colors.end}")

if website == "":
    print(f"{colors.red}Please enter a vaild domain.{colors.end}")
    sys.exit()

if not re.search(regex, website):
    print(f"{colors.red}Please enter a vaild domain.{colors.end}")
    sys.exit()

if website.startswith("www."):
    website = website.strip("www.")

# Write to file
try:
    with open(hostsPath, 'r+') as file:
        content = file.read()
        if website in content or "www." + website in content:
            # Skip already-set websites
            print(f"{colors.green}Website already in host file.{colors.end}")
            sys.exit()
        else:
            file.write(f"{redir} {website} www.{website} \n")
            print(f"{colors.green}Added to host file!{colors.end}")
            sys.exit()

except Exception as err:
    print(f"{colors.red}There was an error while accessing the file, check if you have permissons first.{colors.end}")
    print()
    print(err)
    sys.exit()
