def decryption(file: str):
    alphabet = "МЕУ4>ДИЙОРt1rЛХ28АЧЩ< ЪФКП7ШЬ5Ы"
    dec_alphabet = " ОИАЕНСТВДРЛПЯКМЗЬУХЧЫЦЙЮГЖФЩБШ"
    text = []
    count = {}
    how = 0

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
    
    print(sorted(count.items(), key=lambda x: x[1], reverse=True))

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                place = alphabet.find(i)
                if i in alphabet:
                    text.append(dec_alphabet[place])
                else:
                    text.append(i)
    
    res_file = open('result_text2.txt', 'w', encoding="utf-8")
    for symbol in text:
        res_file.write(symbol)
    res_file.close()

    new_file = open('Key2.txt', 'w', encoding="utf-8")
    new_file.write("Алфавит: ")
    for letter1 in alphabet:
        new_file.write(letter1)
    new_file.write("\n")      
    new_file.write("Ключ: ")
    for letter in dec_alphabet:
        new_file.write(letter)

if __name__ == "__main__":
    decryption("text2.txt")
