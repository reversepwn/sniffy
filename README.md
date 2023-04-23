# sniffy
A terminal IP sniffer
## Usage
### Getting the code
To get the actual code and get started with further installing run this:
```git clone https://github.com/reversepwn/sniffy```
```cd sniffy```
(you need to have git installed, check how to install git [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
### Installing all the requirements
```bash 
pip3 install -r requirements.txt
```
### Running
```
python3 sniffy.py <ip> <option> <interface>
```
**Example:**
```
python3 sniffy.py 127.0.0.1
```
You can use the option `--more` to get more output then just the send/recive things. 

You can specify the specific interface to sniff for

**Example:**
```
python3 sniffy.py 127.0.0.1 --more en0
```

## People
People who have developer/contributed to this project
- [Kevin Alavik (aka puffer)](https://github.com/kevinalavik)
