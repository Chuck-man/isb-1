def encryption(file: str):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    dec_alphabet = "гдежзийклмнопрстуфхцчшщъыьэюяабв"
    text = []

    with open(file, encoding="utf=8") as f:
        for i in f:
            for j in i:
                j = j.lower()
                finding = alphabet.find(j)
                if j in alphabet:
                    text.append(dec_alphabet[finding])
                else:
                    text.append(i)
    
    res_file = open('result_text.txt', 'w')
    for symbol in text:
        res_file.write(symbol)
    res_file.close()

if __name__ == "__main__":
    encryption("text.txt")