salario_atual = int(input("Digite o valor do salário inteiro atual: "))
porcentagem = int(input("Agora, digite a porcentagem de quanto deseja aumentar ou diminuir o salário digitado acima: "))

resultado_porcentagem = salario_atual * porcentagem / 100;

salario_ajustado_para_mais = salario_atual + resultado_porcentagem
salario_ajustado_para_menos = salario_atual - resultado_porcentagem


print(f"Muito bem...\nO salário atual é de R${salario_atual},00")
print(f"A porcentagem que deseja aumentar/diminuir, é de {porcentagem}%")
print(f"{porcentagem}% de R${salario_atual},00 é igual a R${resultado_porcentagem}0")
print(f"Fazendo as contas necessárias, o salário ajustado do funcionário será de R${salario_ajustado_para_mais}0 para mais, ou R${salario_ajustado_para_menos}0 para menos")