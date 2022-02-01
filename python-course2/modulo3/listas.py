num = [1,2,3,4,5]
num [2] = 2
# var.append() para adicionar no final
num.append(6)

# var.sort() para organizar
# var.sort(reverse=True) para organizar ao contrario

# num.insert(2,0) add elemento 0 na posicao 2 

# var.pop(x) deleta o 1 elemento como padrao

# var.remove(x) deleta o valor q vc mandou deletar

if 4 in num:
  num.remove(4)
else:
  print('não tem numero 4')

print(num)