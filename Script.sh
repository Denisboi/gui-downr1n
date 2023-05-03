echo "If you're have a error, try to open install.sh"
sleep 2
set -e
os=$(uname)

if [ $os = "Darwin" ]; then
 if [ $EUID = 0 ]; then
 cp /dev/null d.txt
 echo "D" > d.txt
 sudo python3 ./gui-downgrade.py
 rm d.txt
 else 
  echo "Please run with a sudo"
  sleep 2
 fi

fi
if [ $os = "Linux" ]; then
 if [ "$EUID" -ne 0 ]; then
 echo "Please run with a sudo"
 sleep 2
 exit
 fi
cp /dev/null d.txt
echo "D" > d.txt
sudo python3 ./gui-downgrade.py
rm d.txt

fi


