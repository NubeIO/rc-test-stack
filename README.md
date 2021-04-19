# rc-test-stack

test stack


```
stty -F /dev/ttyAMA0 38400 -cstopb -parenb && cat /dev/ttyAMA0
modpoll -m rtu -p none -b 38400 -a 64 -t 3:float -r 1 -l 5000 /dev/ttyXBEE-2
modpoll -m rtu -p none -b 9600 -a 1 -t 3:float -r 2 -l 2000 /dev/ttyRS485-1
modpoll -m rtu -p none -b 9600 -a 1 -t 3:float -r 2 -l 2000 /dev/ttyRS485-2
```


```
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```