def get_book_text(book_name):
    with open(book_name) as file:
        return file.read()
def get_word_count(book_name):
    with open(book_name) as file:
        print(f"Found {len(get_book_text(book_name).split())} total words")

def get_letter_count(book_name):
    with open(book_name) as file:
        dict={}
        list=get_book_text(book_name).lower()
        for i in list:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        return dict
def get_tally_text(book_name):
    char_counts=get_letter_count(book_name)
    lst=[]
    for char, count in char_counts.items():
        lst.append({"char":char,"num":count})
    lst.sort(reverse=True, key=lambda item: item["num"])
    return lst
        



