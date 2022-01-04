english = {}
word = 'None'

while word !='quit':
    word = input('영어 단어 등록 (종료는 quit) : ')
    if word not in english and word != 'quit':
        meaning = input('%s의 뜻 입력 (종료는 quit) : '%word)
        print()
        english[word] = meaning
    elif word in english :
        print('%s는 이미 등록된 단어 입니다. \n' %word)
        continue
    elif word =='quit':
        break
print()

search = 'None'

while search != 'quit':
    search = input('검색할 단어 입력 (종료는 quit) : ')
    if search in english.keys():
        print('%s의 뜻은 %s입니다. \n' %(search , english[search]))
    elif search not in english.keys() and search != 'quit':
        print('%s는 사전에 없는 단어 입니다. \n'%search)
        continue
    elif search == 'quit':
        break
print()
print('종료합니다.')










# word = None
# meaning = None
#
#
# while word !='quit':
#     word = input('단어입력 : ')
#     meaning = input('%s의 뜻 입력 (종료는 quit) : ' % word)
#     if word == 'quit':
#         break
#         if meaning =='quit':
#             break
#         elif word not in english:
#             print('%s는 이미 등록된 단어 입니다')







# while (word or meaning) != 'quit':
#     word = input('영어 단어 등록 (종료는 quit) : ')
#     if word not in english:
#         meaning = input('%s의 뜻 입력 (종료는 quit) : ' %word)
#         english.update({word: meaning})
#     elif word in english:
#         print('%s는 이미 등록된 단어 입니다.'%word)
#     elif (word or meaning) == 'quit':
#         break


# search = None
# while search != 'quit':
#     search = input('검색할 단어 입력 (종료는 quit) : ')
#     print('%s의 뜻은 %s 입니다.' %(search , english[search]))
#     if search == 'quit':
#         break
#     else :
#         print('%s는 사전에 없는 단어 입니다.' %search)
#         continue
