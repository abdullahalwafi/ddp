# Soal 2 membalikan urutan saat di print
def balikan(array) :
    arrayBaru = []
    for i in range(len(array) -1,-1,-1):    
        arrayBaru.append(array[i])
    print(arrayBaru)

balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])