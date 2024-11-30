def main():
    fn = 'books/frankenstein.txt'
    with open(fn, 'r') as f:
        file_contents = f.read()
    
    words = file_contents.split()
    wc = len(words)

    char_count = {}
    text_lower = file_contents.lower()
    for c in text_lower:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    alpha_character_count_list = []
    for c in char_count:
        if c.isalpha():
            alpha_character_count_list.append({'char':c, 'count':char_count[c]})
    
    def sort_on(x):
        return x["count"]
    
    alpha_character_count_list.sort(reverse=True, key=sort_on)
    
    print(f'--- Begin report of {fn} ---')
    print(f'{wc} words found in the document\n')
    for alpha_count in alpha_character_count_list:
        print(f'The "{alpha_count["char"]}" character was found {alpha_count["count"]} times')
    print('--- End report ---')

main()