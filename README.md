# Wordpress Detector
_This scripts detects if a page is made with wordpress or not_

  
## Installing 🔧
First clone the repo: 
```
https://github.com/Carliquiss/wordpress_detector
```
Then run the following command to install needed libs:
```
pip3 install -r requirements.txt
```

## Usage ⌨️
The URL is given by the "-u" param: -u url (in format http://www.example.com) 
```
python3 spider.py -u <url>
```
If you want to get the urls from a file just use "-f input_file":
```
python3 spider.py -f <input_file>
```

