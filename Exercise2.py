def decryption(file: str):
    alphabet = "МУ4Е>ИДЙt1ОРEЛrХ28M OАЧ<ЩPФЪКШП7-A5XІТ!ЫпЬгb"
    dec_alphabet = " ОИЕТНСАКЯРМЛПВДЬУЧЙЗЖЭЫГЦ,ФБЮХЩШ"
    text = []
    count = {}

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
    
    print(sorted(count.items(), key=lambda x: x[1], reverse=True))

    


if __name__ == "__main__":
    decryption("text2.txt")
