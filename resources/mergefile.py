names = [line.rstrip() for line in open(r'C:\Users\User\Documents\TP_ES\resources\nomes_professores.txt',encoding="utf-8")]
img = [line.rstrip() for line in open(r'C:\Users\User\Documents\TP_ES\resources\urls_fotos',encoding="utf-8")]

file = open('data.csv', 'w')
for i in range (len(names)):
    file.write(names[i] + ';' + img[i] + '\n')

file.close()