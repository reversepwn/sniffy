# sniffy
A terminal IP sniffer

## Usage

### Installing all the requirements

```bash 
pip3 install -r requirements.txt
```

### Running

```bash
python3 sniffy.py <ip> <option> <interface>
```

**Example:**

```bash
python3 sniffy.py 127.0.0.1
```
You can use the option `--more` to get more output then just the send/recive things. 

You can specify the specific interface to sniff for

**Example:**

```bash
python3 sniffy.py 127.0.0.1 --more en0
```
