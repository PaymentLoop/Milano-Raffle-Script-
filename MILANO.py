import requests
from random import getrandbits
from bs4 import BeautifulSoup
url = 'https://www.excelsiormilano.com/module/antcontactcustom/sendmail'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


def main(limit):
    for i in range(1,limit):
        session = requests.Session()
        email = 'your_email+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
                    'first_name': '',
                    'last_name' : '',
                    'birth'     : '', #MM-DD-YYYY don't include spaces
                    'mail'      : email, #Dont edit this
                    'number'    : '', #Phone number
                    'size'      : '', # Example: 10, 10 1/2, 11
                    'country'   : '',
                    'state'     : '',
                    'city'      : '',
                    'zip'       : '',
                    'street'    : ''

        }
        resp = session.post(url, data=payload, headers=headers)
        print('Raffle has been entered {}/{} times.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
