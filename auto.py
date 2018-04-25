import subprocess
import sys
import pexpect
import re

def makeAccount():
    process = pexpect.spawn('geth account new')
    process.expect("assphrase:")
    process.sendline("1234qwer")
    process.expect("assphrase:")
    process.sendline("1234qwer")
    account = process.read().split("{")[1].split("}")[0]
    return account

def editJson(account):
    with open('genesis.json') as genesis:
            lines = genesis.readlines()
    lines[10] = str(re.sub('0x(.*)',"0x"+account+"\": {", lines[10]))
    with open('genesis.json', 'w') as genesis:
        genesis.writelines(lines)

account = makeAccount()
editJson(account)
