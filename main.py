import requests
import csv
from bs4 import BeautifulSoup

words_groups = ['A-B', 'C-D', 'E-G', 'H-K', 'L-N', 'O-P', 'Q-R', 'S', 'T', 'U-Z']

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition std-1)', }
)

word_list = []
for group in words_groups:
    print(f'group: {group}')
    for page_num in range(1, 6):
        print(f'page: {page_num} in group: {group}')
        URL = f"https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_{group}/page={page_num}"
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        words = soup.find('div', id='entrylist1')
        for li in words.find_all('li'):
            word_list.append(li.get_text()[1:-1])
            print(f'word "{li.get_text()[1:-1]}" added to list')

with open('oxford3000.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for word in word_list:
        writer.writerow([word])


