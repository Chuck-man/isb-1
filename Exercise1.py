def code(file: str) -> None:
    alfavit = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dec_alfavit = "ГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    text = []

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                i = i.upper()
                place = alfavit.find(i)
                if i in alfavit:
                    text.append(dec_alfavit[place])
                else:
                    text.append(i)

    new_file = open('output.txt', 'w')
    for element in text:
        new_file.write(element)
    new_file.close()

    new_file = open('alfavit.txt', 'w')
    new_file.write("Ключ: ")
    for element in dec_alfavit:
        new_file.write(element)
    new_file.write("\n")
    new_file.write("      ")
    for element in alfavit:
        new_file.write(element)
    new_file.close()


if __name__ == "__main__":
    code("test.txt")
