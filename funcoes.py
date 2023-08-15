import random
class sorts:
    
    def quickSort(init, fim, tam):
        print("executar quick")
        #if(init<fim):
            #m=order(init, fim)
            #quickSort(init, m)
            #quickSort(m+1, fim)
            
    def mergeSort(init, fim, tam):
        print("executar merge")
        #if(init<fim):
            #mergeSort(init, m)
            #mergeSort(m+1, fim)
            #m=order(init, fim)
            
    def selectionSort(init, fim, tam):
        print("executar select")
        
    def insertionSort(init, fim, tam):
        print("executar insertion")
        
    def heapSort(init, fim, tam):
        print("executar heap")
        
    def countingSort(init, fim, tam):
        print("executar counting")
        


#Classe responsável pela geração de vetores com suas devidas especificações 
class geradorLista:
    
    
    #Função que gera um vetor com valores semialeatórios, que fica organizado de forma randomica
    
    #Resumo:
    
    #Inicialmente ele inicia os valores no vetor "valores", valores escolhidos ficam dentro do espaço de inc e fim andando em intervalos stp,
    #depois de "valores" definido, eles são guardos de forma randomica no vetor "vetor" até atingir 70% de ocupação
    #partir desse ponto pegamos o resto do vetor "valores", e guardamos no oque sobrou no vetor "vetor"
    
    def gerarVetorAleatorio(inc, fim, stp):
        print("executar")
        
        
    #Função responsável por gerar vetor em ordem decrescente
    
    #Resumo:
    
    #São pegos valores de fim até inc dentro de intervalos stp e guardos em vetor
        
    def gerarVetorReverso(inc, fim, stp):
            print("executar")
        
        
    #Função responsável por gerar vetor em ordem crescente
    
    #Resumo:
    
    #São pegos valores de inc até fim dentro de intervalos stp e guardos em vetor
    
    def gerarVetorOrdenado(inc, fim, stp):
            print("executar")
    
    
    #Função responsável por gerar vetor em ordem crescente, e desorganizar este até certo ponto
    
    #Resumo:
    
    #São pegos valores de inc até fim dentro de intervalos stp e guardos em vetor, pós isso pegamos duas posições aleatórias do vetor
    #e trocamos seus valores de lugar isso x vezes até que 10% deste vetor esteja desorganizado
     
    def gerarVetorQuaseOrdenado(inc, fim, stp):
            print("executar")
    
    
    ## Observação em todas as funções valores negativos que apareçam durante a geração não são guardos em valores, e se o tamanho de valores
    ## passar de 20000, a adição de valores no vetor será interrompida fazendo que intermitantemente o tamanho do vetor fique limitado a 20000
    

#Classe gerador documento saída
#class geradorDocSaida:


#Classe gerador graficos saída
#class geradorGraficos: