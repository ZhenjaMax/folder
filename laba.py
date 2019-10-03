import wikipedia
from help_wiki_function import is_page_valid
pages_list = input().split(', ')

if pages_list[-1] in wikipedia.languages():
    wikipedia.set_lang(pages_list[-1])
    del pages_list[-1]
else:
    print('no results')
    exit()

i = 0
while i < len(pages_list):
    if not is_page_valid(i):
        pages_list.remove(pages_list[i])
        i -= 1

max_words, page_number_max = 0, 0
for i in range(len(pages_list)):
    words = len(wikipedia.summary(pages_list[i]).split())
    if words >= max_words:
        max_words = words
        page_number_max = i
print(max_words, wikipedia.page(pages_list[page_number_max]).title)

chain = [pages_list[0]]
for i in range(len(pages_list) - 1):
    links = wikipedia.page(pages_list[i]).links
    if pages_list[i + 1] in links:
        chain.append(pages_list[i + 1])
    else:
        j, not_finded = 0, True
        while not_finded:
            sublinks = wikipedia.page(links[j]).links
            if pages_list[i + 1] in sublinks:
                chain.append(links[j])
                chain.append(pages_list[i + 1])
                not_finded = False
print(chain)
