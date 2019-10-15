import os
import requests
from colorama import init, Fore
from argparse import ArgumentParser
from urllib3.exceptions import InsecureRequestWarning
from Wappalyzer import Wappalyzer, WebPage

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

init(autoreset=True)


def adjustURL(url):
    if not (url.split("/")[0] == "http:" or url.split("/")[0] == 'https:'):
        url = "http://" + url

    return url


def ifWordpress(salida, url):
    isWordpress = False

    if int(salida.count('WORDPRESS')) != 0:
        isWordpress = True

    try:
        if requests.get(os.path.join(url + "/wp-admin"), verify=False, timeout=20).status_code == 200:
            isWordpress = True

        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        salida = str(wappalyzer.analyze(webpage)).upper().split(" ")

        if int(salida.count('WORDPRESS')) != 0 or "U'WORDPRESS'," in salida:
            isWordpress = True

    except Exception as e:
        pass
        #print(Fore.RED + "ERROR")

    return isWordpress


def main():
    argp = ArgumentParser(description="Web Clasifier")

    argp.add_argument('-f', '--file', dest='FileName', help='File to analyze')
    argp.add_argument('-u', '--url', dest='url', help='URL to analyze')

    args = argp.parse_args()

    COMMAND = 'whatweb '

    if args.url:

        url = adjustURL(args.url)
        COMMAND += + url

        salida = os.popen(COMMAND).read()
        salida = str(salida).upper()

        if ifWordpress(salida, url):
            print(url + ' ----> ' + Fore.GREEN + 'Wordpress detected')

        else:
            print(url + ' ----> ' + Fore.RED + 'Wordpress not detected')

    if args.FileName:

        archivo = open(args.FileName, 'r')
        urls = archivo.readlines()

        for url in urls:
            url = url.split("\n")[0]
            url = adjustURL(url)

            Comando = COMMAND + url

            salida = os.popen(Comando).read()
            salida = str(salida).upper()

            print url + ' ----> ',
            if ifWordpress(salida, url):
                print(Fore.GREEN + 'Wordpress detected')

            else:
                print(Fore.RED + 'Wordpress not detected')


if __name__ == '__main__':
    main()
