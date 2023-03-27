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
                    text.append(j)
    
    res_file = open('result_text.txt', 'w')
    for symbol in text:
        res_file.write(symbol)
    res_file.close()

    new_file = open('Key.txt', 'w')
    new_file.write("Алфавит: ")
    for letter1 in alphabet:
        new_file.write(letter1)
    new_file.write("\n")      
    new_file.write("Ключ: ")
    for letter in dec_alphabet:
        new_file.write(letter)
    

if __name__ == "__main__":
    encryption("text.txt")