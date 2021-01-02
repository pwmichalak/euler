ten = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

lenTeens = sum([len(i) for i in teens])
lenTen = sum([len(i) for i in ten])
lenTens = sum([len(i) for i in tens])
total = 0
total += (lenTen + lenTeens + lenTens)
for t in tens:
    total += sum([(len(t) + len(j)) for j in ten])
for i in ten:
    total += sum([(len(i) + len("hundred") + len("and") + len(j)) for j in ten])
    total += sum([(len(i) + len("hundred") + len("and") + len(j)) for j in teens])
    total += sum([len(i) + len("hundred") + len("and") + len(t) for t in tens])
    for t in tens:
        total += sum([(len(i) + len("hundred") + len("and") + len(t) + len(j)) for j in ten])
total += len("one") + len("thousand")
total += sum([len(t) + len("hundred") for t in ten])
print(total)