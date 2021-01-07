import requests
from bs4 import BeautifulSoup


en_fr_pair = 'english-french'
fr_en_pair = 'french-english'
current_pair = ''
user_agent = 'Mozilla/5.0'

print('Type "en" if you want to translate from French into English, '
      'or "fr" if you want to translate from English into French:')
lang = input()
if lang == 'en':
    current_pair = fr_en_pair
else:
    current_pair = en_fr_pair

print('Type the word you want to translate:')
word_to_translate = input()

print(f'You chose "{lang}" as a language to translate "{word_to_translate}".')

url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
r = requests.get(url, headers={'User-Agent': user_agent})
print(str(r.status_code) + ' OK')
print('Translations')

soup = BeautifulSoup(r.text, 'html.parser')
word_translations_list = soup.find_all('a', class_='translation')
word_translations_list = [t.text.strip() for t in word_translations_list]
sentences_list = soup.find_all(class_='text')
sentences_list = [t.text.strip() for t in sentences_list]

print(word_translations_list)
print(sentences_list)
