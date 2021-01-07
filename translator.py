import requests
import sys
from bs4 import BeautifulSoup


args = sys.argv
current_pair = ''
current_lang = ''
user_agent = 'Mozilla/5.0'
support_languages_dict = {1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French',
                          6: 'Hebrew', 7: 'Japanese', 8: 'Dutch', 9: 'Polish', 10: 'Portuguese',
                          11: 'Romanian', 12: 'Russian', 13: 'Turkish'}
my_language = args[1]
language_to_translate = args[2]
word_to_translate = args[3]

if my_language.capitalize() not in support_languages_dict.values():
    print(f"Sorry, the program doesn't support {my_language}")
    sys.exit(0)
if language_to_translate.capitalize() not in support_languages_dict.values() and language_to_translate != 'all':
    print(f"Sorry, the program doesn't support {language_to_translate}")
    sys.exit(0)

file = open(f'{word_to_translate}.txt', 'a', encoding='utf-8')
if file:
    file.truncate(0)


if language_to_translate != 'all':
    current_pair = f'{my_language}' \
                   f'-{language_to_translate}'
    current_lang = language_to_translate.capitalize()

    url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
    r = ''
    try:
        s = requests.Session()
        r = s.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')

    if int(r.status_code) == 404:
        print(f'Sorry, unable to find {word_to_translate}')
        sys.exit(0)

    soup = BeautifulSoup(r.text, 'html.parser')
    word_translations_list = soup.find_all('a', class_='translation')
    word_translations_list = [t.text.strip() for t in word_translations_list]
    word_translations_list.remove(word_translations_list[0])
    sentences_list = soup.find_all(class_='text')
    sentences_list = [t.text.strip() for t in sentences_list]
    sentences_list = sentences_list[46:]

    print(f'{current_lang} Translations:')
    file.write(f'{current_lang} Translations:\n')
    for translate in word_translations_list:
        print(translate)
        file.write(translate + '\n')
        break
    print()
    file.write("\n")

    print(f'{current_lang} Example:')
    file.write(f'{current_lang} Example:\n')
    j = 0
    for sentence in sentences_list:
        if j == 2:
            break
        print(sentence)
        file.write(sentence + '\n')
        j += 1
    print()
    file.write("\n")
else:
    for language in support_languages_dict.values():
        current_pair = f'{my_language}' \
                       f'-{language.lower()}'
        current_lang = language

        url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
        r = ''
        try:
            s = requests.Session()
            r = s.get(url, headers={'User-Agent': user_agent})
        except requests.exceptions.ConnectionError:
            print('Something wrong with your internet connection')

        if int(r.status_code) == 404:
            print(f'Sorry, unable to find {word_to_translate}')
            sys.exit(0)

        soup = BeautifulSoup(r.text, 'html.parser')
        word_translations_list = soup.find_all('a', class_='translation')
        word_translations_list = [t.text.strip() for t in word_translations_list]
        word_translations_list.remove(word_translations_list[0])
        sentences_list = soup.find_all(class_='text')
        sentences_list = [t.text.strip() for t in sentences_list]
        sentences_list = sentences_list[46:]

        print(f'{current_lang} Translations:')
        file.write(f'{current_lang} Translations:\n')
        for translate in word_translations_list:
            print(translate)
            file.write(translate + '\n')
            break
        print()
        file.write("\n")

        print(f'{current_lang} Example:')
        file.write(f'{current_lang} Example:\n')
        j = 0
        for sentence in sentences_list:
            if j == 2:
                break
            print(sentence)
            file.write(sentence + '\n')
            j += 1
        print()
        file.write("\n")


file.close()
