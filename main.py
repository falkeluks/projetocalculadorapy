
import adicao 
import multi
import divisao
import subtracao

def chamada_princiapal():
    print("-------------- Calculadora #foda --------------")
    print("\n       Escolha qual operação deseja fazer:\n 1 Para adição: \n 2 Para subtração:\n 3 Para divisão:\n 4 Para multiplicação:")
def entrada_de_valores(valor):
    valor = int(input("Entrada : "))
    return valor
def operacao(valor):
        var1 = int(input("Entre com o primeiro valor: "))
        var2 = int(input("Entre com o segundo valor: "))
        if (valor == 1) :
            result = adicao.calcular(var1, var2)
            print(var1," + ", var2, " = ", result)
        elif (valor == 2):
            result = subtracao.calcular(var1, var2)
            print(var1," - ", var2, " = ", result)
        elif (valor == 3 ):
            result = divisao.calcular(var1, var2)
            print(var1," / ", var2, " = ", result)
        elif (valor == 4):
            result = multi.calcular(var1, var2)
            print(var1," * ", var2, " = ", result)
        


def mainmenu() :

    intencao = "s".lower()
    memoria = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    valor = 0
    contador_armazenamento_memoria = 0
    
    chamada_princiapal()

    while(intencao == "s".lower()):
        
        valor = entrada_de_valores(valor)
        
        result = operacao(valor)

        teste = input("Deseja armazenar o resultado?\n Envia S para sim e N para não: \n").lower()
        if(teste == "s"):
            memoria[contador_armazenamento_memoria] = result
            print("O valor salvo está alocado na memória de número {}".format(contador_armazenamento_memoria + 1))
            contador_armazenamento_memoria += 1

        intencao = input("Deseja fazer outra operação? s ou n \n").lower()


if(__name__ == "__main__"):
    mainmenu()