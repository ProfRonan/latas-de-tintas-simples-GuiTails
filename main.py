print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
Valor1 = metros_quadrados / 54 
if Valor1 ==0:
    X = 0
if Valor1 > 0 and Valor1 <=1:
    X = 1
if Valor1 > 1 and Valor1 <=2:
    X = 2
if Valor1 > 2 and Valor1 <=3:
    X = 3
if Valor1 > 3 and Valor1 <=4:
    X = 4
if Valor1 > 4 and Valor1 <=5:
    X = 5
# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = X
valor_total = 80*X

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
