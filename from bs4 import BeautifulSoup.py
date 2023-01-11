from bs4 import BeautifulSoup
import requests
import sys

URL = 'https://instagram.com/{}/'

    
def scrap_data(user_name):
    data = requests.get(URL.format(user_name))
    soup = BeautifulSoup(data.text ,'html.parser')

    meta = soup.find('meta',property='og:description')
    s = meta.attrs['content']
    s = s.split('_')[0]
    print(s)



if __name__ == '__main__':
    
    try :
        user_name = input('please enter username :')
        scrap_data(user_name)
    except :
        print('User Name Not founded.')
        user_name = input('Please try new User Name :')
        scrap_data(user_name)
    finally:
        sys.exit(1)
