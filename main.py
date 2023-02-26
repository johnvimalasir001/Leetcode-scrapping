from bs4 import BeautifulSoup
import requests

url = requests.get('https://leetcode.com/johnvimalasir/').text
soup = BeautifulSoup(url,'lxml')
info = soup.find('div',class_='mx-auto mt-[50px] w-full grow p-4 md:mt-0 md:max-w-[888px] md:p-6 lg:max-w-screen-xl')
name = info.find('div',class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text
solved_problems=info.find('div',class_='text-[24px] font-medium text-label-1 dark:text-dark-label-1').text
easy = info.find('span',class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1').text
medium= info.find('span',class_= 'mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1').text
hard= info.find('span',class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1').text


print(f'Name:{name}\nSolved Problems:{solved_problems}\nEasy:{easy}\nMedium:{medium}\nHard:{hard}\n\n')