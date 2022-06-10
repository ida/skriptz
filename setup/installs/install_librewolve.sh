# https://librewolf.net/installation/debian/ (January 2022)

echo "deb [arch=amd64] http://deb.librewolf.net $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/librewolf.list

sudo wget https://deb.librewolf.net/keyring.gpg -O /etc/apt/trusted.gpg.d/librewolf.gpg

sudo apt update

--->

Hit:2 http://de.archive.ubuntu.com/ubuntu bionic InRelease                                                                                           
Hit:3 http://archive.canonical.com/ubuntu bionic InRelease                                                                                           
Hit:4 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                                                    
Hit:5 http://de.archive.ubuntu.com/ubuntu bionic-updates InRelease                                                                                   
Hit:6 http://ppa.launchpad.net/gezakovacs/ppa/ubuntu bionic InRelease                                                                            
Hit:7 http://archive.ubuntu.com/ubuntu bionic InRelease                                                                                              
Hit:8 http://de.archive.ubuntu.com/ubuntu bionic-backports InRelease                                                                                 
Hit:9 http://ppa.launchpad.net/peek-developers/stable/ubuntu bionic InRelease                                                                        
Ign:1 https://deb.librewolf.net bionic InRelease                                                                               
Err:10 https://deb.librewolf.net bionic Release   
  404  Not Found [IP: 116.203.248.82 443]
  Reading package lists... Done
  E: The repository 'http://deb.librewolf.net bionic Release' does not have a Release file.
  N: Updating from such a repository can't be done securely, and is therefore disabled by default.
  N: See apt-secure(8) manpage for repository creation and user configuration details.)







sudo apt install librewolf -y


