list = ['a','a','a', 'b', 'c','c','d','e','c','c','f']

def remove_duplicates(list):
    deduped = []
    for i in list:
        if i not in deduped:
            deduped.append(i)
    return deduped

print(remove_duplicates(list))
