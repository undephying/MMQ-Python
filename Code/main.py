import math as math

listX = []
listY = []

#Definir tamanho da lista e os dados dentro de ambos X e Y
sizeOfList = int(input("Dados por grade: "))
i = 1
while i<=sizeOfList:
    uinput = float(input("Inserir dado coeficiente X (Dependente): "))
    listX.append(uinput)
    i = i+1
i = 1
while i<=sizeOfList:
    uinput = float(input("Inserir dado do coeficiente Y (Intependente): "))
    listY.append(uinput)
    i = i+1                      

#Calcular o somatório MULTIPLICATIVO (X vai sempre ser uma lista nessa função)
def sumOf(X, Y):      
    sumOfAll = 0   
    #Verifica se Y (da função) é uma lista, se não Y = [1, 1, 1, 1, ...] com o mesmo tamanho da lista X.
    if isinstance(Y, list) == False:
        Y = []
        for i in range(len(X)):
            uinput = 1
            Y.append(uinput)
    #Somatório da múltiplicação de X e Y                  
    for i in range(len(X)):                 #Se Y não foi definida como uma lista, o código vai executar *somente* o
        sumOfAll = sumOfAll + (X[i] * Y[i]) #somatório de X (X1 * 1 + X2 * 1 +....). Se Y foi definida como uma lista,
                                            #o código vai executar como (X1 * Y1 + X2 * Y2 +....)
    return sumOfAll

#n & D
n = len(listX)
D = (n*sumOf(listX, listX))-(sumOf(listX, 1)*sumOf(listX, 1))

#a (Coeficiente linear)
a =((sumOf(listX, listX)*sumOf(listY, 1))-(sumOf(listX, 1)*sumOf(listX, listY)))/D
#print("Linear (a) = ", a)

#b (Coeficiente angular)
b = ((n*sumOf(listX, listY))-(sumOf(listX, 1)*sumOf(listY, 1)))/D
#print("Angular (b) = ", b)

#𝜎^2 (Sigma ao quadrado)
##Calcular o somatório de (yi - a - bxi)^2:
sig = 0
for i in range(len(listX)):
    sig = sig + ((listY[i] - a - (b*listX[i]))*(listY[i] - a - (b*listX[i])))
##Calcular sigma^2:
sigmaSQ = sig/(n-2)

#𝛿a^2 (Desvio padrão de a ao quadrado)
desvioASQ = (1/D)*(sumOf(listX, listX))*sigmaSQ

#𝛿b^2 (Desvio padrão de b ao quadrado)
desvioBSQ = (1/D)*n*sigmaSQ

#Ylinha
yLinha = sumOf(listY, 1)/n

#R^2
##Calcular o somatório de (a+bxi-ylinha)^2
rTop = 0
for i in range(len(listX)):
    rTop = rTop + ((a+(b*listX[i])-yLinha)*(a+(b*listX[i])-yLinha))
##Calcular o somatório de (yi-ylinha)^2
rBot = 0
for i in range(len(listX)):
    rBot = rBot + ((listY[i]-yLinha)*(listY[i]-yLinha))
##Calcular R^2
rSQ = (rTop)/(rBot)

#𝜒^2
chiSQ = 0
for i in range(len(listX)):
    chiSQ = chiSQ + ((listY[i]-a-(b*listX[i]))*(listY[i]-a-(b*listX[i])))

#RESPOSTAS
print("------------------------------------------------------------")
print("Coeficiente Linear: ", a, " ± ", math.sqrt(desvioASQ))
print("Coeficiente Angular: ", b, " ± ", math.sqrt(desvioBSQ))
print("------------------------------------------------------------")
print("Chi^2: ", chiSQ)
print("R^2: ", rSQ)
print("------------------------------------------------------------")