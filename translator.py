import requests
from bs4 import BeautifulSoup


current_pair = ''
current_lang = ''
user_agent = 'Mozilla/5.0'
support_languages_dict = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French',
                          6: 'Hebrew', 7: 'Japanese', 8: 'Dutch', 9: 'Polish', 10: 'Portuguese',
                          11: 'Romanian', 12: 'Russian', 13: 'Turkish'}


print("Hello, you're welcome to the translator. Translator supports:")
for key, value in zip(support_languages_dict.keys(), support_languages_dict.values()):
    print(f'{key}. {value}')

print('Type the number of your language:')
my_language = int(input())

print('Type the number of language you want to translate to:')
language_to_translate = int(input())

print('Type the word you want to translate:')
word_to_translate = input()

current_pair = f'{support_languages_dict.get(my_language).lower()}' \
               f'-{support_languages_dict.get(language_to_translate).lower()}'
current_lang = support_languages_dict.get(language_to_translate)


url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
r = requests.get(url, headers={'User-Agent': user_agent})

soup = BeautifulSoup(r.text, 'html.parser')
word_translations_list = soup.find_all('a', class_='translation')
word_translations_list = [t.text.strip() for t in word_translations_list]
sentences_list = soup.find_all(class_='text')
sentences_list = [t.text.strip() for t in sentences_list]

print(f'{current_lang} Translations:')
for translation in word_translations_list:
    print(translation)

print(f'{current_lang} Examples:')
for sentence in sentences_list:
    print(sentence)
