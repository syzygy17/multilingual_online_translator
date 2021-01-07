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

print('Type the number of a language you want to translate to or \'0\' to translate to all languages:')
language_to_translate = int(input())

print('Type the word you want to translate:')
word_to_translate = input()

file = open(f'{word_to_translate}.txt', 'a', encoding='utf-8')
if file:
    file.truncate(0)

s = requests.Session()

if language_to_translate != 0:
    current_pair = f'{support_languages_dict.get(my_language).lower()}' \
                   f'-{support_languages_dict.get(language_to_translate).lower()}'
    current_lang = support_languages_dict.get(language_to_translate)

    url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
    r = s.get(url, headers={'User-Agent': user_agent})

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
    for i in support_languages_dict.keys():
        current_pair = f'{support_languages_dict.get(my_language).lower()}' \
                       f'-{support_languages_dict.get(i).lower()}'
        current_lang = support_languages_dict.get(i)

        url = 'https://context.reverso.net/translation/' + current_pair + '/' + word_to_translate
        r = s.get(url, headers={'User-Agent': user_agent})

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
