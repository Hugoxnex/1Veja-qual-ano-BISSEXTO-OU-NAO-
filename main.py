ano = int(input(" Qua ano voce quer Analisar ? "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(" O ano {} é BISSEXTO ".format(ano))
else:
    print(" O ano {} NÂO é BISSEXTO".format(ano))