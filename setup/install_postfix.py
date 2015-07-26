# Install a mailserver for your Unix-system's users
# =================================================
#
# Terminology
# -----------
#
# In the following the word 'mailserver' will be used as an equivalent for 
# 'Mail Transfer Agent' (MTA), albeit wrong, commonly used to summarize a
# Mail-suite's components.
#
#
# Preamble
# --------
#
# Unixish operating-systems provide by default a mailing-feature for the
# system's users, which out-of-the-box allows the machine's user's to
# communicate with each other within the system. In the following, an example
# on how to additionally install, configure and start a well known mailserver named
# postfix, so mailuser's of external mailservers, can send mails to our users,
# such as 'someusername@yourserverdomain.org'.
#
#
# Usage
# -----
#
# Replace 'yourdomain.org' in the last line, with your machine's domain and run this script in a shell:
#     python install_postfix.py yourdomain.org
#
#
# Epilogue
# --------
#
# Some helpful docs:
# http://www.linux.com/learn/tutorials/308917-install-and-configure-a-postfix-mail-server
# https://vexxhost.com/resources/tutorials/how-to-install-and-setup-postfix-on-ubuntu/
# http://www.postfix.org/BASIC_CONFIGURATION_README.html
# https://help.ubuntu.com/community/Postfix

import os
import shutil

def installPostfix():
    sis = os.sys
    sis('sudo apt-get update -y')
    sis('sudo apt-get upgrade -y')
    sis('sudo apt-get install postfix')

    conftmp = conftmp + '.tmp'
    digest = ''
    LINE_REPLACED = False

def modifyPostfixConf(yourdomain):
    conf = '/etc/postfix/main.cf'
    conf = '/home/ida/etc/postfix/main.cf' # DEV
    with open(conf) as fin, open(conf + '.tmp', 'w') as fout:
        lines = fin.readlines()
        pats_dikt = {'myhostname': 'myhostname = ' + yourdomain + '\n',
                     'mydomain':'mydomain = ' + yourdomain + '\n',
                     'mydestination':'mydestination = $myhostname localhost.$mydomain localhost' + '\n'}
        for line in lines:
            for key, val in pats_dikt.items():
                if line.startswith(key):
                    digest += val
                    LINE_REPLACED = True
            if LINE_REPLACED:
                digest += '# ' + line
                LINE_REPLACED = False
            else:
                digest += line
        fout.write(digest)
        shutil.move(

def startPostfix():
    pass # TODO

def main(yourdomain):
    installPostfix()
    configPostfix(yourdomain)
    startPostfix()

if __name__ == '__main__':
    yourdomain='somedomain.org'
    main(yourdomain)
