set -e
os=$(uname)
if [ "$os" = "Darwin" ]; then
 echo "Do you have "xcrun: error: invalid active developer path"?(Y/n)"
 read $varname
 if [ "$varname" = "Y" ] || [ "$varname" = "y" ]; then
  xcode-select --install
 fi
 which -s brew
 if [[ $? != 0 ]] ; then
    # Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  fi
 brew install libimobiledevice libusbmuxd git python@3.11 wget && python3 -m pip install pyimg4
 if ! python3 -c 'import customtkinter; exit(not customtkinter.find_loader("customtkinter"))' ||  ! python3 -c 'import PIL; exit(not PIL.find_loader("Pillow"))'; then
  pip3 install customtkinter Pillow
 fi
 echo "all done!"
fi
if [ "$os" = "Linux" ]; then 
 if [ "$EUID" -ne 0 ]; then
  echo "Please run with SUDO (as root)"
  exit
  fi
 if [[ -f "/etc/lsb-release" || -f "/etc/debian_version" ]]; then
  echo "Linux Ubuntu detected and is supported"
  sudo add-apt-repository universe && sudo apt-get update && sudo apt install libimobiledevice-utils libusbmuxd-tools git curl python3-pip unzip clang -y && python3 -m pip install pyimg4 && pip install requests remotezip pyimg4 pyqt5 applescript && sudo apt-get install python3-tk && sudo apt-get install python3-pil python3-pil.imagetk && sudo wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb && sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb && sudo rm libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb
  fi
 if ! python3 -c 'import customtkinter; exit(not customtkinter.find_loader("customtkinter"))' || ! python3 -c 'import PIL; exit(not PIL.find_loader("Pillow"))'; then
  sudo pip3 install customtkinter Pillow
 fi
fi


